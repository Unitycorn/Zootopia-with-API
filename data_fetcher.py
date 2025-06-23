from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

REQUEST_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = os.getenv('API_KEY')


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def fetch_data(animal_name):
    """Fetching animal data from API"""
    return requests.get(REQUEST_URL + animal_name, headers={"X-Api-Key": API_KEY}).json()
