import requests
from bs4 import BeautifulSoup
import csv

class Extract_urls:

	 def __init__(self, url):
	 	self.category_page_url = url

	 def make_request(self):
	 	try:
	 		response = requests.get(self.category_page_url)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 		print(f"Request successful!; status_code : {response.status_code}")
	 		return response.status_code
	 	except Exception as e:
	 		print(f"Failed request!; ERROR : {e}")
	 		return None

	 def get_urls(self):
	 	articles_list = self.soup.find_all("article", class_="product_pod")
	 	urls_list = []
	 	for article in articles_list:
	 		urls_list.append(article.find("div", class_="image_container").find("a")["href"])
	 	return urls_list

	 def clean_urls(self, list_url):
	 	new_url_list = []
	 	for url in list_url:
	 		new_url_list.append(url[8:])
	 	return new_url_list

	 def extract_urls_main(self):
	 	status_code = self.make_request()
	 
	 	if status_code == 200:
	 		try:
	 			urls_list = self.get_urls()
	 			new_url_list = self.clean_urls(urls_list)
	 			return new_url_list
	 		except Exception as e:
	 			print(f"Failed scraping!; ERROR : {e}")
