# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


"""class which consults the pages of a chosen category, and extracts the URL 
of the product pages of each book belonging to this category.
At the end the main method returns the list of urls retrieved.
"""
class BOOKS:

	 def __init__(self, category_name, page_list):
	 	self.catalogue_index_page = "http://books.toscrape.com/catalogue"
	 	self.category_name = category_name
	 	self.pages_list = page_list
	 	self.books_list = []

	 def make_request(self, page):
	 	try:
	 		response = requests.get(page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 	except Exception as e:
	 		error = "Failed request!; ERROR : " + str(e)
	 		print(error)

	 def parse(self, path):
	 	# parse and concat catalogue_url with ressource url
	 	book = self.catalogue_index_page + path[8:]
	 	return book

	 def get_books(self):
	 	articles_list = self.soup.find_all("article", class_="product_pod")
	 	for article in articles_list:
	 		path = article.find("div", class_="image_container").find("a")["href"]
	 		book = self.parse(path)
	 		self.books_list.append(book)
	 	return self.books_list

	 def main(self):
	 	for page in self.pages_list:
	 		self.make_request(page)
	 		self.get_books()
	 	print("There are " + str(len(self.books_list)) + " books in " + str(self.category_name) + " category.")
	 	return self.books_list


"""
urls_list = ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html']
books = BOOKS("sequential-art_5", urls_list)
books.main()
"""