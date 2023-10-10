import customtkinter as ctk
from Windows import login_window, load_window


class MainWindow:
    def __init__(self):
        self.load_btn = None
        self.login_btn = None
        self.create_btn = None
        self.quit_btn = None
        self.root = ctk.CTk()
        self.setup_ui()
        self.root.mainloop()

    def setup_ui(self):
        self.login_btn = ctk.CTkButton(self.root, text="Login", command=self.launch_login)
        self.root.title('Main Window')
        self.root.geometry('600x600')

        self.login_btn = ctk.CTkButton(self.root, text="Login", command=self.launch_login)
        self.login_btn.pack(pady=20)

        self.load_btn = ctk.CTkButton(self.root, text="Load", command=self.launch_load)
        self.load_btn.pack(pady=20)

        self.create_btn = ctk.CTkButton(self.root, text="Create")
        self.create_btn.pack(pady=20)

        self.quit_btn = ctk.CTkButton(self.root, text="Quit", command=self.root.destroy)
        self.quit_btn.pack(pady=20)

    def launch_login(self):
        login_window.show_login_window(self.root)

    def launch_load(self):
        load_window.show_load_window(self.root)


if __name__ == "__main__":
    MainWindow()
