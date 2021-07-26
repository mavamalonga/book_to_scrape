import requests
from bs4 import BeautifulSoup
import csv


"""extract all the links of the products of a category"""
class Get_all_urls_books:

	 def __init__(self, url):
	 	self.catalogue_url = "http://books.toscrape.com/catalogue"
	 	self.all_urls_category = url
	 	self.all_books_urls = []

	 def make_request(self, category_page_n):
	 	try:
	 		response = requests.get(category_page_n)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 	except Exception as e:
	 		print(f"Failed request!; ERROR : {e}")

	 def parse_url(self, url):
	 	# parse and concat catalogue_url with ressource url
	 	clear_url = self.catalogue_url + url[8:]
	 	return clear_url


	 def get_urls(self):
	 	articles_list = self.soup.find_all("article", class_="product_pod")
	 	for article in articles_list:
	 		url = article.find("div", class_="image_container").find("a")["href"]
	 		parse_url = self.parse_url(url)
	 		self.all_books_urls.append(parse_url)
	 	return self.all_books_urls

	 def main(self):
	 	for category_page_n in self.all_urls_category:
	 		self.make_request(category_page_n)
	 		urls = self.get_urls()
	 	return f"{len(self.all_books_urls)} : pounds recovered"



url = ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html']
main = Get_all_urls_books(url)
print(main.main())