from bs4 import BeautifulSoup
from datetime import date
import requests

url = "https://www.jrepodcast.com/"

res = requests.get(url).text

soup = BeautifulSoup(res, 'lxml')
dates = soup.find_all('time', attrs= {'class' : 'entry-date published'})
titles = soup.find_all('h3', attrs= {'class' : 'card__title'})
intro = soup.find_all('div', attrs= {'class' : 'card__excerpt'})


with open('scrape.html', 'w') as file:
    for item in range(len(intro)):
        file.write(str(titles[item]) + '\n')
        file.write(str(intro[item]) + '\n')
        file.write(str(dates[item]) + '\n')
        file.write('<br>')
        file.write('<br>')

today = date.today()
date_format = today.strftime('%Y.%m.%d')

file = open('scrape.html', 'a')
file.write('<hr>')
file.write('\nLast checked: ')
file.write(date_format)
file.close()


scrape = open('scrape.html', 'r')
scrape_content = scrape.read()
index = open('index.html', 'w+')
index_content = index.read()


if not (bool(scrape_content == index_content)):
    index.write(scrape_content)

index.close()
scrape.close()

