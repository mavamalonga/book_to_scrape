from product_page import Extract_content
from category_page import Extract_urls


def call_extract_urls(page_url):
	extract_urls = Extract_urls(page_url)
	urls_list = extract_urls.extract_urls_main()
	return urls_list

def check_next_page(url):
	extract_urls = Extract_urls(url)
	next_page = extract_urls.next_page()
	return next_page

def concat_url(category_page_url, urls_list):
	new_urls_list = []
	for url in urls_list:
		new_urls_list.append(f"{category_page_url}{url}")
	return new_urls_list

def call_extract_content(urls_list):
	extract_content = Extract_content(urls_list)
	extract_content.main()

def main(url):
	urls_list = call_extract_urls(url)
	new_urls_list = concat_url("http://books.toscrape.com/catalogue", urls_list)
	call_extract_content(new_urls_list)

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/page-1.html"
main(url)





"""
class Book_to_scrape(Extract_urls, Extract_content):

	def __init__(self, page_url):
		Extract_urls.__init__(self, page_url)
		self.category_page_url = "http://books.toscrape.com/catalogue/"

	def call_extract_urls(self):
		urls_list = self.extract_urls_main()
		return urls_list 

	http://books.toscrape.com/catalogue/the-death-of-humanity-and-the-case-for-life_932/index.html

	def concat_url(self, urls_list):
		new_urls_list = []
		for url in urls_list:
			new_urls_list.append("'" +  self.category_page_url + url + "'")
		return new_urls_list

	def main(self):
		urls_list = self.call_extract_urls()
		print(urls_list)

if __name__ == '__main__':
	book_to_scrape = Book_to_scrape(
		"http://books.toscrape.com/catalogue/category/books/health_47/index.html")
	book_to_scrape.main()
"""