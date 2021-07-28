# -*- coding: utf-8 -*-
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
	for category_name, category_index_url in categories_list:

		categories = CATEGORIES(category_name, category_index_url)
		other_pages_urls = categories.main()

		book = BOOKS(category_name, other_pages_urls)
		all_book_urls = book.main()

		page_content = PAGE_CONTENT(category_name, all_book_urls)
		page_content.main()

	print("The scraping of the booktoscrap website was a success.")


if __name__ == '__main__':
	main()