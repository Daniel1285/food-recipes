from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton, QLabel, QFrame, QScrollArea, QHBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
import requests
from PIL import Image
from io import BytesIO

class RecipeWidget(QFrame):
    def __init__(self, recipe_data, parent=None):
        super().__init__(parent)
        self.recipe_data = recipe_data if isinstance(recipe_data, dict) else {}
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        # Access recipe data only if it's a dictionary
        name_label = QLabel(self.recipe_data.get('name', 'No Name'))
        name_label.setAlignment(Qt.AlignLeft)
        layout.addWidget(name_label)

        background_label = QLabel()
        image_url = self.recipe_data.get('imageUrl', '')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
        }
        if image_url:
            try:
                response = requests.get(image_url, headers)
                if response.status_code == 200:
                    image_data = BytesIO(response.content)
                    image = Image.open(image_data)
                    image = image.convert("RGBA")
                    image_qt = QImage(image.tobytes(), image.size[0], image.size[1], QImage.Format_RGBA8888)
                    pixmap = QPixmap.fromImage(image_qt)
                    background_label.setPixmap(pixmap)
                    background_label.setAlignment(Qt.AlignCenter)
                else:
                    print(f"Failed to fetch image: HTTP status code {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching image: {e}")
            except Exception as e:
                print(f"Error loading image: {e}")
                
        layout.addWidget(background_label)
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

        layout.addStretch(1)

        self.setLayout(layout)
        self.setMaximumHeight(300)
        self.setFrameShape(QFrame.Box)
        self.setFrameShadow(QFrame.Sunken)

    def open_recipe_link(self):
        recipe_link = self.recipe_data.get('url', '')
        if recipe_link:
            QDesktopServices.openUrl(QUrl(recipe_link))
        
    def open_grocery_window(self):
        pass
   