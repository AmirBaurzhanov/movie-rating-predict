from bs4 import BeautifulSoup as bs
import requests

urls = [f'https://www.imdb.com/list/ls002209246/?st_dt=&mode=detail&page={i}&sort=list_order,asc' for i in range(1, 11)]
links = []

def get_link(url, result):
	page = requests.get(url)

	if page.status_code == 200:
		soup = bs(page.text, 'html.parser')

	for link in soup.select('.lister-item-header > a', href=True):
		if '/title/' in link['href']:
			result.append(f"https://www.imdb.com{link['href']}/")

	return result


for i in range(10):
	links = get_link(urls[i], links)

with open(r'links.txt', 'w') as f:
	for link in links:
		f.write("%s\n" % link)
