"""
load_window logic
"""

from Windows.LoadWindow.load_window_model import LoadWindowModel
from Windows.LoadWindow.load_window_view import LoadWindow


class LoadWindowController:
    def __init__(self, parent):
        self.model = LoadWindowModel()
        self.view = LoadWindow(parent, self)

    def populate_fields(self):
        # Insert data from loaded query into vars and description
        # Selected var ON SELECT should display partial line where value resides, with the value being
        # highlighted or otherwise stand out
        data = self.model.VAR_LIST
        self.view.update_fields(data)


def show_load_window(parent):
    controller = LoadWindowController(parent)
    parent.wait_window(controller.view.app)
