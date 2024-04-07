from PySide6.QtWidgets import QWidget
from ui.pages.about_ui import Ui_Form

class About(QWidget):
    def __init__(self):
        super(About, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)