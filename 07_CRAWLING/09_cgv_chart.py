import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/movies/?lt=1&ft=0'

re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')
name = []

data = soup.select('strong.title')

for item in data:
    name.append(item.string.strip())
print(name)
