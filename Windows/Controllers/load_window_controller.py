"""
load_window logic
"""

from tkinter import filedialog
from Windows.load_window import LoadWindow
import re

# Path to loaded query
QUERY_PATH = ''
# Key/Value VAR/DESCR
VAR_DICT = []


def load_new_file():
    # Assign file path to global variable
    # query_file_path = filedialog.askopenfile().path
    pass


def parse_variables(path, var_dict):
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
                # Use regex to find pattern like --MY_VALUE--
                match = re.search(r'--\[?(.*?)\]?--', line)
                if match:
                    current_var = match.group(1)
                    if current_var not in var_dict:
                        var_dict[current_var] = 'NO DESCRIPTION'
                else:
                    print(f"Failed to match: {line}")

            elif state == inside_description:
                # Extract description from format like --[MY_VALUE] This is the description
                # Extract variable and description from format like --[MY_VALUE] This is the description
                var_match, description = line.split('] ', 1)
                current_var = var_match.replace("--[", "")
                var_dict[current_var] = description.strip()


# Testing
parse_variables('C:\\Users\\Brayden\\PycharmProjects\\sqlGenie\\Queries\\Test1\\sample querey.sql', VAR_DICT)
print(VAR_DICT)


def save_to_file():
    # Select file to save to
    # Make sure loaded file is same file being written to
    pass


def populate_fields():
    # Insert data from loaded query into vars and description
    # Selected var ON SELECT should display partial line where value resides, with the value being
    # highlighted or otherwise stand out
    pass


def show_load_window(parent):
    load_win = LoadWindow(parent)
    parent.wait_window(load_win.app)
