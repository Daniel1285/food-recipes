from PySide6.QtWidgets import QApplication

from model import Cookbook
from view import CookbookView
from controller import CookbookController


def main():
    app = QApplication([])
    model =  Cookbook() 
    view = CookbookView(model)
    controller = CookbookController(model, view)
    controller.run()
    app.exec()

if __name__ == "__main__":
    main()    
