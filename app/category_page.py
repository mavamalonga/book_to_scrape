import requests
from bs4 import BeautifulSoup
import csv

class Scrape_category:

	 def __init__(self, url):
	 	category_page_url = url
	 	response = requests.get(category_page_url)
	 	if response.status_code == requests.codes.ok:
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 		self.request_200 = True
	 	else:
	 		self.request_200 = False

	 def get_urls(self):
	 	url_list = []
	 	articles_list = self.soup.find_all("article", class_="product_pod")

	 	for article in articles_list:
	 		url_list.append(article.find("div", class_="image_container").find("a")["href"])
	 	return url_list

	 def clean_urls(self, list_url):
	 	new_url_list = []
	 	for url in list_url:
	 		new_url_list.append(url[8:])
	 	return new_url_list

	 def main(self):
	 	url_list = self.get_urls()
	 	new_url_list = self.clean_urls(url_list)
	 	return new_url_list

