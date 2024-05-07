import requests
import logging
from urllib.parse import quote


class Recipe:
    """
    Class representing a recipe.
    """
    def __init__(self):
        """
        Initializes a Recipe object.
        """
        self.id = None
        self.cookbook_name = None
        self.name = None
        self.ingredients = None
        self.image_url = None
        self.url = None

    def print_recipe(self):
        """Print details of the recipe."""

        print(f"Cookbook name: {self.cookbook_name}")
        print(f"Name: {self.name}")
        print(f"Ingredients: {self.ingredients}")
        print(f"Image URL: {self.image_url}")
        print(f"URL: {self.url}\n")

    def requestApi(self, address):
        """Send a GET request to the provided address."""

        try:
            response = requests.get(address)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return None

    def get_recipe(self, query):
        """Get recipe by cookbook name."""

        url = f'http://localhost:7007/api/Recipe/ByCookbookName/{query}'
        return self.requestApi(url)

    def request_EdamamApi(self, query):
        """Request data from server."""

        url = f'http://localhost:7007/api/Edamam/{query}'
        return self.requestApi(url)

    def request_ImaggaApi(self, query):
        """Request data from server."""

        encoded_query = quote(query, safe='')
        url = f'http://localhost:7007/api/Imagga/{encoded_query}'
        return self.requestApi(url)

    def delete_by_cookbookName(self, cookbook_name):
        """Delete recipe by cookbook name."""

        url = f"http://localhost:7007/api/Recipe/DeleteByCookbookName/{cookbook_name}"
        response = requests.delete(url)
        if response.status_code == 204:
            return "Recipe deleted successfully."
        elif response.status_code == 404:
            return "No Recipe found with the specified cookbook name."
        else:
            return f"Error occurred: {response.text}"

    def update_cookbook_name(self, old_cookbook_name, new_cookbook_name):
        """Update cookbook name."""

        url = f"http://localhost:7007/api/Recipe/UpdateCookbookName?"
        data = {
            'oldCookbookName': old_cookbook_name,
            'newCookbookName': new_cookbook_name
        }

        response = requests.put(url, params=data)

        if response.status_code == 204:
            return "Cookbook name updated successfully."
        elif response.status_code == 404:
            return "No entities found with the old cookbook name."
        else:
            return f"Error occurred: {response.text}"

    # def get_recipe(self, query):
    #     url = f'http://localhost:7012/api/Test1/ByCookbookName/{query}'
    #     response = self.requestApi(url)
    #     return response
    #
    # def request_EdamamApi(self, query):
    #     url = f'http://localhost:7012/api/Test2/{query}'
    #     response = self.requestApi(url)
    #     return response
    #
    # def request_ImaggaApi(self, query):
    #     encoded_query = quote(query, safe='')
    #     url = f'http://localhost:7012/api/Test3/{encoded_query}'
    #     response = self.requestApi(url)
    #     return response
    #
    # def delete_by_cookbookName(self, cookbook_name):
    #     # URL of your API endpoint
    #     url = f"http://localhost:7012/api/Test1/DeleteByCookbookName/{cookbook_name}"
    #
    #     # Sending DELETE request to the API endpoint
    #     response = requests.delete(url)
    #
    #     # Checking the response status
    #     if response.status_code == 204:
    #         return "Tests deleted successfully."
    #     elif response.status_code == 404:
    #         return "No tests found with the specified cookbook name."
    #     else:
    #         return f"Error occurred: {response.text}"
    #
    # def update_cookbook_name(self, old_cookbook_name, new_cookbook_name):
    #
    #     url = f"http://localhost:7012/api/Test1/UpdateCookbookName?"
    #
    #     data = {
    #         'oldCookbookName': old_cookbook_name,
    #         'newCookbookName': new_cookbook_name
    #     }
    #
    #     # Sending PUT request to the API endpoint
    #     response = requests.put(url, params=data)
    #
    #     # Checking the response status
    #     if response.status_code == 204:
    #         print("Cookbook name updated successfully.")
    #         return "Cookbook name updated successfully."
    #     elif response.status_code == 404:
    #         print("No entities found with the old cookbook name.")
    #         return "No entities found with the old cookbook name."
    #     else:
    #         print(f"Error occurred: {response.text}")
    #         return f"Error occurred: {response.text}"
