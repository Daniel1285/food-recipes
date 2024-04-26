from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea, QHBoxLayout
from ui.pages.recipe_ui import RecipeWidget

class RecipePage(QMainWindow):
    """
    Class representing the recipe page in the Cookbook application.
    """
    def __init__(self, recipe_data):
        """
        Initializes the RecipePage class.

        Args:
            recipe_data: Data of recipes to be displayed.
        """
        super().__init__()
        self.setWindowTitle("Recipe Viewer")  # Set window title
        self.setGeometry(100, 100, 1200, 700)  # Set window geometry
        self.central_widget = QWidget()  # Create central widget
        self.setCentralWidget(self.central_widget)  # Set central widget
        self.layout = QVBoxLayout(self.central_widget)  # Create vertical layout
        self.recipe_data = recipe_data  # Store recipe data
        self.fetch_and_display_recipes()  # Fetch and display recipes

    def fetch_and_display_recipes(self):
        """
        Fetches and displays recipes.
        """
        # Await the coroutine to get the actual data
        #actual_recipe_data = await self.recipe_data

        scroll_area = QScrollArea()  # Create scroll area
        scroll_area.setWidgetResizable(True)  # Allow scroll area content to be resizable
        scroll_area_content = QWidget()  # Create widget for scroll area content
        scroll_area.setWidget(scroll_area_content)  # Set widget for scroll area
        scroll_layout = QVBoxLayout(scroll_area_content)  # Create vertical layout for scroll area content

        row_layout = None  # Initialize row layout
        for i, data in enumerate(self.recipe_data):
            if i % 3 == 0:
                if row_layout:
                    scroll_layout.addSpacing(10)  # Add spacing between rows
                row_layout = QHBoxLayout()  # Create horizontal layout for a row of recipe widgets
                scroll_layout.addLayout(row_layout)  # Add row layout to scroll layout
            recipe_widget = RecipeWidget(data)  # Create recipe widget with provided data
            row_layout.addWidget(recipe_widget)  # Add recipe widget to row layout

        self.layout.addWidget(scroll_area)  # Add scroll area to the main layout
