import requests
import json
class Recipe:
    def __init__(self):
        self.id = None
        self.cookbook_name = None
        self.name = None
        self.ingredients = None
        self.image_url = None
        self.url = None


    def print_recipe(self):
        print(f"Cookbook name: {self.cookbook_name}")
        print(f"Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Image URL: {self.image_url}")
        print(f"URL: {self.url}\n")




    def requestApi(self, address):
        try:
            # Send a GET request to the server
            response = requests.get(address, verify=False)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Print the response from the server
                print("Response from server:\n", response.json())
                return response.json()
            else:
                print("Error:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", e)


    def get_recipe(self, query):
        url = f'https://localhost:7012/api/Test1/ByCookbookName/{query}'
        response = self.requestApi(url)
        return response


    def request_EdamamApi(self, query):
        url = f'https://localhost:7012/api/Test2/{query}'
        response = self.requestApi(url)
        return response


















#===============================================================================================
        # base_url = "https://api.edamam.com/search"
        # app_id = "41995353"
        # app_key = "6b15ef1f2702dab80a37425f64371705"
        #
        # response = requests.get(f"{base_url}?q={query}&app_id={app_id}&app_key={app_key}")
        #
        # if response.status_code == 200:
        #     data = response.json()
        #
        #     for hit in data.get('hits', []):
        #         recipe_details = hit.get('recipe', {})
        #         recipe = Recipe()
        #         recipe.cookbook_name = query
        #         recipe.name = recipe_details.get('label')
        #         recipe.ingredients = ", ".join(recipe_details.get('ingredientLines', []))
        #         recipe.image_url = recipe_details.get('image')
        #         recipe.url = recipe_details.get('url')
        #         recipe.print_recipe()
        # else:
        #     print("Failed to retrieve recipe data. Status code:", response.status_code)
