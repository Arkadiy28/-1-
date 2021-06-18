from bs4 import BeautifulSoup
import requests

url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')



mas = {}

for rr in soup.find_all('div', class_='tab_item_content'):
    name = rr.find('div', class_='tab_item_name').text
    tags = []
    for i in rr.find_all('div', class_='tab_item_top_tags'):
        tags.append(i.text)
    mas[name] = tags

print(mas)
