import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/point/af/list.naver'

re = requests.get(url).text
soup = BeautifulSoup(re, 'html.parser')

point = []
review = []
num = []
title = []


data = soup.select("tbody tr th p.title a")

for item in data:
    title.append(item.string.strip())



data = soup.select('tbody tr td.left p.artist a')
for item in data:
    artist.append(item.string.strip())


items = list(zip(title, artist))
print(items)