import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.chitalnya.ru/work/3211282/'
response = requests.get(url).text
soup = bs(response, 'html.parser')
weather = soup.find('div', class_='col-md-9 x2')
print(weather.text)

