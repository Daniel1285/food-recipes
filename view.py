from PySide6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QLabel, QWidget, QLineEdit,  QInputDialog
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtCore import Qt

from ui.main_window_ui import Ui_MainWindow
from ui.widgets.title_bar import CustomTitleBar

from pages_functions.home import Home
from pages_functions.imagetorecipe import ImageToRecipe
from pages_functions.recipe import RecipeTab

import json

class CookbookView(QMainWindow):
    """
    Main window class for the Cookbook application.
    """

    def __init__(self, model):
        """
        Initialize the CookbookView class.

        Args:
            model: The model associated with the view.
        """
        super(CookbookView, self).__init__()
        self.model = model
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("static/icons/IconApp.ico"))
        self.setWindowTitle("Cookbook")

        # Set the window flag to enable customization of the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.custom_title_bar = CustomTitleBar(self)
        self.setMenuWidget(self.custom_title_bar)

        self.image_to_recipe_instance = ImageToRecipe()
        self.recipes_page = self.ui.recipes_page
        self.home_btn = self.ui.homeButton
        self.image_to_recipe_btn = self.ui.imagtToRecipeButton

        self.menu_btn_dict = {
            self.home_btn: Home(),
            self.image_to_recipe_btn: self.image_to_recipe_instance
        }

        self.show_home_page()

        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.ui.search_btn.clicked.connect(self.search_action)
        self.home_btn.clicked.connect(self.show_selected_page)
        self.image_to_recipe_btn.clicked.connect(self.show_selected_page)
        self.connect_recipe_signal(self.image_to_recipe_instance)

    def show_home_page(self):
        """ Opens the home page by default. """

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
        image_to_recipe_instance.recipeSelected.connect(self.search_action)

    @Slot(str)
    def search_action(self, name=None):
        """
        Perform search action.

        Args:
            name (str, optional): The name of the cookbook to search for. Defaults to None.

        Description:
            - If a name is provided (from imageTo_Recipe), use it as the cookbook name.
            - If not, get the name from the line edit field.
            - Retrieve recipe data for the cookbook name.
            - If not found, retrieve data from Edamam API.
            - Create a new tab with the recipe data.
            - Add buttons for the new tab:
                - Button for the cookbook name.
                - Edit icon.
                - Delete icon.
            - Connect signals for button clicks and icon interactions.

        Returns:
            None
        """
        if name:
            cookbook_name = name
            print(cookbook_name)
        else:
            cookbook_name = self.ui.lineEdit.text()

        if cookbook_name:

            recipe_data = self.model.get_recipe(cookbook_name)
            if recipe_data == []:  # Not Found
                print(recipe_data)
                recipe_data = self.model.request_EdamamApi(cookbook_name)

            if recipe_data:

                new_page = RecipeTab(recipe_data)

                # Add the new tab to the tab widget
                cur_index = self.ui.tabWidget.addTab(new_page, cookbook_name)
                self.ui.tabWidget.setCurrentIndex(cur_index)
                self.ui.tabWidget.setVisible(True)

                # Create a horizontal layout to hold the buttons
                button_layout = QHBoxLayout()

                # Create the button for the new tab
                button = QPushButton(cookbook_name)
                button_layout.addWidget(button)

                # Create the edit icon
                edit_icon = QLabel()
                icon = "static/icons/edit.svg"
                icon_hover = "static/icons/edit-hover.svg"
                self.set_icon(edit_icon, icon)  # Set the edit icon
                self.setup_hover_effects(edit_icon, icon, icon_hover)  # Setup hover effects
                button_layout.addWidget(edit_icon)

                # Create the delete icon
                delete_icon = QLabel()
                icon = "static/icons/trash-2.svg"
                icon_hover = "static/icons/trash-2-red.svg"
                self.set_icon(delete_icon, icon)  # Set the delete icon
                self.setup_hover_effects(delete_icon, icon, icon_hover)  # Setup hover effects
                button_layout.addWidget(delete_icon)

                # Create a wrapper widget to hold the layout
                wrapper_widget = QWidget()
                wrapper_widget.setLayout(button_layout)

                # Insert the wrapper widget into the vertical layout
                self.ui.verticalLayout_2.insertWidget(0, wrapper_widget)

                # Connect button click signal to show_selected_page slot
                button.clicked.connect(self.show_selected_page)

                # Connect edit icon click signal to edit_button slot
                edit_icon.mousePressEvent = lambda event: self.edit_button(wrapper_widget, cur_index, cookbook_name)

                # Connect delete icon click signal to delete_button_and_tab slot
                delete_icon.mousePressEvent = lambda event: self.delete_button_and_tab(wrapper_widget, cur_index,
                                                                                       cookbook_name)
                # Set the toolBox to the "recipe"
                self.ui.toolBox.setCurrentIndex(1)  # Assuming "recipe" is at index 1
            else:
                print("Recipe not found")

        self.ui.lineEdit.clear()




    def delete_button_and_tab(self, wrapper_widget, tab_index, cookbook_name):
        """Delete the button, associated tab, and related data."""

        self.model.delete_by_cookbookName(cookbook_name)
        self.ui.verticalLayout_2.removeWidget(wrapper_widget)
        wrapper_widget.deleteLater()
        self.ui.tabWidget.removeTab(tab_index)

    def edit_button(self, wrapper_widget, tab_index, cookbook_name):
        """
        Handle the edit button click event.
        """
        # Get the current text of the button
        current_text = self.ui.tabWidget.tabText(tab_index)

        # Open a dialog to edit the cookbook name
        new_name, ok_pressed = QInputDialog.getText(self, "Edit", "Enter new name:", QLineEdit.Normal,
                                                    current_text)

        if ok_pressed and new_name.strip():
            # Update the button text
            self.ui.tabWidget.setTabText(tab_index, new_name)

            # Update the text of the button in the button layout
            button_layout = wrapper_widget.layout()
            button = button_layout.itemAt(0).widget()
            button.setText(new_name)

            self.model.update_cookbook_name(cookbook_name, new_name)

    def set_icon(self, label, icon_path):
        """Set the icon for a label."""

        pixmap = QPixmap(icon_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setFixedSize(16, 16)

    def change_icon_on_hover(self, label, icon, icon_hover, is_hovering):
        """Change the delete icon when hovering over it."""

        if is_hovering:
            self.set_icon(label, icon_hover)
        else:
            self.set_icon(label,icon)


    def setup_hover_effects(self, label, icon, icon_hover):
        """Setup hover effects for a label."""

        label.setMouseTracking(True)
        label.enterEvent = lambda event: self.change_icon_on_hover(label, icon, icon_hover, True)
        label.leaveEvent = lambda event: self.change_icon_on_hover(label, icon, icon_hover, False)


