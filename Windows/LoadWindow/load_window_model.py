import os
import re
from tkinter import filedialog


class LoadWindowModel:
    def __init__(self, on_file_loaded_callback=None):
        self.QUERY_PATH = None
        self.VAR_LIST = []
        self.on_file_loaded = on_file_loaded_callback
        self.variable_hashmap = {}

    def load_new_file(self):
        self.QUERY_PATH = None
        self.VAR_LIST = []
        self.variable_hashmap = {}
        self.QUERY_PATH = filedialog.askopenfilename(filetypes=[('SQL Files', '*.sql')])
        if self.QUERY_PATH:
            self.parse_variables(self.QUERY_PATH)
            self.create_variable_hashmap()
            if self.on_file_loaded:
                self.on_file_loaded()

    def parse_variables(self, path):
        # State definitions
        outside = 0
        inside_var = 1
        inside_description = 2
        state = outside

        current_var = None

        with open(path, 'r') as file:
            for line in file:
                line = line.strip()

                # Transition states if needed
                if 'VARIABLE_START' in line.replace(" ", ""):
                    state = inside_var
                    continue
                elif 'VARIABLE_END' in line.replace(" ", ""):
                    state = outside
                    continue
                elif 'DESCRIPTION_START' in line.replace(" ", ""):
                    state = inside_description
                    continue
                elif 'DESCRIPTION_END' in line.replace(" ", ""):
                    state = outside
                    continue

                # Process based on state
                if state == inside_var:
                    match = re.search(r'--\[?(.*?)\]?--', line)
                    if match:
                        current_var = match.group(1)
                        # Check if the variable already exists in the list
                        if not any(d['variable'] == current_var for d in self.VAR_LIST):
                            self.VAR_LIST.append({'variable': current_var, 'description': 'NO DESCRIPTION'})

                elif state == inside_description:
                    _, description = line.split('] ', 1)
                    # Update the last added dictionary (since it's in sequence, it should be the one for this
                    # description)
                    if self.VAR_LIST:
                        self.VAR_LIST[-1]['description'] = description.strip()

    def create_variable_hashmap(self):
        self.variable_hashmap = {d['variable']: d for d in self.VAR_LIST}

    def get_variable_hashmap(self):
        return self.variable_hashmap

    def save_to_file(self, modified_query_content):
        # Generate the output filename
        try:
            output_filename = self.QUERY_PATH.replace('.sql', 'modified.sql')

            # Save the modified query to the new file
            with open(output_filename, 'w') as out_file:
                out_file.write(modified_query_content)
        except AttributeError as e:
            print(e)

    def generate_modified_query(self):
        # Determine the correct path to read from
        try:
            output_filename = self.QUERY_PATH.replace('.sql', 'modified.sql')
            if os.path.exists(output_filename):
                read_path = output_filename
            else:
                read_path = self.QUERY_PATH
        except AttributeError:
            return None

        # Read the content from the appropriate file
        with open(read_path, 'r') as file:
            query_content = file.read()

        # List of keys to remove from hashmap after processing
        keys_to_remove = []

        # Iterate over each variable in the hashmap
        for variable, data in self.variable_hashmap.items():
            # If the internal variable has been changed by the user
            if data['variable'] != variable:  # Using the nested 'variable' to compare
                # Replace all instances of that variable in the query content
                placeholder_in_file = '--' + variable + '--'
                new_value = data['variable']
                query_content = query_content.replace(placeholder_in_file, new_value)
                keys_to_remove.append(variable)

        # Remove the processed variables from the hashmap
        for key in keys_to_remove:
            del self.variable_hashmap[key]

        return query_content



