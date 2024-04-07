class CookbookController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def run(self):    
        self.view.show()
