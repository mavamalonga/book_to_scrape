from catalogue import CATALOGUE
from category import CATEGORIES
from book import BOOKS
from page_content import PAGE_CONTENT

def main():
	url = "https://books.toscrape.com"
	catalogue = CATALOGUE(url)
	categories_list = catalogue.main()

	# deletion of the first value which corresponds to the list of all books
	del categories_list[0]
	for category_index_url in categories_list:
		categories = CATEGORIES(category_index_url)
		category_all_pages_urls = categories.main()
		print(categories_all_pages_urls)
		


if __name__ == '__main__':
	main()