import requests
from bs4 import BeautifulSoup


"""class which consults the pages of a chosen category, and extracts the URL 
of the product pages of each book belonging to this category.
At the end the main method returns the list of urls retrieved.
"""
class BOOKS:

	 def __init__(self, category_name, urls_list):
	 	self.catalogue_url = "http://books.toscrape.com/catalogue"
	 	self.category_name =category_name
	 	self.all_urls_category = urls_list
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
	 		self.get_urls()
	 	print("There are " + str(len(self.all_books_urls)) + " books in " + str(self.category_name) + " category.")
	 	return self.all_books_urls


"""
urls_list = ['http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-2.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-3.html', 
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/page-4.html']
main = Get_all_urls_books("sequential-art_5", urls_list)
main.main()
"""