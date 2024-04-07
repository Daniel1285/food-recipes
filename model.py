class Cookbook:
    # def __init__(self, id, name, options):
    #     self.id = id
    #     self.name = name
    #     self.options = options if options is not None else []
    pass

    
class Recipe: 
    def __init__(self, id, name, ingredients, imageUrl, url):
        self.id = id
        self.name = name
        self.ingredients = ingredients
        self.imageUrl = imageUrl
        self.url = url
