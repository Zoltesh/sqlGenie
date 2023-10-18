"""
Allows the user to Load a query. The file contains placeholder text and the UI provides the user
with the ability to fill out the placeholders in a clear and clean way
"""

import customtkinter as ctk

# TODO Switch to a modular class like approach for the Frames
#   class Frame1(ctk.CTkFRAME)


class LoadWindow:
    """
    Load window enables the user to load a sql file to perform placeholder replacements
    """
    def __init__(self, parent, controller):
        # An instance of the Controller class to act as liaison between model and view
        self.controller = controller
        # Parent Frames
        self.parent_frame_1 = None
        self.parent_frame_2 = None
        self.parent_frame_3 = None
        self.parent_frame_4 = None

        # Frame 1 widgets
        self.window_title = None

        # Frame 2 widgets
        self.variable_label = None
        self.variable_combobox = None
        self.variable_textbox = None
        self.apply_button = None
        self.description_label = None
        self.description_textbox = None

        # Frame 3 widgets
        self.query_output_textbox = None
        self.save_btn = None
        self.load_new_btn = None
        self.cancel_btn = None

        self.configs = {
            'title': {'font': ('Arial', 22, 'bold')},
            'label': {'font': ('Arial', 16)},
            'button': {'font': ('Arial', 18)},
            'text': {'font': ('Arial', 14)}
        }

        self.description_box = None
        self.query_input = None

        self.query_label = None

        self.browse_btn = None
        self.app = ctk.CTkToplevel(parent)
        # Prevent user from loading more windows on the root window
        self.app.grab_set()
        self.app.geometry('800x600')
        self.app.configure(bg='#2a3439')
        self.app.title('Load Query')

        self.setup_ui()
        self.initialize_ui_elements()

    def initialize_ui_elements(self):
        """
        The combobox and textboxes must be initialized upon the user's first interaction
        :return:
        """
        variable_names = list(self.controller.variable_hashmap.keys())
        self.variable_combobox.configure(values=variable_names)

        if variable_names:
            default_variable_name = variable_names[0]
            default_description = (
                self.controller.variable_hashmap)[default_variable_name]['description']

            self.variable_combobox.set(default_variable_name)
            self.description_textbox.insert('0.0', default_description)
            self.variable_textbox.insert('0.0', default_variable_name)

    def setup_ui(self):
        """
        Handles placement and design of widgets upon the Load Window
        :return:
        """
        # Configuration of the User Interface
        self.app.minsize(800, 600)
        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=2)
        self.app.grid_rowconfigure(2, weight=5)

        # Title frame only contains a title
        self.parent_frame_1 = ctk.CTkFrame(self.app)
        self.parent_frame_1.grid(row=0, column=0, sticky='nsew')
        self.parent_frame_1.columnconfigure(0, weight=1)
        self.parent_frame_1.rowconfigure(0, weight=0)

        # New keyword frame. Provides label, combobox, textbox, and Apply button
        self.parent_frame_2 = ctk.CTkFrame(self.app)
        self.parent_frame_2.grid(row=1, column=0, sticky='nsew')
        self.parent_frame_2.columnconfigure(0, weight=0)
        self.parent_frame_2.columnconfigure(1, weight=0)
        self.parent_frame_2.columnconfigure(2, weight=3)
        self.parent_frame_2.rowconfigure(0, weight=0)
        self.parent_frame_2.rowconfigure(1, weight=0)

        # Query preview contains only a single large textbox
        self.parent_frame_3 = ctk.CTkFrame(self.app)
        self.parent_frame_3.grid(row=2, column=0, sticky='nsew')
        self.parent_frame_3.columnconfigure(0, weight=1)
        self.parent_frame_3.columnconfigure(1, weight=1)
        self.parent_frame_3.columnconfigure(2, weight=1)
        self.parent_frame_3.rowconfigure(0, weight=3)
        self.parent_frame_3.rowconfigure(1, weight=1)

        # Parent 4 is the bottom row containing the Cancel, Load New, and Save buttons
        self.parent_frame_4 = ctk.CTkFrame(self.app)
        self.parent_frame_4.grid(row=3, column=0, sticky='nsew')
        self.parent_frame_4.columnconfigure(0, weight=1)
        self.parent_frame_4.columnconfigure(1, weight=1)
        self.parent_frame_4.columnconfigure(2, weight=1)

        # Frame 1's Widgets
        # A single label
        self.window_title = ctk.CTkLabel(self.parent_frame_1, text='Load Query')
        self.window_title.configure(**self.configs['title'])
        self.window_title.grid(row=0, column=0, sticky='nsew')

        # Frame 2's widgets
        # A label for the combobox
        self.variable_label = ctk.CTkLabel(self.parent_frame_2, text='Variables')
        self.variable_label.configure(**self.configs['label'])
        self.variable_label.grid(row=0, column=0, padx=(10, 0), sticky='w')

        # Holds the variable names
        self.variable_combobox = ctk.CTkComboBox(self.parent_frame_2, values=[''],
                                                 command=self.handle_variable_selection_change)
        self.variable_combobox.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        self.variable_combobox.set('')

        # Display the current value of the selected variable. Is editable and savable with the
        # Apply button
        self.variable_textbox = ctk.CTkTextbox(self.parent_frame_2, height=30)
        self.variable_textbox.configure(**self.configs['text'])
        self.variable_textbox.grid(row=0, column=2, sticky='nsew', padx=10)

        # Sets the current text in variable_textbox as the new value of the selected item's
        # variable key
        self.apply_button = ctk.CTkButton(self.parent_frame_2, text='Apply',
                                          command=self.update_variable_callback)
        self.apply_button.configure(**self.configs['button'])
        self.apply_button.grid(row=0, column=3, sticky='nsew', padx=10)

        # A label for the description textbox
        self.description_label = ctk.CTkLabel(self.parent_frame_2, text='Description', width=30)
        self.description_label.configure(**self.configs['label'])
        self.description_label.grid(row=1, column=0, sticky='nw', padx=10)

        # The description textbox displays the selected item's value at the 'description' key.
        # Is not editable
        self.description_textbox = ctk.CTkTextbox(self.parent_frame_2, wrap='word')
        self.description_textbox.configure(**self.configs['text'])
        self.description_textbox.grid(row=1, column=1, columnspan=2, sticky='nsew', pady=10,
                                      padx=10)

        # Frame 3 widgets
        # A single large textbox to provide a view of the output file
        self.query_output_textbox = ctk.CTkTextbox(self.parent_frame_3)
        self.query_output_textbox.configure(**self.configs['text'])
        self.query_output_textbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10,
                                       sticky='nsew')
        self.query_output_textbox.columnconfigure(0, weight=1)
        self.query_output_textbox.rowconfigure(0, weight=1)

        # Frame 4's widgets
        # A button to destroy the Load Window and return to the Main Window
        self.cancel_btn = ctk.CTkButton(self.parent_frame_4, text='Cancel',
                                        command=self.app.destroy)
        self.cancel_btn.configure(**self.configs['button'])
        self.cancel_btn.grid(row=0, column=0, padx=10, pady=10, sticky='sw')

        # A button that triggers the load_new_file method. Allows user to select a sql file
        self.load_new_btn = ctk.CTkButton(self.parent_frame_4, text='Load New',
                                          command=self.controller.model.load_new_file)
        self.load_new_btn.configure(**self.configs['button'])
        self.load_new_btn.grid(row=0, column=1, pady=10, sticky='s')

        # A button to write the changes to the output sql file. on_save creates a new file if not
        # already present
        self.save_btn = ctk.CTkButton(self.parent_frame_4, text='Save', command=self.on_save)
        self.save_btn.configure(**self.configs['button'])
        self.save_btn.grid(row=0, column=2, padx=10, pady=10, sticky='se')

    def update_fields(self):
        """
        Upon parsing the selected input sql file, the widgets must display the relevant sql content
        The combobox is set to a list of variable names from the hashmap keys.
        The description textbox state is set to 'normal' to then be deleted and ready to receive new
        text and is then disabled to prevent user changes.
        :return:
        """
        variable_names = list(self.controller.variable_hashmap.keys())

        # Allows the description textbox to be edited. Clears contents of the textbox
        self.description_textbox.configure(state='normal')
        self.description_textbox.delete('1.0', 'end')

        # Set combobox values to the list of hashmap's key values
        self.variable_combobox.configure(values=variable_names)

        # Check if variable_names is not empty
        if variable_names:
            # Set selected combobox value to index 0
            self.variable_combobox.set(variable_names[0])
            # Set variable textbox to the hashmap item's description at selected variable value
            self.variable_textbox.insert(0.0,
                                         text=variable_names[0])
            # Insert the new description and disable it, so it can't be edited
            self.description_textbox.insert('0.0',
                                            text=self.controller.variable_hashmap[
                                                self.variable_combobox.get()]['description'])
            self.description_textbox.configure(state='disabled')
        # If list of variable names is empty, set combobox to a blank string and clear contents of
        # the variable textbox
        else:
            self.variable_combobox.set('')
            self.variable_textbox.delete('1.0',
                                         'end')

    def handle_variable_selection_change(self, event=None):
        """
        When a new selection is made in the combobox, the variable textbox and description textbox
        must be cleared and display the corresponding values from the hashmap.
        :param event:
        :return:
        """
        # Get the selected item from the combobox
        selected_variable = self.variable_combobox.get()
        try:
            # Extract that item's variable and description values
            variable = self.controller.variable_hashmap[selected_variable]['variable']
            description = self.controller.variable_hashmap[selected_variable]['description']
            # Reset and populate the description textbox
            self.description_textbox.configure(state='normal')
            self.description_textbox.delete('1.0', 'end')
            self.description_textbox.insert('0.0', text=description)
            self.description_textbox.configure(state='disabled')

            # Set the variable textbox to the current value of the corresponding hashmap item
            self.variable_textbox.delete('1.0', 'end')
            self.variable_textbox.insert('0.0', text=variable)
        # Catches exceptions where the hashmap at the corresponding item is NoneType/not initialized
        except TypeError as e:
            print(f'Error: {e}')

    def update_variable_callback(self):
        """
        The Apply button's command, which saves the current text from the variable textbox to the
        corresponding 'variable' key of the hashmap, in memory.
        :return:
        """
        try:
            # Get the current text in variable textbox and assign it to the corresponding
            # 'variable' key in the hashmap
            new_value = self.variable_textbox.get('1.0', 'end')
            self.controller.variable_hashmap[self.variable_combobox.get()]['variable'] = new_value
        # FIXME determine expected exceptions and catch them specifically
        except Exception as e:
            print(e)

    def refresh_combobox(self):
        """
        Current behavior is to remove items from the combobox where the 'variable' value has been
        changed. The change has occurred whenever the Apply button is clicked.
        :return:
        """
        # Refreshes combobox to latest details
        try:
            variable_names = list(self.controller.variable_hashmap.keys())
            self.variable_combobox.configure(values=variable_names)
            self.description_textbox.configure(state='normal')
            self.description_textbox.delete('1.0', 'end')
            self.variable_textbox.delete('1.0', 'end')

            # Check if variable_names is not empty
            if variable_names:
                variable_item = self.controller.variable_hashmap[variable_names[0]]
                self.variable_combobox.set(variable_item['variable'])
                self.description_textbox.insert('0.0', text=variable_item['description'])
                self.description_textbox.configure(state='disabled')
            else:
                self.variable_combobox.set('')
        except AttributeError as e:
            print(e)

    def on_save(self):
        """
        Calls the model instance's method to create a new sql file OR save to an existing one
        :return:
        """
        modified_query = self.controller.model.generate_modified_query()
        self.controller.model.save_to_file(modified_query)
        # The combobox is cleared of variables that had changes applied
        self.refresh_combobox()
