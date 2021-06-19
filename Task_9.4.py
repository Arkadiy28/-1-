from bs4 import BeautifulSoup
import requests
import re

url = 'https://ru.wikipedia.org/wiki/Небьюла'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

sylki = []

for element in soup.find_all('a'):
    href = element.get('href')
    sylki.append(href)

syl = str(sylki)

s = re.findall('https://[A-z%:./0-9]+', syl)

for i in s:
    if 'wikipedia' not in i:
        print(i)
