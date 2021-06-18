from bs4 import BeautifulSoup
import requests

url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

mas = {}


for rr in soup.find_all('div', class_='tag_count_button'):
    name = rr.find('span', class_='tag_name').text
    tags = None
    for i in rr.find_all('span', class_='tag_count tab_filter_control_count'):
        tags = i.text
    mas[name] = tags

print(mas)
