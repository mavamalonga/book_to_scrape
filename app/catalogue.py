# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""class consults the catalog page of the BooktoScrape.com website and 
retrieves all the index category page urls.
The main method returns the urls list of all the pages index category.
"""
class Catalogue:

	 def __init__(self, home_page):
	 	self.home_page = home_page
	 	self.list_urls_categories = []

	 def make_request(self):
	 	try:
	 		response = requests.get(self.home_page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 	except Exception as e:
	 		error = "Failed request!; ERROR" + str(e)
	 		print(error)

	 def concat_path(self, href):
	 	url_category = str(self.home_page) + "/" + str(href)
	 	return url_category

	 def get_categories_urls(self):
	 	side_categories = self.soup.find("div", class_="side_categories")
	 	nav_list = side_categories.find("ul", class_="nav nav-list")
	 	li_list = nav_list.find_all("li")

	 	for path in li_list:
	 		category_name = path.find("a").string.replace("\n", "").replace(" ", "")
	 		url_category = self.concat_path(path.find("a")["href"])
	 		self.list_urls_categories.append((category_name, url_category))

	 def main(self):
	 	self.make_request()
	 	self.get_categories_urls()
	 	print("The BooktoScrape has " + str(len(self.list_urls_categories)) + " book categories.")
	 	return self.list_urls_categories

"""
home_page = "https://books.toscrape.com"
catalogue = Catalogue(home_page)
main = catalogue.main()
print(main)
"""