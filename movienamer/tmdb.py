import json
import urllib

import requests

TMDB_API_KEY = '4ec9e70a6068fa052f00fcd4c03b6c46'
TMDB_HOST = 'http://api.themoviedb.org/3'


def search(name, year=None):
    if name is None or name == '':
        raise Exception

    if isinstance(name, unicode):
        name = name.encode('utf8')

    endpoint = TMDB_HOST + '/search/movie'
    payload = {'api_key': TMDB_API_KEY, 'query': urllib.quote_plus(str(name))}
    if year is not None:
        payload['year'] = year

    try:
        response = requests.get(endpoint, params=payload, timeout=5)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        raise Exception

    try:
        result = json.loads(response.text)
        return result['results']
    except ValueError:
        raise Exception
