import requests
from bs4 import BeautifulSoup


"""class consults the catalog page of the BooktoScrape.com website and 
retrieves all the index category page urls.
The main method returns the urls list of all the pages index category.
"""
class CATALOGUE:

	 def __init__(self, url):
	 	self.url_catalogue_index_page = url
	 	self.urls_list = []

	 def make_request(self):
	 	try:
	 		response = requests.get(self.url_catalogue_index_page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 	except Exception as e:
	 		print("Failed request!; ERROR" + str(e))

	 def concat(self, path_index_page):
	 	entire_url = str(self.url_catalogue_index_page) + "/" + str(path_index_page)
	 	return entire_url

	 def get_all_index_category_page(self):
	 	side_categories = self.soup.find("div", class_="side_categories")
	 	nav_list = side_categories.find("ul", class_="nav nav-list")
	 	all_li_list = nav_list.find_all("li")

	 	for path_index_page in all_li_list:
	 		category_name = path_index_page.find("a").string.replace("\n", "").replace(" ", "")
	 		category_url = self.concat(path_index_page.find("a")["href"])
	 		self.urls_list.append((category_name, category_url))
	 	return self.urls_list

	 def main(self):
	 	self.make_request()
	 	self.get_all_index_category_page()
	 	print("The BooktoScrape has " + str(len(self.urls_list)) + " book categories.")
	 	return self.urls_list


"""
catalogue = Get_all_category_urls("https://books.toscrape.com")
catalogue.main()
"""

