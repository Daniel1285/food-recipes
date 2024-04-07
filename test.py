import requests
import json
from io import BytesIO

APP_ID = '41995353'
APP_KEY = '6b15ef1f2702dab80a37425f64371705'

# Base URL for the Edamam API
base_url = 'https://api.edamam.com/search'



def load_data(data):
    with open(data, 'r', encoding='utf-8') as f:
        return json.load(f)



def Get_recipe(query):

    # Make the request to the API
    response = requests.get(base_url, params={'q': query, 'app_id': APP_ID, 'app_key': APP_KEY})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data)
        # Create a list to store recipe details
        recipes = []

        # Extract and save the details for each recipe
        for hit in data['hits']:
            recipe = hit['recipe']
            recipe_details = {
                'name': recipe['label'],
                'ingredients': recipe['ingredientLines'],
                'imageUrl': recipe['image'],
                'url': recipe['url'],
            }
            recipes.append(recipe_details)

        # Save the recipes to a JSON file with UTF-8 encoding
        with open('recipes.json', 'w', encoding='utf-8') as f:
            json.dump(recipes, f, indent=4, ensure_ascii=False)
        
        # Print the result
        print(json.dumps(recipes, indent=4, ensure_ascii=False))
        
    else:
        print('Error:', response.status_code)



#================================================================c

def main():
    data = load_data("recipes.json")
    label = [recipe['label'] for recipe in data]

    print(label)


if __name__ == '__main__':
    main()


