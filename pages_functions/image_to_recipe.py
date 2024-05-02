from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea
from PySide6 import QtCore
#from PySide6.QtCore import Signal
from ui.pages.image_to_recipe_ui import Ui_Form

class Image_to_recipe(QWidget, QtCore.QObject):

    recipeSelected = QtCore.Signal(str)

    def __init__(self):
        super(Image_to_recipe, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.imagga_searchButton.clicked.connect(self.add_buttons)
        self.ui.getRecipeButton.clicked.connect(self.is_clicked)
        self.middle_frame = self.ui.middle_frame

        self.selected_button = None  # keep track of the selected button

    def add_buttons(self):
        url = self.ui.input_imageUrl.text()
        #response = model.Recipe().request_ImaggaApi(url)
        response = [ "Pizza",  "Burger","Pasta",  "Sushi", "Salad", "Steak",  "Tacos", "Chicken",
                      "Rice","Soup", "Sandwich", "Curry", "Omelette", "Fries", "Lasagna", "Shrimp",
                      "Pancakes",  "Smoothie", "Donuts","Ice Cream", "Apple Cake"]
                      

        self.middle_frame.setLayout(QVBoxLayout())

        # Clear existing buttons from middle_frame
        for widget in self.middle_frame.findChildren(QPushButton):
            widget.deleteLater()
                

        btn_style = """
            QPushButton {
                color: #fff;
                background-color: #29323c;
                text-align: center;
                border-radius: 3px;
            }

            QPushButton:hover {
                background-color: #485563;
            }

            QPushButton:checked {
                background-color: #4398d8;
            }
        """
        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("background-color: white;")
        scroll_layout = QVBoxLayout(scroll_widget)

        # Add buttons for each option in the response
        row_layout = None
        for i, option in enumerate(response):
            if i % 5 == 0:
                row_layout = QHBoxLayout()
                scroll_layout.addLayout(row_layout)
            button = QPushButton(option)
            button.setFixedWidth(200)
            button.setMinimumSize(0, 30)
            button.setStyleSheet(btn_style)
            button.setCheckable(True)
            button.clicked.connect(self.button_clicked)
            row_layout.addWidget(button)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)
        scroll_area.setStyleSheet("QScrollArea { border: none; }")

        self.middle_frame.setLayout(QVBoxLayout())
        self.middle_frame.layout().addWidget(scroll_area)



    def button_clicked(self):
        button = self.sender()
        self.selected_button = button  # Update the selected button

        for btn in button.parent().findChildren(QPushButton):  # Iterate through buttons in the same layout
            if btn is button:
                btn.setChecked(True)  
            else:
                btn.setChecked(False) 
        

    def is_clicked(self):
        if self.selected_button:
            name = self.selected_button.text()
            print("Selected Button:", name)
            self.recipeSelected.emit(name)
        else:
            print("No button selected.")