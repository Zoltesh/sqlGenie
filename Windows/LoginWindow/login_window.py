"""
Facilitate connection to database. Currently only connects and prints out Success or Fail.
Later code it to provide interaction with the database.
"""

import threading
import customtkinter as ctk
import pyodbc


class LoginWindow:
    """
    Establish a connection to a Microsoft SQL database
    """
    def __init__(self, parent):
        """
        Initialize the window design
        :param parent:
        """
        self.app = ctk.CTkToplevel(parent)
        self.app.grab_set()
        self.app.geometry('600x600')
        self.app.configure(bg='#2a3439')
        self.app.title('Login')

        self.setup_ui()

    def setup_ui(self):
        """
        Setup of the widgets and design
        :return:
        """
        self.server_label = ctk.CTkLabel(self.app, text='Server IP:')
        self.server_label.pack(pady=10)
        self.server_entry = ctk.CTkEntry(self.app)
        self.server_entry.pack(pady=10)
        self.server_entry.configure(fg_color='white', text_color='black')

        self.database_label = ctk.CTkLabel(self.app, text='Database:')
        self.database_label.pack(pady=10)
        self.database_entry = ctk.CTkEntry(self.app)
        self.database_entry.pack(pady=10)
        self.database_entry.configure(fg_color='white', text_color='black')

        self.username_label = ctk.CTkLabel(self.app, text='Username:')
        self.username_label.pack(pady=10)
        self.username_entry = ctk.CTkEntry(self.app)
        self.username_entry.pack(pady=10)
        self.username_entry.configure(fg_color='white', text_color='black')

        # Password Entry
        self.password_label = ctk.CTkLabel(self.app, text="Password:")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self.app, show="*")
        self.password_entry.pack(pady=10)
        self.password_entry.configure(fg_color='white', text_color='black')

        self.login_button = ctk.CTkButton(self.app, text="Login", command=self.attempt_login)
        self.login_button.pack(pady=20)

        self.status_label = ctk.CTkLabel(self.app, text="")
        self.status_label.pack(pady=20)

    def attempt_login(self):
        """
        Test the login with the credentials provided by the user
        :return:
        """
        def threaded_attempt():
            """
            Using format provided by pyodbc
            :return:
            """
            server = self.server_entry.get()
            database = self.database_entry.get()
            username = self.username_entry.get()
            password = self.password_entry.get()

            connection_string = (f"DRIVER={{ODBC Driver 18 for SQL Server}};"
                                 f"SERVER={server};"
                                 f"DATABASE={database};"
                                 f"UID={username};"
                                 f"PWD={password};"
                                 f"TrustServerCertificate=yes;"
                                 )

            try:
                conn = pyodbc.connect(connection_string)
                self.status_label.configure(text="Success", fg_color="green")
                conn.close()
            except Exception as e:
                self.status_label.configure(text="Fail", fg_color="red")
                print(e)

        # Start the threaded login attempt
        threading.Thread(target=threaded_attempt).start()


def show_login_window(parent):
    """
    Show the login window
    :param parent:
    :return:
    """
    login_win = LoginWindow(parent)
    parent.wait_window(login_win.app)
