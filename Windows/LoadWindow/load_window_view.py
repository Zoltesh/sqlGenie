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

        # Frame 1 widgets
        self.window_title_1 = None

        # Frame 2 widgets
        self.variable_label_2 = None
        self.variable_combobox_2 = None
        self.variable_textbox_2 = None
        self.submit_button_2 = None
        self.description_label_2 = None
        self.description_textbox_2 = None

        # Frame 3 widgets
        self.query_output_textbox_3 = None
        self.save_btn_3 = None
        self.load_new_btn_3 = None
        self.cancel_btn_3 = None

        self.filled_value_combobox = None
        self.button_font = None
        self.text_font = None
        self.label_font = None
        self.title_font = None
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
        self.title_font = ('Arial', 22, 'bold')
        self.label_font = ('Arial', 16)
        self.text_font = ('Arial', 14)
        self.button_font = ('Arial', 18)
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

        # Frame 1's Widgets
        self.window_title_1 = ctk.CTkLabel(self.parent_frame_1, text='Load Query', font=self.title_font)
        self.window_title_1.grid(row=0, column=0, sticky='nsew')

        # Frame 2's widgets
        self.variable_label_2 = ctk.CTkLabel(self.parent_frame_2, text='Variables', font=self.label_font,
                                             width=30)
        self.variable_label_2.grid(row=0, column=0, padx=(10, 0), sticky='w')

        self.variable_combobox_2 = ctk.CTkComboBox(self.parent_frame_2, values=[''],
                                                   command=self.variable_combobox_2_callback)
        self.variable_combobox_2.grid(row=0, column=1, sticky='nsew', padx=(10, 0))
        self.variable_combobox_2.set('')

        self.variable_textbox_2 = ctk.CTkTextbox(self.parent_frame_2, font=self.text_font, height=30)
        self.variable_textbox_2.grid(row=0, column=2, sticky='nsew', padx=10)

        self.submit_button_2 = ctk.CTkButton(self.parent_frame_2, text='Update', font=self.button_font, width=40,
                                             command=self.update_variable_callback)
        self.submit_button_2.grid(row=0, column=3, sticky='nsew', padx=10)

        self.description_label_2 = ctk.CTkLabel(self.parent_frame_2, text='Description', font=self.label_font,
                                                width=30)
        self.description_label_2.grid(row=1, column=0, sticky='nw', padx=10)

        self.description_textbox_2 = ctk.CTkTextbox(self.parent_frame_2, font=self.text_font, wrap='word')
        self.description_textbox_2.grid(row=1, column=1, columnspan=2, sticky='nsew', pady=10, padx=10)

        # Frame 3 widgets
        self.query_output_textbox_3 = ctk.CTkTextbox(self.parent_frame_3, font=self.text_font)
        self.query_output_textbox_3.grid(row=0, column=0, columnspan=3, padx=10, sticky='nsew')
        self.query_output_textbox_3.columnconfigure(0, weight=1)
        self.query_output_textbox_3.rowconfigure(0, weight=1)

        self.cancel_btn_3 = ctk.CTkButton(self.parent_frame_3, text='Cancel', font=self.button_font, width=40,
                                          command=self.app.destroy)
        self.cancel_btn_3.grid(row=1, column=0, padx=10, pady=10, sticky='sw')

        self.load_new_btn_3 = ctk.CTkButton(self.parent_frame_3, text='Load New', font=self.button_font, width=40,
                                            command=self.controller.model.load_new_file)
        self.load_new_btn_3.grid(row=1, column=1, pady=10, sticky='s')

        self.save_btn_3 = ctk.CTkButton(self.parent_frame_3, text='Save', font=self.button_font, width=40,
                                        command=self.on_save)
        self.save_btn_3.grid(row=1, column=2, padx=10, pady=10, sticky='se')

    def update_fields(self, data):
        variable_names = list(self.controller.variable_hashmap.keys())

        # Reset description textbox
        self.description_textbox_2.configure(state='normal')
        self.description_textbox_2.delete('1.0', 'end')

        # Set combobox values to variable name
        self.variable_combobox_2.configure(values=variable_names)
        # Set selected combox value to index 0
        self.variable_combobox_2.set(variable_names[0])

        # Set variable textbox to the currently selected value
        self.variable_textbox_2.insert(0.0, text=variable_names[0])
        # Insert the new description and disable it, so it can't be edited
        self.description_textbox_2.insert('0.0',
                                          text=self.controller.variable_hashmap[
                                              self.variable_combobox_2.get()]['description'])
        self.description_textbox_2.configure(state='disabled')

    def variable_combobox_2_callback(self, event=None):
        selected_variable = self.variable_combobox_2.get()
        try:
            variable = self.controller.variable_hashmap[selected_variable]['variable']
            description = self.controller.variable_hashmap[selected_variable]['description']
            # Reset and populate the description textbox
            self.description_textbox_2.delete('1.0', 'end')
            self.description_textbox_2.insert('0.0', text=description)
            self.description_textbox_2.configure(state='disabled')

            self.variable_textbox_2.delete('1.0', 'end')
            self.variable_textbox_2.insert('0.0', text=variable)
        except TypeError as e:
            print(f'Error: {e}')

    def update_variable_callback(self):
        try:
            new_value = self.variable_textbox_2.get('1.0', 'end')
            self.controller.variable_hashmap[self.variable_combobox_2.get()]['variable'] = new_value
        except Exception as e:
            print(e)

    def refresh_combobox(self):
        """ Refreshes the combobox with the latest variables. """
        variable_names = list(self.controller.variable_hashmap.keys())
        self.variable_combobox_2.configure(values=variable_names)
        self.description_textbox_2.configure(state='normal')
        self.description_textbox_2.delete('1.0', 'end')
        self.variable_textbox_2.delete('1.0', 'end')
        if variable_names:
            variable_item = self.controller.variable_hashmap[variable_names[0]]
            self.variable_combobox_2.set(variable_item['variable'])
            self.description_textbox_2.insert('0.0', text=variable_item['description'])
            self.description_textbox_2.configure(state='disabled')
        else:
            self.variable_combobox_2.set('')

    def on_save(self):
        modified_query = self.controller.model.generate_modified_query()
        self.controller.model.save_to_file(modified_query)
        self.refresh_combobox()
