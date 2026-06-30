import requests
from bs4 import BeautifulSoup

r = requests.get('https://legal-privacy.ru/')
print(r.status_code)

soup = BeautifulSoup(r.text, 'html.parser')
print(f"Заголовок сайта: {soup.title.string}")