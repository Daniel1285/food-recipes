from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox , QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QFrame, QScrollArea, QHBoxLayout
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)

import model
from ui.main_window_ui import Ui_MainWindow
from pages_functions.home import Home
from pages_functions.about import About
from pages_functions.recipe import RecipePage
from ui.pages.recipe_ui import RecipeWidget
import json
import asyncio
class CookbookView(QMainWindow):
        def __init__(self, model):
            super(CookbookView, self).__init__()
            self.model = model
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.setWindowTitle("Cookbook")


            self.home_btn = self.ui.homeButton

            self.menu_btn_dict = {
                self.home_btn: Home(),
            }

            self.show_home_page()

            self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
            self.ui.search_btn.clicked.connect(self.add_btn_to_recipes_page)
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

        def load_data(self, json_file):
            with open(json_file, 'r', encoding='utf-8') as f:
                return json.load(f)


        async def get_data(self, data):
            recipe_data = await model.Recipe().get_recipe(data)
            return  recipe_data

        def add_btn_to_recipes_page(self):

            cookbook_name = self.ui.lineEdit.text()
            recipe_dat = self.load_data("recipes.json")
            print(f"recipe json\n{recipe_dat}")
            recipe_data = model.Recipe().get_recipe(cookbook_name)
            print(recipe_data)
            new_page = RecipePage(recipe_data)
            # Add the new tab to the tab widget
            cur_index = self.ui.tabWidget.addTab(new_page, cookbook_name)
            self.ui.tabWidget.setCurrentIndex(cur_index)
            self.ui.tabWidget.setVisible(True)

            # Create a button for the new tab
            button = QPushButton(cookbook_name)
            # Insert the button into the layout
            self.ui.verticalLayout_2.insertWidget(0, button)
            self.ui.lineEdit.clear()
            button.clicked.connect(self.show_selected_page)


