"""
Load Window Model handles business logic. It reads in data, parses data, and outputs data.
It is not aware of operations in the Conrtoller or View. It is only made available through
instances created by the Controller.
"""
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
        self.QUERY_PATH = filedialog.askopenfilename(filetypes=[('SQL Files', '*.sql')])
        if self.QUERY_PATH:
            self.VAR_LIST = []
            self.variable_hashmap = {}
            self.parse_variables(self.QUERY_PATH)
            self.create_variable_hashmap()
            if self.on_file_loaded:
                self.on_file_loaded()


    def parse_variables(self, path):
        with open(path, 'r') as file:
            for line in file:
                line = line.strip()

                # Check for a description
                desc_matches = re.findall(r'--\[(.*?)\](.*?)(?=\s*--|$)', line)
                for desc_match in desc_matches:
                    variable_name = desc_match[0]
                    description = desc_match[1].strip()
                    if variable_name and description:  # Check to ensure no blank entries
                        if variable_name in self.variable_hashmap:
                            # Update the hashmap's description
                            self.variable_hashmap[variable_name]['description'] = description
                        else:
                            # If variable not yet in hashmap, add it with description
                            self.variable_hashmap[variable_name] = {'variable': variable_name,
                                                                    'description': description}

                # Check for a variable match, but make sure the character after '--' isn't '['
                matches = re.findall(r'--(?!\[)(.*?)--', line)
                for match in matches:
                    match = match.strip()
                    if match and match not in self.variable_hashmap:
                        self.variable_hashmap[match] = {'variable': match, 'description': 'NO DESCRIPTION'}

            # At the end, update VAR_LIST based on hashmap values
            self.VAR_LIST = list(self.variable_hashmap.values())

    def create_variable_hashmap(self):
        self.variable_hashmap = {d['variable']: d for d in self.VAR_LIST}

    def get_variable_hashmap(self):
        return self.variable_hashmap

    def save_to_file(self, modified_query_content):
        try:
            output_filename = self.QUERY_PATH.replace('.sql', 'modified.sql')
            with open(output_filename, 'w') as out_file:
                out_file.write(modified_query_content)
        except AttributeError as e:
            print(e)

    def generate_modified_query(self):
        try:
            output_filename = self.QUERY_PATH.replace('.sql', 'modified.sql')
            read_path = output_filename if os.path.exists(output_filename) else self.QUERY_PATH
        except AttributeError:
            return None

        with open(read_path, 'r') as file:
            query_content = file.read()

        keys_to_remove = []

        for variable, data in self.variable_hashmap.items():
            if data['variable'] != variable:
                placeholder_in_file = '--' + variable + '--'
                # Strip any leading or trailing whitespace
                new_value = data['variable'].strip()
                query_content = query_content.replace(placeholder_in_file, new_value)
                keys_to_remove.append(variable)

        for key in keys_to_remove:
            del self.variable_hashmap[key]

        return query_content
