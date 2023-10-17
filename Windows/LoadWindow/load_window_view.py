"""
Allows the user to Load a query. The file contains placeholder text and the UI provides the user
with the ability to fill out the placeholders in a clear and clean way
"""

import customtkinter as ctk


class LoadWindow:
    def __init__(self, parent, controller):
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
        self.submit_button = None
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

    def setup_ui(self):

        self.app.minsize(800, 600)

        self.app.grid_columnconfigure(0, weight=1)
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_rowconfigure(1, weight=2)
        self.app.grid_rowconfigure(2, weight=5)

        # Title frame
        self.parent_frame_1 = ctk.CTkFrame(self.app)
        self.parent_frame_1.grid(row=0, column=0, sticky='nsew')
        self.parent_frame_1.columnconfigure(0, weight=1)
        self.parent_frame_1.rowconfigure(0, weight=0)

        # New keyword frame
        self.parent_frame_2 = ctk.CTkFrame(self.app)
        self.parent_frame_2.grid(row=1, column=0, sticky='nsew')
        self.parent_frame_2.columnconfigure(0, weight=0)
        self.parent_frame_2.columnconfigure(1, weight=0)
        self.parent_frame_2.columnconfigure(2, weight=3)
        self.parent_frame_2.rowconfigure(0, weight=0)
        self.parent_frame_2.rowconfigure(1, weight=0)

        # Query preview and buttons frame -- TODO Create a 4th frame to hold the buttons and isolate
        # query preview
        self.parent_frame_3 = ctk.CTkFrame(self.app)
        self.parent_frame_3.grid(row=2, column=0, sticky='nsew')
        self.parent_frame_3.columnconfigure(0, weight=1)
        self.parent_frame_3.columnconfigure(1, weight=1)
        self.parent_frame_3.columnconfigure(2, weight=1)
        self.parent_frame_3.rowconfigure(0, weight=3)
        self.parent_frame_3.rowconfigure(1, weight=1)

        self.parent_frame_4 = ctk.CTkFrame(self.app)
        self.parent_frame_4.grid(row=3, column=0, sticky='nsew')
        self.parent_frame_4.columnconfigure(0, weight=1)
        self.parent_frame_4.columnconfigure(1, weight=1)
        self.parent_frame_4.columnconfigure(2, weight=1)

        # Frame 1's Widgets
        self.window_title = ctk.CTkLabel(self.parent_frame_1, text='Load Query')
        self.window_title.configure(**self.configs['title'])
        self.window_title.grid(row=0, column=0, sticky='nsew')

        # Frame 2's widgets
        self.variable_label = ctk.CTkLabel(self.parent_frame_2, text='Variables')
        self.variable_label.configure(**self.configs['label'])
        self.variable_label.grid(row=0, column=0, padx=(10, 0), sticky='w')

        self.variable_combobox = ctk.CTkComboBox(self.parent_frame_2, values=[''],
                                                 command=self.variable_combobox_2_callback)
        self.variable_combobox.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        self.variable_combobox.set('')

        self.variable_textbox = ctk.CTkTextbox(self.parent_frame_2, height=30)
        self.variable_textbox.configure(**self.configs['text'])
        self.variable_textbox.grid(row=0, column=2, sticky='nsew', padx=10)

        self.submit_button = ctk.CTkButton(self.parent_frame_2, text='Apply', command=self.update_variable_callback)
        self.submit_button.configure(**self.configs['button'])
        self.submit_button.grid(row=0, column=3, sticky='nsew', padx=10)

        self.description_label = ctk.CTkLabel(self.parent_frame_2, text='Description', width=30)
        self.description_label.configure(**self.configs['label'])
        self.description_label.grid(row=1, column=0, sticky='nw', padx=10)

        self.description_textbox = ctk.CTkTextbox(self.parent_frame_2, wrap='word')
        self.description_textbox.configure(**self.configs['text'])
        self.description_textbox.grid(row=1, column=1, columnspan=2, sticky='nsew', pady=10, padx=10)

        # Frame 3 widgets
        self.query_output_textbox = ctk.CTkTextbox(self.parent_frame_3)
        self.query_output_textbox.configure(**self.configs['text'])
        self.query_output_textbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky='nsew')
        self.query_output_textbox.columnconfigure(0, weight=1)
        self.query_output_textbox.rowconfigure(0, weight=1)

        # Frame 4 bottom buttons to cancel, load a new file, and save current mods
        self.cancel_btn = ctk.CTkButton(self.parent_frame_4, text='Cancel', command=self.app.destroy)
        self.cancel_btn.configure(**self.configs['button'])
        self.cancel_btn.grid(row=0, column=0, padx=10, pady=10, sticky='sw')

        self.load_new_btn = ctk.CTkButton(self.parent_frame_4, text='Load New',
                                          command=self.controller.model.load_new_file)
        self.load_new_btn.configure(**self.configs['button'])
        self.load_new_btn.grid(row=0, column=1, pady=10, sticky='s')

        self.save_btn = ctk.CTkButton(self.parent_frame_4, text='Save', command=self.on_save)
        self.save_btn.configure(**self.configs['button'])
        self.save_btn.grid(row=0, column=2, padx=10, pady=10, sticky='se')

    def update_fields(self, data):
        variable_names = list(self.controller.variable_hashmap.keys())

        # Reset description textbox
        self.description_textbox.configure(state='normal')
        self.description_textbox.delete('1.0', 'end')

        # Set combobox values to variable name
        self.variable_combobox.configure(values=variable_names)
        # Set selected combox value to index 0
        self.variable_combobox.set(variable_names[0])

        # Set variable textbox to the currently selected value
        self.variable_textbox.insert(0.0, text=variable_names[0])
        # Insert the new description and disable it, so it can't be edited
        self.description_textbox.insert('0.0',
                                        text=self.controller.variable_hashmap[
                                            self.variable_combobox.get()]['description'])
        self.description_textbox.configure(state='disabled')

    def variable_combobox_2_callback(self, event=None):
        selected_variable = self.variable_combobox.get()
        try:
            variable = self.controller.variable_hashmap[selected_variable]['variable']
            description = self.controller.variable_hashmap[selected_variable]['description']
            # Reset and populate the description textbox
            self.description_textbox.delete('1.0', 'end')
            self.description_textbox.insert('0.0', text=description)
            self.description_textbox.configure(state='disabled')

            self.variable_textbox.delete('1.0', 'end')
            self.variable_textbox.insert('0.0', text=variable)
        except TypeError as e:
            print(f'Error: {e}')

    def update_variable_callback(self):
        try:
            new_value = self.variable_textbox.get('1.0', 'end')
            self.controller.variable_hashmap[self.variable_combobox.get()]['variable'] = new_value
        except Exception as e:
            print(e)

    def refresh_combobox(self):
        # Refreshes combobox to latest details
        try:
            variable_names = list(self.controller.variable_hashmap.keys())
            self.variable_combobox.configure(values=variable_names)
            self.description_textbox.configure(state='normal')
            self.description_textbox.delete('1.0', 'end')
            self.variable_textbox.delete('1.0', 'end')
            if variable_names:
                variable_item = self.controller.variable_hashmap[variable_names[0]]
                self.variable_combobox.set(variable_item['variable'])
                self.description_textbox.insert('0.0', text=variable_item['description'])
                self.description_textbox.configure(state='disabled')
            else:
                self.variable_combobox.set('')
        except AttributeError as e:
            print(e)

    """
    def refresh_combobox(self):
    variable_names = list(self.controller.variable_hashmap.keys())
    self._update_combobox(variable_names)
    self._reset_description_textbox()
    self._populate_textboxes(variable_names)

    def _update_combobox(self, data):
        self.variable_combobox.configure(values=data)
        self.variable_combobox.set(data[0] if variable_names else '')
    
    def _reset_description_textbox(self):
        self.description_textbox.configure(state='normal')
        self.description_textbox.delete('1.0', 'end')
    
    def _populate_textboxes(self, data):
        selected_variable = self.variable_combobox.get()
        variable_item = self.controller.variable_hashmap.get(selected_variable, {})
        
        description = variable_item.get('description', '')
        self.description_textbox.insert('0.0', text=description)
        self.description_textbox.configure(state='disabled')
    
        variable = variable_item.get('variable', '')
        self.variable_textbox.delete('1.0', 'end')
        self.variable_textbox.insert('0.0', text=variable)
    """

    def on_save(self):
        modified_query = self.controller.model.generate_modified_query()
        self.controller.model.save_to_file(modified_query)
        self.refresh_combobox()
