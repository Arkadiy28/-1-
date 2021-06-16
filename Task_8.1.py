from bs4 import BeautifulSoup
import requests

url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

mas = {}

for element in soup.find_all('a'):
    href = element.get('href')
    text = element.text
    mas[href] = text

for k, v in mas.items():
    if 'Free To Play' in v:
        print(k, v)
