"""
load_window logic
"""

from Windows.LoadWindow.load_window_model import LoadWindowModel
from Windows.LoadWindow.load_window_view import LoadWindow


class LoadWindowController:
    def __init__(self, parent):
        self.variable_hashmap = None
        self.model = LoadWindowModel(on_file_loaded_callback=self.populate_fields)
        self.view = LoadWindow(parent, self)

    def populate_fields(self):
        # TODO Make this actually populate the fields in the view
        data = self.model.VAR_LIST
        self.view.update_fields(data)
        self.variable_hashmap = self.model.get_variable_hashmap()


def show_load_window(parent):
    controller = LoadWindowController(parent)
    parent.wait_window(controller.view.app)
