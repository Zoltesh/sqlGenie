"""
Load and Create sql templates to make reusing queries easier. Specifically designed to allow
easy placeholder replacement for queries that run multiple times with different sql objects
"""
import customtkinter as ctk
from Windows.LoadWindow import load_window_controller
from Windows.LoginWindow import login_window


class MainWindow:
    """
    One window to rule them all. Basic menu options to launch additional windows
    """
    def __init__(self):
        self.load_btn = None
        self.login_btn = None
        self.create_btn = None
        self.quit_btn = None
        self.root = ctk.CTk()
        self.setup_ui()
        self.root.mainloop()

    def setup_ui(self):
        """
        Build the main window and place widgets on it
        :return:
        """
        self.login_btn = ctk.CTkButton(self.root, text="Login", command=self.launch_login)
        self.root.title('Main Window')
        self.root.geometry('600x600')

        self.login_btn = ctk.CTkButton(self.root, text="Login", command=self.launch_login)
        self.login_btn.grid(row=0, column=0, pady=20)

        self.load_btn = ctk.CTkButton(self.root, text="Load", command=self.launch_load)
        self.load_btn.grid(row=1, column=0, pady=20)

        self.create_btn = ctk.CTkButton(self.root, text="Create")
        self.create_btn.grid(row=2, column=0, pady=20)

        self.quit_btn = ctk.CTkButton(self.root, text="Quit", command=self.root.destroy)
        self.quit_btn.grid(row=3, column=0, pady=20)

    def launch_login(self):
        """
        Simple method to instantiate and display the login window
        :return:
        """
        login_window.show_login_window(self.root)

    def launch_load(self):
        """
        Simple method to instantiate and display the load window
        :return:
        """
        load_window_controller.show_load_window(self.root)


if __name__ == "__main__":
    MainWindow()
