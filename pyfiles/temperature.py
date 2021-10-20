import requests
from selectorlib import Extractor


class Temperature:
    """a scraper that uses an yml file to read the xpath of a value it needs to extract from the https://www.timeanddate.com/weather url"""

    base_url = "https://www.timeanddate.com/weather/"
    yml_path = "temperature1.yaml"
    h = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    def __init__(self, country, city):
        self.c = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Builds the url string ading country and city"""
        url = self.base_url + self.c + "/" + self.city
        return url
        # _build_url we use _ for getting access to a complete "return" of this function

    def _scrape(self):
        """Extracts a value as instracted the yml file and returns a dictionary"""
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        print(extractor)
        r = requests.get(url=url, headers=self.h)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of _scrape"""
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace(" °C", "").strip())
        # .strip() - removes all spaces


if __name__ == "__main__":
    temperature = Temperature(city="Minsk", country="Belarus")
    print(temperature._scrape())
    print(temperature.get())

# if __name__ == "__main__": that helps us not to execute this code, if we importing it to another
