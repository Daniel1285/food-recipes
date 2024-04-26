from PySide6.QtWidgets import QApplication

from model import Recipe
from view import CookbookView
from controller import CookbookController

import asyncio


def main():
    app = QApplication([])
    model =  Recipe()
    view = CookbookView(model)
    controller = CookbookController(model, view)
    controller.run()
    app.exec()

if __name__ == "__main__":
   main()
