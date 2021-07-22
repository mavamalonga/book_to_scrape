from product_page import Extract_content
from category_page import Extract_urls

class Book_to_scrape(Extract_urls, Extract_content):

	def __init__(self, page_url):
		Extract_urls.__init__(self, page_url)
		self.category_page_url = "http://books.toscrape.com/catalogue/"

	def call_extract_urls(self):
		urls_list = self.extract_urls_main()
		return urls_list 

	def call_extract_content(self, urls_list):
		Extract_content.__init__(self, urls_list)

	def concat_url(self, urls_list):
		new_urls_list = []
		for url in urls_list:
			new_urls_list.append("'" +  self.category_page_url + url + "'")
		return new_urls_list

	def book_to_scrape_main(self):
		urls_list = self.call_extract_urls()
		print(urls_list)

if __name__ == '__main__':
	book_to_scrape = Book_to_scrape(
		"http://books.toscrape.com/catalogue/category/books/health_47/index.html")
	book_to_scrape.book_to_scrape_main()
