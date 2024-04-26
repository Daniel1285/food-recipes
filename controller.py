class CookbookController:
    """
    Controller class responsible for managing interaction between model and view.

    Attributes:
        model: The model component of the MVC architecture.
        view: The view component of the MVC architecture.
    """

    def __init__(self, model, view):
        """
        Initialize the CookbookController.

        Args:
            model: The model component of the MVC architecture.
            view: The view component of the MVC architecture.
        """
        self.model = model
        self.view = view

    def run(self):
        """Run the controller."""
        self.view.show()
