import requests
from urllib.parse import quote
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


    # def get_recipe(self, query):
    #     url = f'https://localhost:7007/api/Recipe/ByCookbookName/{query}'
    #     response = self.requestApi(url)
    #     return response

    # def request_EdamamApi(self, query):
    #     url = f'https://localhost:7007/api/Edamam/{query}'
    #     response = self.requestApi(url)
    #     return response
    #

    # def delete_by_cookbookName(self, query):
    #     url = f'https://localhost:7007/api/Recipe/DeleteByCookbookName/{query}'
    #     response = self.requestApi(url)
    #     return response


    def get_recipe(self, query):
        url = f'https://localhost:7012/api/Test1/ByCookbookName/{query}'
        response = self.requestApi(url)
        return response



    def request_EdamamApi(self, query):
        url = f'https://localhost:7012/api/Test2/{query}'
        response = self.requestApi(url)
        return response

    def request_ImaggaApi(self, query):
        encoded_query = quote(query, safe='')
        url = f'https://localhost:7012/api/Test3/{encoded_query}'
        response = self.requestApi(url)
        return response
    def delete_by_cookbookName(self, query):
        url = f'https://localhost:7012/api/Test1/DeleteByCookbookName/{query}'
        response = self.requestApi(url)
        return response