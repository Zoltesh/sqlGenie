"""
Allows the user to Load a query. The file contains placeholder text and the UI provides the user
with the ability to fill out the placeholders in a clear and clean way
"""
import tkinter

import customtkinter as ctk
from tkinter import filedialog


def load_file():
    query_file = filedialog.askopenfile()
    print(query_file)


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

        # Frame 2 child 1 widgets
        self.placeholder_label_2_1 = None
        self.placeholder_combobox_2_1 = None
        self.placeholder_textbox_2_1 = None

        # Frame 2 child 2 widgets
        self.placeholder_textbox_2_2 = None

        # Frame 2 child 3 widgets
        self.description_label_2_3 = None
        self.description_textbox_2_3 = None

        # Frame 3 children
        self.child_frame_3_1 = None
        self.child_frame_3_2 = None

        # Frame 3 widgets
        self.save_btn_3_2 = None
        self.cancel_btn_3_1 = None

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
        self.app.grid_rowconfigure(1, weight=5)
        self.app.grid_rowconfigure(2, weight=1)

        # Create frames for each column
        self.parent_frame_1 = ctk.CTkFrame(self.app)
        self.parent_frame_1.grid(row=0, column=0, sticky='nsew')
        self.parent_frame_1.columnconfigure(0, weight=1)

        self.parent_frame_2 = ctk.CTkFrame(self.app)
        self.parent_frame_2.grid(row=1, column=0, sticky='nsew')
        self.parent_frame_2.columnconfigure(0, weight=0)
        self.parent_frame_2.columnconfigure(1, weight=3)

        self.parent_frame_3 = ctk.CTkFrame(self.app)
        self.parent_frame_3.grid(row=2, column=0, sticky='nsew')
        self.parent_frame_3.columnconfigure(0, weight=1)
        self.parent_frame_3.columnconfigure(1, weight=1)

        # Frame 1's Widgets
        self.window_title_1 = ctk.CTkLabel(self.parent_frame_1, text='Load Query', font=self.title_font)
        self.window_title_1.grid(row=0, column=0, sticky='nsew')

        # Frame 2 child 1 widgets
        self.child_frame_2_1 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_1.grid(row=0, column=0, sticky='nsew')

        self.placeholder_label_2_1 = ctk.CTkLabel(self.child_frame_2_1, text='Variables', font=self.label_font,
                                                  height=30, width=30)
        self.placeholder_label_2_1.grid(row=0, column=0, padx=20, sticky='w')

        self.placeholder_combobox_2_1 = ctk.CTkComboBox(self.child_frame_2_1, values=['1', '2'], height=30)
        self.placeholder_combobox_2_1.grid(row=0, column=1, sticky='nsew')

        # Frame 2 child 2 widgets
        self.child_frame_2_2 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_2.grid(row=0, column=1, sticky='nsew')
        self.child_frame_2_2.columnconfigure(0, weight=1)

        self.placeholder_textbox_2_2 = ctk.CTkTextbox(self.child_frame_2_2, font=self.text_font, height=30)
        self.placeholder_textbox_2_2.grid(row=0, column=0, sticky='ew')

        # Frame 2 child 3 widgets
        self.child_frame_2_3 = ctk.CTkFrame(self.parent_frame_2)
        self.child_frame_2_3.grid(row=1, column=0, sticky='nsew')

        self.description_label_2_3 = ctk.CTkLabel(self.child_frame_2_3, text='Description', font=self.label_font,
                                                  height=30, width=30)
        self.description_label_2_3.grid(row=0, column=0, sticky='nw', padx=20)

        self.description_textbox_2_3 = ctk.CTkTextbox(self.child_frame_2_3, font=self.text_font)
        self.description_textbox_2_3.grid(row=0, column=1, sticky='nsew', pady=10)

        # Frame 3 child 1 widgets
        self.child_frame_3_1 = ctk.CTkFrame(self.parent_frame_3)
        self.child_frame_3_1.grid(row=0, column=0, sticky='nsew')
        self.child_frame_3_1.columnconfigure(0, weight=1)
        self.child_frame_3_1.rowconfigure(0, weight=1)

        self.cancel_btn_3_1 = ctk.CTkButton(self.child_frame_3_1, text='Cancel', font=self.button_font, width=40,
                                            command=self.app.destroy)
        self.cancel_btn_3_1.grid(row=1, column=0, padx=50, sticky='w')

        # Frame 3 child 2 widgets
        self.child_frame_3_2 = ctk.CTkFrame(self.parent_frame_3)
        self.child_frame_3_2.grid(row=0, column=1, sticky='nsew')
        self.child_frame_3_2.columnconfigure(0, weight=1)

        self.save_btn_3_2 = ctk.CTkButton(self.child_frame_3_2, text='Save', font=self.button_font, width=40)
        self.save_btn_3_2.grid(row=1, column=0, padx=50, sticky='e')
        self.child_frame_3_2.rowconfigure(0, weight=1)


def show_load_window(parent):
    load_win = LoadWindow(parent)
    parent.wait_window(load_win.app)
