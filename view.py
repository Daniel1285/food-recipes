from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QWidget
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QPixmap

from ui.main_window_ui import Ui_MainWindow
from pages_functions.home import Home
from pages_functions.image_to_recipe import Image_to_recipe
from pages_functions.recipe import RecipePage

import json


class CookbookView(QMainWindow):
    def __init__(self, model):
        super(CookbookView, self).__init__()
        self.model = model
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("static/icons/IconApp.ico"))
        self.setWindowTitle("Cookbook")
        self.image_to_recipe_instance = Image_to_recipe()

        self.home_btn = self.ui.homeButton
        self.imagga_btn = self.ui.imaggaButton

        self.menu_btn_dict = {
            self.home_btn: Home(),
            self.imagga_btn: self.image_to_recipe_instance
        }

        self.show_home_page()

        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.ui.search_btn.clicked.connect(self.add_btn_to_recipes_page)
        self.home_btn.clicked.connect(self.show_selected_page)
        self.imagga_btn.clicked.connect(self.show_selected_page)
        self.connect_recipe_signal(self.image_to_recipe_instance)

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


    def connect_recipe_signal(self, image_to_recipe_instance):
        # Connect the signal from Image_to_recipe to a slot in CookbookView
        image_to_recipe_instance.recipeSelected.connect(self.add_btn_to_recipes_page)

    @Slot(str)
    def add_btn_to_recipes_page(self, name=None):
        """
        Add a button for a new cookbook to the recipes page.
        """
        if name:
            cookbook_name = name
        else:
            cookbook_name = self.ui.lineEdit.text()

        if cookbook_name:
            # recipe_data = self.model.request_EdamamApi(cookbook_name)
            recipe_data = self.model.get_recipe(cookbook_name)
            if recipe_data:
                #recipe_data = self.load_data("recipes.json")
                new_page = RecipePage(recipe_data)
                # Add the new tab to the tab widget
                cur_index = self.ui.tabWidget.addTab(new_page, cookbook_name)
                self.ui.tabWidget.setCurrentIndex(cur_index)
                self.ui.tabWidget.setVisible(True)

                # Create a horizontal layout to hold the button and delete icon
                layout = QHBoxLayout()
                # Create the button for the new tab
                button = QPushButton(cookbook_name)
                layout.addWidget(button)
                # Create the delete icon
                delete_icon = QLabel()
                self.set_icon(delete_icon, "static/icons/trash-2.svg")  # Set the default icon
                self.setup_hover_effects(delete_icon)  # Setup hover effects
                layout.addWidget(delete_icon)

                # Create a wrapper widget to hold the layout
                wrapper_widget = QWidget()
                wrapper_widget.setLayout(layout)

                # Insert the wrapper widget into the vertical layout
                self.ui.verticalLayout_2.insertWidget(0, wrapper_widget)

                # Connect button click signal to show_selected_page slot
                button.clicked.connect(self.show_selected_page)

                # Connect delete icon click signal to delete_button_and_tab slot
                delete_icon.mousePressEvent = lambda event: self.delete_button_and_tab(wrapper_widget, cur_index, cookbook_name)
        self.ui.lineEdit.clear()


    def delete_button_and_tab(self, wrapper_widget, tab_index, cookbook_name):
        """Delete the button, associated tab, and related data."""

        self.model.delete_by_cookbookName(cookbook_name)
        self.ui.verticalLayout_2.removeWidget(wrapper_widget)
        wrapper_widget.deleteLater()
        self.ui.tabWidget.removeTab(tab_index)

    def set_icon(self, label, icon_path):
        """Set the icon for a label."""

        pixmap = QPixmap(icon_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setFixedSize(16, 16)

    def change_icon_on_hover(self, label, is_hovering):
        """Change the delete icon when hovering over it."""

        if is_hovering:
            self.set_icon(label,"static/icons/trash-2-red.svg")
        else:
            self.set_icon(label,"static/icons/trash-2.svg")


    def setup_hover_effects(self, label):
        """Setup hover effects for a label."""

        label.setMouseTracking(True)
        label.enterEvent = lambda event: self.change_icon_on_hover(label, True)
        label.leaveEvent = lambda event: self.change_icon_on_hover(label, False)
