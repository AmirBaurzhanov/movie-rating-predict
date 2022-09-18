from bs4 import BeautifulSoup as bs
import requests


urls = [f'https://www.kinopoisk.ru/lists/movies/popular-films/?page={i}' for i in range(1, 21)]

def get_link(url, result):
	list1 = []
	page = requests.get(url)

	if page.status_code == 200:
		soup = bs(page.text, 'html.parser')

	for link in soup.find_all('a', href=True):
		if '/film/' in link['href']:
			list1.append(link['href'])

	return list1

data = []

for i in range(20):
	data.append(get_link(urls[i], data))

print(len(data), data[0])