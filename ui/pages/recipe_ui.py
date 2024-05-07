from PySide6.QtWidgets import QWidget, QDialog, QVBoxLayout, QPushButton, QLabel, QFrame, QScrollArea
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
import requests
from PIL import Image
from io import BytesIO
from threading import Thread

class IngredientsWindow(QDialog):
    """
    A dialog window to display a list of ingredients.

    Args:
        ingredients_text (str): The text containing the list of ingredients.
        parent (QWidget, optional): The parent widget. Defaults to None.
    """

    def __init__(self, ingredients_text, parent=None):
        """
        Initializes the IngredientsWindow.

        Args:
            ingredients_text (str): The text containing the list of ingredients.
            parent (QWidget, optional): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.ingredients_text = ingredients_text
        self.init_ui()

    def init_ui(self):
        """Initializes the user interface of the window."""
        layout = QVBoxLayout()

        # Create a scroll area to contain the ingredients label
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a QLabel to display the ingredients text with styled dots
        ingredients_label = QLabel()
        ingredients_label.setStyleSheet(
            """
            QLabel {
                font-size: 12px;
                padding: 5px;
            }
            QLabel::item {
                border-bottom: 1px solid #ccc;
                padding-left: 10px;
                margin-bottom: 5px;
            }
            """
        )
        ingredients_label.setTextFormat(Qt.RichText)

        # Style each ingredient row with a round dot
        formatted_ingredients_text = "<ul>"
        for ingredient in self.ingredients_text.split(","):
            formatted_ingredients_text += f"<li>&#8226; {ingredient}</li>"
        formatted_ingredients_text += "</ul>"
        ingredients_label.setText(formatted_ingredients_text)

        scroll_area.setWidget(ingredients_label)
        layout.addWidget(scroll_area)

        self.setLayout(layout)
        self.setWindowTitle("Ingredients List")
        self.setFixedSize(600, 300)


class RecipeWidget(QFrame):
    """
    A widget to display recipe information.

    Attributes:
        recipe_data (dict): A dictionary containing recipe information.
    """

    def __init__(self, recipe_data, parent=None):
        """
        Initialize the RecipeWidget.

        Args:
            recipe_data (dict): A dictionary containing recipe information.
            parent (QWidget): The parent widget. Defaults to None.
        """
        super().__init__(parent)
        self.recipe_data = recipe_data if isinstance(recipe_data, dict) else {}
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface of the widget."""
        layout = QVBoxLayout()

        # Display recipe name
        name_label = QLabel(self.recipe_data.get('name', 'No Name'))
        name_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(name_label)

        # background_label = QLabel()
        # image_path = r"C:\Users\Daniel\Desktop\food-recipes\static\images\timeOut_image.jpg"
        # background_label.setPixmap(self.image_processing(image_path))
        # background_label.setAlignment(Qt.AlignCenter)
        # layout.addWidget(background_label)

        background_label = QLabel()
        image_url = self.recipe_data.get('imageUrl', '')
        if image_url:
            thread = Thread(target=self.fetch_image, args=(image_url, background_label))
            thread.start()

        layout.addWidget(background_label)

        # Create buttons for recipe link and opening grocery window
        btn_style = """
            QPushButton {
                color: #fff;
                background-color: #29323c;
                padding: 5px 0px 5px 20px;
                text-align: left;
                border-radius: 3px;
            }

            QPushButton:hover {
                background-color: #485563;
            }

            QPushButton:checked {
                background-color: #4398d8;
            }
        """
        link_button = QPushButton("Recipe Link")
        link_button.setStyleSheet(btn_style)
        layout.addWidget(link_button)
        link_button.clicked.connect(self.open_recipe_link)

        grocery_button = QPushButton("Open Grocery Window")
        grocery_button.setStyleSheet(btn_style)
        layout.addWidget(grocery_button)
        grocery_button.clicked.connect(self.open_ingredients_window)

        layout.addStretch(1)

        self.setLayout(layout)
        self.setMaximumHeight(300)
        self.setMaximumWidth(400)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)

    def fetch_image(self, image_url, label):
        try:
            response = requests.get(image_url, verify=False)
            if response.status_code == 200:
                image_data = BytesIO(response.content)
                pixmap = self.image_processing(image_data)
                self.update_image(label, pixmap)
            else:
                print(f"Failed to fetch image: HTTP status code {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image: {e}")
            image_path = r"C:\Users\Daniel\Desktop\food-recipes\static\images\timeOut_image.jpg"
            pixmap = self.image_processing(image_path)
            self.update_image(label, pixmap)
        except Exception as e:
            print(f"Error loading image: {e}")
            image_path = r"C:\Users\Daniel\Desktop\food-recipes\static\images\timeOut_image.jpg"
            pixmap = self.image_processing(image_path)
            self.update_image(label, pixmap)

    def update_image(self, label, pixmap):
        label.setPixmap(pixmap)
        label.setAlignment(Qt.AlignCenter)

    def open_recipe_link(self):
        """Open the recipe link in the default web browser."""
        recipe_link = self.recipe_data.get('url', '')
        if recipe_link:
            QDesktopServices.openUrl(QUrl(recipe_link))

    def open_ingredients_window(self):
        """Open a window displaying the ingredients."""
        ingredients = self.recipe_data.get('ingredients')
        ingredients_window = IngredientsWindow(ingredients)
        ingredients_window.exec_()

    def image_processing(self, image):
        """Process the input image and convert it to a QPixmap."""
        image = Image.open(image)
        image = image.convert("RGBA")
        image_qt = QImage(image.tobytes(), image.size[0], image.size[1], QImage.Format_RGBA8888)
        pixmap = QPixmap.fromImage(image_qt)
        return pixmap
