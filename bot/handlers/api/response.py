import json

import requests


class BotAPI:
    def __init__(self):
        self.categories = 'http://localhost:8000/api/v1/category/'
        self.subcategory = 'http://localhost:8000/api/v1/subcategory/'
        self.products = 'http://localhost:8000/api/v1/products/'

    def json_loads(self, url):
        return json.loads(requests.get(url).text)

    def get_categories(self, cat_id=None):
        if cat_id:
            url = f"{self.categories}{cat_id}"
            return self.json_loads(url)

        return self.json_loads(self.categories)

    def get_subcateogries(self, sub_id=None):
        if sub_id:
            url = f"{self.subcategory}{sub_id}"
            return self.json_loads(url)

    def get_product(self, prod_id=None):
        if prod_id:
            url = f"{self.products}{prod_id}"
            return self.json_loads(url)


api_response = BotAPI()

if __name__ == '__main__':
    api_response = BotAPI()
    print(api_response.get_categories(1))
#
