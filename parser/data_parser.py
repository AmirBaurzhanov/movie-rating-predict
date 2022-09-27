import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


links = []
data = []

with open(r'links.txt', 'r') as r:
	for link in r:
		x = link[:len(link)-2]
		links.append(x)

def get_data(links, list):
	for link in links:
		page = requests.get(link)

		soup = bs(page.text, 'html.parser')
		print(link)

		actors = [soup.findAll('a', class_='sc-36c36dd0-1 QSQgP')[i].text for i in range(len(soup.findAll('a', class_='sc-36c36dd0-1 QSQgP')))]
		all_writers = [soup.select('.ipc-metadata-list__item:nth-child(2) > div > ul > li > a')[i].text for i in range(len(soup.select('.ipc-metadata-list__item:nth-child(2) > div > ul > li > a'))-2)]
		cert = None if len(soup.findAll('span', class_='sc-8c396aa2-2 itZqyK')) == 1 else soup.findAll('span', class_='sc-8c396aa2-2 itZqyK')[1].text
		data = {
			"title": soup.findAll('h1', class_='sc-b73cd867-0')[0].text,
			"year": soup.findAll('a', class_='ipc-link ipc-link--baseAlt ipc-link--inherit-color sc-8c396aa2-1 WIUyh')[0].text,
			"certificate": cert,
			"rating": soup.findAll('span', class_='sc-7ab21ed2-1 jGRxWM')[0].text,
			"description": soup.findAll('span', class_='sc-16ede01-2 gXUyNh')[0].text,
			"director": soup.select('li.ipc-metadata-list__item:first-child > div > ul > li > a')[0].text,
			"writer": all_writers,
			"actors": actors,
			"genres": soup.select('.ipc-chip-list__scroller')[0].text,
			"runtime": None if soup.select('.sc-80d4314-2.iJtmbR > ul > li:nth-child(3)') == [] else soup.select('.sc-80d4314-2.iJtmbR > ul > li:nth-child(3)')[0].text
		}

		list.append(data)
	return list


data = get_data(links, data)

films_df = pd.DataFrame(data)
films_df.to_csv('data.csv')
