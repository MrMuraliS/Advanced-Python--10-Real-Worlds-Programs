from selectorlib import Extractor
import requests


class Temperature:
    """
    This will calculate the temperature based on the location
    user has provided.
    """

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        url = f'https://www.timeanddate.com/weather/{self.country}/{self.city}'
        r = requests.get(url)

        if r.status_code == 200:
            extractor = Extractor.from_yaml_file('temperature.yaml')
            raw_results = extractor.extract(r.text)['temp'].replace('\xa0°C', '').strip()
            return raw_results
        else:
            return "City or Country doesn't exist"



