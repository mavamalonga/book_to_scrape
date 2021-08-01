# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


"""class which consults the pages of a chosen category, and extracts the URL 
of the product pages of each book belonging to this category.
At the end the main method returns the list of urls retrieved.
"""
class Books:

	 def __init__(self, category_name, list_pages, catalog_index_page):
	 	self.catalog_index_page = catalog_index_page
	 	self.category_name = category_name
	 	self.list_pages = list_pages
	 	self.list_urls_books = []

	 def make_request(self, page):
	 	try:
	 		response = requests.get(page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 	except Exception as e:
	 		error = "Failed request!; ERROR : " + str(e)
	 		print(error)

	 def parse_path(self, path):
	 	# parse and concat catalogue_url with ressource url
	 	url_book = self.catalog_index_page + path[8:]
	 	return url_book

	 def get_books_path(self):
	 	list_articles = self.soup.find_all("article", class_="product_pod")
	 	for article in list_articles:
	 		path = article.find("div", class_="image_container").find("a")["href"]
	 		url_book = self.parse_path(path)
	 		self.list_urls_books.append(url_book)

	 def main(self):
	 	for page in self.list_pages:
	 		self.make_request(page)
	 		self.get_books_path()
	 	print("There are " + str(len(self.list_urls_books)) + " books in " + str(self.category_name) + " category.")
	 	return self.list_urls_books

"""
urls_list = ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html']
catalogue_page = "https://books.toscrape.com"
books = Books("sequential-art_5", urls_list, catalogue_page)
books.main()
"""