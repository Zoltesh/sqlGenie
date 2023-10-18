"""
load_window logic
"""

from Windows.LoadWindow.load_window_model import LoadWindowModel
from Windows.LoadWindow.load_window_view import LoadWindow


class LoadWindowController:
    """
    The Controller acts as the liaison between the Model and View. The Model and View do not
    need to interact with each other.
    """
    def __init__(self, parent):
        """
        The LoadWindowController is initialized with a parent window. In this case, the parent is
        the MainWindow
        :param parent:
        """
        # To prevent errors when attempting to access keys on a NoneType object, variable_hashmap
        # must be initialized to an empty dictionary
        self.variable_hashmap = {}
        # The callback causes the Controller's populate_fields method to run within the model's
        # instance at the time of initialization
        self.model = LoadWindowModel(on_file_loaded_callback=self.populate_fields)
        self.view = LoadWindow(parent, self)

    def populate_fields(self):
        """
        As the model object initializes and parses a selected sql file, the Controller obtains
        a copy of the variable_hashmap
        :return:
        """
        self.variable_hashmap = self.model.get_variable_hashmap()
        self.view.update_fields()


def show_load_window(parent):
    """
    Using the caller window as a parent, overlay the LoadWindow
    :param parent:
    :return:
    """
    controller = LoadWindowController(parent)
    parent.wait_window(controller.view.app)
