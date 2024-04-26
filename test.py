import requests
import json
from model import Recipe

APP_ID = '41995353'
APP_KEY = '6b15ef1f2702dab80a37425f64371705'

# Base URL for the Edamam API
base_url = 'https://api.edamam.com/search'

def load_data(data):
    with open(data, 'r', encoding='utf-8') as f:
        return json.load(f)

#================================================================c

def main():
    pass


if __name__ == '__main__':
    main()


