import re
from tkinter import filedialog


class LoadWindowModel:
    def __init__(self, on_file_loaded_callback=None):
        self.QUERY_PATH = None
        self.VAR_LIST = []
        self.on_file_loaded = on_file_loaded_callback
        self.variable_hashmap = {}

    def load_new_file(self):
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

    def save_to_file(self):
        # Select file to save to
        # Make sure loaded file is the same file being written to
        pass

    # Add any other necessary methods/functions related to data or business logic here
