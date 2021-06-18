from bs4 import BeautifulSoup
import requests

url = 'https://store.steampowered.com/genre/Free%20to%20Play/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

mas = []

for element in soup.find_all('div', class_='tag_count_button'):
    text = element.text
    mas.append(text)

def slovar(spisok):
    qwq = ''.join(spisok)
    qq = qwq.split()
    b = {qq[i]: qq[i + 1] for i in range(0, len(qq), 2)}
    return b


print(slovar(mas))
