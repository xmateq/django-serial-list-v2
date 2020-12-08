import requests
import environ
import jmespath
from django_list_v2.settings import TRAKT_API_URL

HTTP_200_OK = 200
headers = {
        'Content_type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': '6b3819e58b6b2b8b317bb2ee99988c2dab6e4ff3e2e865743cc0069b19d3b45f'
    }


def call_api(serial_title: str) -> dict:
    response = requests.get(TRAKT_API_URL.format(serial_title), headers=headers)
    if response.status_code == HTTP_200_OK:

        data = response.json()
        if type(data) is list:
            final_data = {
                'year': jmespath.search('show.year', data[0]),
                'slug': jmespath.search('show.ids.slug', data[0]),
                'imdb': jmespath.search('show.ids.imdb', data[0]),
                'apititle': jmespath.search('show.title', data[0])
                }
            return final_data
    else:
        raise Exception('UnknownError')