import requests
import jmespath
from django_list_v2.settings import TRAKT_API_URL, env

HTTP_200_OK = 200
HEADERS = {
        'Content_type': 'application/json',
        'trakt-api-version': '2',
        'trakt-api-key': env('TRAKT_API_KEY')
    }


def call_api(serial_title: str) -> dict:
    response = requests.get(TRAKT_API_URL.format(serial_title), headers=HEADERS)
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
        return {
            'year': None,
            'slug': None,
            'imdb': None,
            'apititle': None
        }