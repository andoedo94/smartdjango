import logging
import requests


def request_get(url, params):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error("Error in the request code:  " + str(response.status_code))
        return None
