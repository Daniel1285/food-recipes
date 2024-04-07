from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox , QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout
from ui.main_window_ui import Ui_MainWindow
from pages_functions.home import Home
from pages_functions.about import About


class CookbookView(QMainWindow):
        def __init__(self, model):
            super(CookbookView, self).__init__()
            self.model = model
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowTitle("Cookbook")

            ##=======================================================================================================
            ## Get all object in window
            ##=======================================================================================================
            self.home_btn = self.ui.homeButton



            ##=======================================================================================================
            ## setup 
            ##=======================================================================================================
            self.menu_btn_dict = {
                self.home_btn: Home(),
            }

            ##=======================================================================================================
            ## Show home page when stat app
            ##=======================================================================================================
            self.show_home_page()

            ##=======================================================================================================
            ## Connect signal and slot
            ##=======================================================================================================
            self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)

            self.home_btn.clicked.connect(self.show_selected_page)

        
        def show_home_page(self):

            result = self.open_tab_flag(self.home_btn.text())
            self.set_btn_checked(self.home_btn)

            if result[0]:
                self.ui.tabWidget.setCurrentIndex(result[1])
            else:
                tab_title = self.home_btn.text()
                curIndex = self.ui.tabWidget.addTab(Home(), tab_title)
                self.ui.tabWidget.setCurrentIndex(curIndex)
                self.ui.tabWidget.setVisible(True)

        def show_selected_page(self):
            """
            Function for showing selected window
            :return:
            """
            button = self.sender()

            result = self.open_tab_flag(button.text())
            self.set_btn_checked(button)

            if result[0]:
                self.ui.tabWidget.setCurrentIndex(result[1])
            else:
                title = button.text()
                curIndex = self.ui.tabWidget.addTab(self.menu_btn_dict[button], title)
                self.ui.tabWidget.setCurrentIndex(curIndex)
                self.ui.tabWidget.setVisible(True)


        def close_tab(self, index):
            self.ui.tabWidget.removeTab(index)
            if self.ui.tabWidget.count() == 0:
                self.ui.toolBox.setCurrentIndex(0)
                self.show_home_page()

        def open_tab_flag(self, tab):
            """
            Check if selected window showed or not
            :param tab: tab title
            :return: bool and index
            """
            open_tab_count = self.ui.tabWidget.count()

            for i in range(open_tab_count):
                tab_name = self.ui.tabWidget.tabText(i)
                if tab_name == tab:
                    return True, i
                else:
                    continue

            return False,

        def set_btn_checked(self, btn):

            for button in self.menu_btn_dict.keys():
                if button != btn:
                    button.setChecked(False)
                else:
                    button.setChecked(True)