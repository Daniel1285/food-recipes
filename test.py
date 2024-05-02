import requests
import json

import model
from model import Recipe

def load_data(data):
    with open(data, 'r', encoding='utf-8') as f:
        return json.load(f)

#================================================================c

def main():
    url = input("Enter url: ")
    print(url)
    option = model.Recipe().request_ImaggaApi(url)


if __name__ == '__main__':
    main()


