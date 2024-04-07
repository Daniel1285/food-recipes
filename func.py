import requests
from io import BytesIO
import json
import os

APP_ID = '41995353'
APP_KEY = '6b15ef1f2702dab80a37425f64371705'


# Function to fetch recipes based on the user's input query
def fetch_recipes(query):

    base_url = 'https://api.edamam.com/search'

    # Make the request to the API
    response = requests.get(base_url, params={'q': query, 'app_id': APP_ID, 'app_key': APP_KEY})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        API_data = response.json()

        # Create a list to store recipe details
        recipes = []

        # Extract and save the details for each recipe
        for hit in API_data['hits']:
            recipe = hit['recipe']
            recipe_details = {
                'label': recipe['label'],
                'ingredients': recipe['ingredientLines'],
                'img': recipe['image']
            }
            recipes.append(recipe_details)

            # # Display the image associated with the recipe
            # img_url = recipe['image']
            # response = requests.get(img_url)
            # img = Image.open(BytesIO(response.content))
            # img.show()

        return recipes

    else:
        print('Error:', response.status_code)
        return []


# Function to save recipes to a JSON file
def save_recipes(data):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        print("User results saved successfully!")


# Function to load user results from a JSON file
def load_data():
    if os.path.exists('data.json'):
        with open('data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return []


def get_all_user_requests(data):
    return [key for result in data for key in result.keys()]

# Function to print recipes children from one result of the user input
def print_user_result(user_input, data):
    for result in data:
        if user_input in result:
            print(f"Results for '{user_input}':")
            for recipe in result[user_input]:
                print("Label:", recipe['label'])
                print("Ingredients:")
                for ingredient in recipe['ingredients']:
                    print("- ", ingredient)
                print("Image URL:", recipe['img'])
            return
    print(f"No results found for '{user_input}'.")


# Function to display all labels and allow the user to select a recipe by number
def get_ingredients(user_input, data):
    # Display all labels for the user input
    all_request = get_all_user_requests(data)
    parent_recipe = all_request[user_input]
    print(parent_recipe)
    category = []
    for result in data:
        if parent_recipe in result:
            for recipe in result[parent_recipe]:
                category.append(recipe['label'])

    for i in range(1, len(category)):
        print(f"{i}. {category[i]}")

    user_choice = int(input("Choose which recipe you want to display the ingredients you need:"))

    ingredients = data[user_input][parent_recipe][user_choice]["ingredients"]
    for ingredient in ingredients:
        print(ingredient)

# Chocolate Cake




def main():

    # Load user results from the JSON file
    data = load_data()





#     recipes = get_all_user_requests(data)
#     for i in range(len(recipes)):
#         print(f"{i}. {recipes[i]}")

#     user_input = int(input("Select a parent recipe: "))

   
#    # Call the function to display all labels and allow the user to select a recipe by number
#     get_ingredients(user_input, data)


if __name__ == '__main__':
    main()




#==================================================================================

    """
    Prompt the user to input their queries and fetch recipes for each query
    data = []
    while True:
        user_input = input("Enter your recipe query (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
    
        recipes = fetch_recipes(user_input)
        data.append({user_input: recipes})
    
    # Save the user results to a JSON file
    save_recipes(data) 
    """