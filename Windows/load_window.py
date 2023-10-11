"""
Allows the user to Load a query. The file contains placeholder text and the UI provides the user
with the ability to fill out the placeholders in a clear and clean way
"""
import tkinter

import customtkinter as ctk
from tkinter import filedialog


def load_new_file():
    # Check if changes made to currently loaded file
    # If no changes, begin dialogue to load new file
    # If changes made to currently loaded file, dialogue to save changes
    # After save or no save, dialogue to open new file
    query_file = filedialog.askopenfile()
    print(query_file)


def save_to_file():
    # Select file to save to
    # Make sure loaded file is same file being written to
    pass


def populate_fields():
    # Insert data from loaded query into vars and description
    # Selected var ON SELECT should display partial line where value resides, with the value being
    # highlighted or otherwise stand out
    pass


class LoadWindow:
    def __init__(self, parent):
        # Parent Frames
        self.parent_frame_1 = None
        self.parent_frame_2 = None
        self.parent_frame_3 = None

        # Frame 1 widgets
        self.window_title_1 = None

        # Frame 2 children
        self.child_frame_2_1 = None
        self.child_frame_2_2 = None
        self.child_frame_2_3 = None
        self.child_frame_2_4 = None

        # Frame 2 child 1 widgets
        self.placeholder_label_2 = None
        self.placeholder_combobox_2 = None
        self.placeholder_textbox_2 = None

        # Frame 2 child 2 widgets
        self.placeholder_textbox_2 = None

        # Frame 2 child 3 widgets
        self.description_label_2 = None

        # Frame 2 child 4 widgets
        self.description_textbox_2 = None

        # Frame 3 children
        self.child_frame_3_1 = None
        self.child_frame_3_2 = None

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
        self.placeholder_value = None
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

        # Create frames for each column
        self.parent_frame_1 = ctk.CTkFrame(self.app)
        self.parent_frame_1.grid(row=0, column=0, sticky='nsew')
        self.parent_frame_1.columnconfigure(0, weight=1)
        self.parent_frame_1.rowconfigure(0, weight=0)

        self.parent_frame_2 = ctk.CTkFrame(self.app)
        self.parent_frame_2.grid(row=1, column=0, sticky='nsew')
        self.parent_frame_2.columnconfigure(0, weight=0)
        self.parent_frame_2.columnconfigure(1, weight=0)
        self.parent_frame_2.columnconfigure(2, weight=3)
        self.parent_frame_2.rowconfigure(0, weight=0)
        self.parent_frame_2.rowconfigure(1, weight=0)

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
        self.placeholder_label_2 = ctk.CTkLabel(self.parent_frame_2, text='Variables', font=self.label_font,
                                                width=30)
        self.placeholder_label_2.grid(row=0, column=0, padx=(10, 0), sticky='w')

        self.placeholder_combobox_2 = ctk.CTkComboBox(self.parent_frame_2, values=['1', '2'])
        self.placeholder_combobox_2.grid(row=0, column=1, sticky='nsew', padx=(10, 0))

        self.placeholder_textbox_2 = ctk.CTkTextbox(self.parent_frame_2, font=self.text_font, height=30)
        self.placeholder_textbox_2.grid(row=0, column=2, sticky='nsew', padx=10)

        self.description_label_2 = ctk.CTkLabel(self.parent_frame_2, text='Description', font=self.label_font,
                                                width=30)
        self.description_label_2.grid(row=1, column=0, sticky='nw', padx=10)

        self.description_textbox_2 = ctk.CTkTextbox(self.parent_frame_2, font=self.text_font)
        self.description_textbox_2.grid(row=1, column=1, columnspan=2, sticky='nsew', pady=10, padx=10)

        """# Frame 2 child 1 widgets
        self.child_frame_2_1 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_1.grid(row=0, column=0, sticky='nsew')

        self.placeholder_label_2_1 = ctk.CTkLabel(self.child_frame_2_1, text='Variables', font=self.label_font,
                                                  height=30, width=30)
        self.placeholder_label_2_1.grid(row=0, column=0, padx=(10, 0), sticky='nsew')

        self.placeholder_combobox_2_1 = ctk.CTkComboBox(self.child_frame_2_1, values=['1', '2'], height=30)
        self.placeholder_combobox_2_1.grid(row=0, column=1, sticky='nsew', padx=(10, 0))

        # Frame 2 child 2 widgets
        self.child_frame_2_2 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_2.grid(row=0, column=1, sticky='nsew')
        self.child_frame_2_2.columnconfigure(0, weight=1)

        self.placeholder_textbox_2_2 = ctk.CTkTextbox(self.child_frame_2_2, font=self.text_font, height=30)
        self.placeholder_textbox_2_2.grid(row=0, column=0, sticky='nsew', padx=10)

        # Frame 2 child 3 widgets
        self.child_frame_2_3 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_3.grid(row=1, column=0, sticky='nsew')
        self.child_frame_2_3.columnconfigure(0, weight=0)
        self.child_frame_2_3.columnconfigure(1, weight=1)

        self.description_label_2_3 = ctk.CTkLabel(self.child_frame_2_3, text='Description', font=self.label_font,
                                                  height=30, width=30)
        self.description_label_2_3.grid(row=0, column=0, sticky='nsew', padx=10)

        # Frame 2 child 4 widgets
        self.child_frame_2_4 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_4.grid(row=1, column=1, sticky='nsew')
        self.child_frame_2_4.columnconfigure(0, weight=1)
        self.description_textbox_2_4 = ctk.CTkTextbox(self.child_frame_2_4, font=self.text_font)
        self.description_textbox_2_4.grid(row=0, column=0, sticky='nsew', pady=10, padx=10)"""

        # Frame 3 widgets
        self.query_output_textbox_3 = ctk.CTkTextbox(self.parent_frame_3, font=self.text_font)
        self.query_output_textbox_3.grid(row=0, column=0, columnspan=3, padx=10, sticky='nsew')
        self.query_output_textbox_3.columnconfigure(0, weight=1)
        self.query_output_textbox_3.rowconfigure(0, weight=1)

        self.cancel_btn_3 = ctk.CTkButton(self.parent_frame_3, text='Cancel', font=self.button_font, width=40,
                                          command=self.app.destroy)
        self.cancel_btn_3.grid(row=1, column=0, padx=10, pady=10, sticky='sw')

        self.load_new_btn_3 = ctk.CTkButton(self.parent_frame_3, text='Load New', font=self.button_font, width=40)
        self.load_new_btn_3.grid(row=1, column=1, pady=10, sticky='s')

        self.save_btn_3 = ctk.CTkButton(self.parent_frame_3, text='Save', font=self.button_font, width=40)
        self.save_btn_3.grid(row=1, column=2, padx=10, pady=10, sticky='se')


def show_load_window(parent):
    load_win = LoadWindow(parent)
    parent.wait_window(load_win.app)
