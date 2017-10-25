import requests
import json

# Initalization of variables and other stuff
BASE_URL = 'https://api.fixer.io/'

class Pycur:

    def __init__(self, base=None):
        self.base = base
        if type(self.base) != str:
            raise ("Error")

    def get_currency(self):
        self.URL = BASE_URL + 'latest?base={}'.format(self.base)
        self.raw_data = requests.get(self.URL).text
        self.data = json.loads(self.raw_data)
        return self.data['rates']

    def get_historical(self, date):
        self.date = date
        self.URL = BASE_URL + '{}?base={}'.format(self.date, self.base)
        self.raw_data = requests.get(self.URL).text
        self.data = json.loads(self.raw_data)
        return self.data['rates']
