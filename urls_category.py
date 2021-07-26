import requests
from bs4 import BeautifulSoup
import csv


"""extract all the links of the products of a category"""
class Get_urls_category_page:

	 def __init__(self, url):
	 	self.category_page_url = url
	 	self.main_url = "http://books.toscrape.com/catalogue/category/books/"
	 	self.next_page_url = None
	 	self.url_page_list = []

	 def add_to_page_url_list(self):
	 	self.url_page_list.append(self.category_page_url)
	 	print(self.url_page_list)
	 	return self.url_page_list

	 def make_request(self):
	 	try:
	 		response = requests.get(self.category_page_url)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 		print(f"Request successful!; status_code : {response.status_code}")
	 		return response.status_code
	 	except Exception as e:
	 		print(f"Failed request!; ERROR : {e}")
	 		return None

	 def get_next_page_url(self):
	 	try:
	 		next_page = self.soup.find("ul", class_="pager").find("li", class_="next").find("a")["href"]
	 		if next_page is not None:
	 			category = self.category_page_url[51:].split("/")[0]
	 			next_page_url = f"{self.main_url}{category}/{next_page}"
	 			return next_page_url
	 	except Exception as e:
	 		return None

	 def main(self):
	 	self.make_request()
	 	self.add_to_page_url_list()
	 	self.next_page_url = self.get_next_page_url()

	 	while self.next_page_url is not None:
	 		self.category_page_url = self.next_page_url
	 		self.make_request()
	 		self.add_to_page_url_list()
	 		self.next_page_url = self.get_next_page_url()





url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
main = Extract_urls(url)
main.main()