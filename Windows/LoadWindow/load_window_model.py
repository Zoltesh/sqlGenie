"""
Load Window Model handles business logic. It reads in data, parses data, and outputs data.
It is not aware of operations in the Conrtoller or View. It is only made available through
instances created by the Controller.
"""
import os
import re
from tkinter import filedialog


class LoadWindowModel:
    """
    Handles the business logic such as reading and writing data
    """
    def __init__(self, on_file_loaded_callback=None):
        """
        Initialize file path and variable list. Use of callback method to fill data upon
        initialization
        :param on_file_loaded_callback:
        """
        self.query_path = None
        self.var_list = []
        self.on_file_loaded = on_file_loaded_callback
        self.variable_hashmap = {}

    def load_new_file(self):
        """
        Present user with file dialogue to select a sql file
        :return:
        """
        self.query_path = filedialog.askopenfilename(filetypes=[('SQL Files', '*.sql')])
        if self.query_path:
            self.var_list = []
            self.variable_hashmap = {}
            self.parse_variables(self.query_path)
            self.create_variable_hashmap()
            if self.on_file_loaded:
                self.on_file_loaded()


    def parse_variables(self, path):
        """
        Using custom sql tagging to retrieve variables and descriptions. Variables are denoted with
        --VAR-- and the corresponding description is denoted with --[VAR] blah blah--
        :param path:
        :return:
        """
        with open(path, 'r', encoding='utf-8') as file:
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
                        self.variable_hashmap[match] = {'variable': match,
                                                        'description': 'NO DESCRIPTION'}

            # At the end, update VAR_LIST based on hashmap values
            self.var_list = list(self.variable_hashmap.values())

    def create_variable_hashmap(self):
        """
        List comprehension creates a list of dictionaires, where each outer dictionary contains a
        key that is the name of the variable from the sql file and its value is another dictionary.
        The format looks like this: [{'variable1': {'variable1': 'value', 'description': 'value'}},
        {{}}]
        :return:
        """
        self.variable_hashmap = {d['variable']: d for d in self.var_list}

    def get_variable_hashmap(self):
        """
        Retrieve the hashmap
        :return:
        """
        return self.variable_hashmap

    def save_to_file(self, modified_query_content):
        """
        Writes the modified query content to the new file.
        :param modified_query_content:
        :return:
        """
        try:
            output_filename = self.query_path.replace('.sql', 'modified.sql')
            with open(output_filename, 'w', encoding='utf-8') as out_file:
                out_file.write(modified_query_content)
        except AttributeError as e:
            print(e)

    def generate_modified_query(self):
        """
        Create a copy of the original sql query and replace all --placeholders-- with the new
        values provided by the user.
        :return:
        """
        try:
            output_filename = self.query_path.replace('.sql', 'modified.sql')
            read_path = output_filename if os.path.exists(output_filename) else self.query_path
        except AttributeError:
            return None

        with open(read_path, 'r', encoding='utf-8') as file:
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
