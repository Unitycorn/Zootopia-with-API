import requests
import json

REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "gf743J9I+YtnTkhjgvudxA==C7see5DHXn9hgBcH"


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def fetch_data(animal_name):
    """Fetching animal data from API"""
    return requests.get(REQUEST_URL + animal_name, headers={"X-Api-Key": API_KEY}).json()
