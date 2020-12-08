import requests
import environ
from django_list_v2.settings import TRAKT_API_URL



def call_api(serial_title: str) -> dict:
    response = requests.get(TRAKT_API_URL.format(serial_title), headers={
        'Content_type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': '6b3819e58b6b2b8b317bb2ee99988c2dab6e4ff3e2e865743cc0069b19d3b45f'
    })
    if response.status_code == 200:

        data = response.json()
        if type(data) is list:
            final_data = {
                'year': data[0]['show']['year'],
                'slug': data[0]['show']['ids']['slug'],
                'imdb': data[0]['show']['ids']['imdb'],
                'apititle': data[0]['show']['title']
            }
            return final_data
    else:
        raise Exception('UnknownError')