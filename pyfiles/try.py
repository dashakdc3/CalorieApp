from selectorlib import Extractor
# for extracting data from web page
import requests
from pprint import pprint
# pprint - pretty print

response = requests.get("https://www.timeanddate.com/weather")
# print(response)

# NOTE!!!
# if not response [200], requests.get("https://www.timeanddate.com/weather", headers = h)
# h = info from headers_for_scraping.txt (app 6)

x = response.content
# print(pprint(x))
# print(type(x))
# <class 'bytes'>

x = response.text
# print(type(x))
# <class 'str'>

extractor = Extractor.from_yaml_file('temperature.yaml')
# a method from_yaml_file()initiolyses the Extractor class. and this Exctractor need an Xpath, that we give


t = extractor.extract(x)
# print(extractor.extract(x))
# extractor.extract() - we need the source code for this, and this sourse code is on veriable x
print(t['temp'])

temp = t['temp'].replace(" °C", "")
print(float(temp))
y = 10
print(dir(str))
