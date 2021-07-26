import requests
from bs4 import BeautifulSoup


"""extract all the links of the products of a category"""
class Get_urls_category_page:

	 def __init__(self, url):
	 	self.url_page = url
	 	self.root_url = "http://books.toscrape.com/catalogue/category/books/"
	 	self.next_page_url = None
	 	self.urls_list = []

	 def make_request(self):
	 	try:
	 		response = requests.get(self.url_page)
	 		self.soup = BeautifulSoup(response.content, 'html.parser')
	 		self.urls_list.append(self.url_page)
	 	except Exception:
	 		print("Failed request!; ERROR" + str(Exception))
	 		return None

	 def parse_url(self, next_page):
	 	self.category_name = self.url_page[51:].split("/")[0]
	 	next_page_url = self.root_url + str(self.category_name) + "/" + str(next_page)
	 	return next_page_url

	 def get_next_page_url(self):
	 	try:
	 		next_page = self.soup.find("ul", class_="pager").find("li", class_="next").find("a")["href"]
	 		if next_page is not None:
	 			next_page_url = self.parse_url(next_page)
	 			return next_page_url
	 	except Exception:
	 		return None

	 def main(self):
	 	self.make_request()
	 	self.next_page_url = self.get_next_page_url()

	 	while self.next_page_url is not None:
	 		self.url_page = self.next_page_url
	 		self.make_request()
	 		self.next_page_url = self.get_next_page_url()
	 	print("The are " + str(len(self.urls_list)) + " pages in the " + str(self.category_name) + " category.")
	 	return self.category_name, self.urls_list





url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
main = Get_urls_category_page(url)
print(main.main())