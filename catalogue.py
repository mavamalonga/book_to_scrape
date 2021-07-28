import requests
from bs4 import BeautifulSoup


"""class consults the catalog page of the BooktoScrape.com website and 
retrieves all the index category page urls.
The main method returns the urls list of all the pages index category.
"""
class CATALOGUE:

	 def __init__(self, home_page):
	 	self.home_page = home_page
	 	self.categories_list = []

	 def make_request(self):
	 	try:
	 		response = requests.get(self.home_page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 	except Exception as e:
	 		error = "Failed request!; ERROR" + str(e)
	 		print(error)

	 def concat(self, href):
	 	category = str(self.home_page) + "/" + str(href)
	 	return category

	 def get_categories(self):
	 	side_categories = self.soup.find("div", class_="side_categories")
	 	nav_list = side_categories.find("ul", class_="nav nav-list")
	 	li_list = nav_list.find_all("li")

	 	for path in li_list:
	 		category_name = path.find("a").string.replace("\n", "").replace(" ", "")
	 		category = self.concat(path.find("a")["href"])
	 		self.categories_list.append((category_name, category))

	 def main(self):
	 	self.make_request()
	 	self.get_categories()
	 	print("The BooktoScrape has " + str(len(self.categories_list)) + " book categories.")
	 	return self.categories_list


"""
home_page = "https://books.toscrape.com"
catalogue = CATALOGUE(home_page)
main = catalogue.main()
print(main)
"""

