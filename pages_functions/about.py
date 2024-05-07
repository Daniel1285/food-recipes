from PySide6.QtWidgets import QWidget
from ui.pages.about_ui import Ui_Form

class About(QWidget):
    """
    Class representing the About page of the application.

    Attributes:
        ui (Ui_Form): Instance of the user interface class for About page.
    """

    def __init__(self):
        """
        Initialize the About page.
        """
        super(About, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
