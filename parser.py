import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('COUNTRY_LAYER_API_KEY')


def get_countries():
    url = f'https://api.countrylayer.com/v2/all?access_key={api_key}'
    response = requests.get(url)
    countries = response.json()
    for country in countries:
        payload = {
            'name': country['name'],
            'alpha2Code': country['alpha2Code'],
            'alpha3Code': country['alpha3Code'],
            'capital': country['capital'],
            'region': country['region']
        }
        response = requests.post('http://127.0.0.1:8000/post/country/', json=payload)

        if response.status_code != 201:
            print(f'Error: {response.status_code} {country}')


if __name__ == '__main__':
    get_countries()
