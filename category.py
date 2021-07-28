# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


"""class consults the chosen category page, 
and checks if the category is multi-page and retrieves the other URLs.
The main method returns the urls list of all the pages in the category."""
class CATEGORIES:

	 def __init__(self, category_name, index_page):
	 	self.category_name = category_name
	 	self.index_page = index_page
	 	self.root_path = "http://books.toscrape.com/catalogue/category/books/"
	 	self.pages_list = []

	 def make_request(self, page):
	 	try:
	 		response = requests.get(page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 		self.pages_list.append(page)
	 	except Exception as e:
	 		error = "Failed request!; ERROR" + str(e)
	 		print(error)
	 		return None

	 def get_collection_value(self):
	 	self.collection = self.index_page.split("/")
	 	del self.collection[0:6]
	 	return self.collection[0]

	 def get_next_page(self, collection_name):
	 	try:
	 		href = self.soup.find("ul", class_="pager").find("li", class_="next").find("a")["href"]
	 		if href is not None:
	 			next_page = self.root_path + str(collection_name) + "/" + str(href)
	 			return next_page
	 	except Exception as e:
	 		error = "No next page; ERROR: " + str(e)
	 		#print(error) 

	 def main(self):
	 	self.make_request(self.index_page)
	 	self.collection_name = self.get_collection_value()
	 	self.next_page = self.get_next_page(self.collection_name)

	 	while self.next_page is not None:
	 		self.make_request(self.next_page)
	 		self.next_page = self.get_next_page(self.collection_name)

	 	print("The are " + str(len(self.pages_list)) + " pages in the " + str(self.category_name) + " category.")
	 	return self.pages_list


"""
url = "https://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html"
category_name = "sequential-art"
categories = CATEGORIES(category_name, url)
main = categories.main()
print(main)
"""