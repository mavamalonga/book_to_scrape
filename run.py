# -*- coding: utf-8 -*-
import timeit
from app.catalogue import CATALOGUE
from app.category import CATEGORIES
from app.book import BOOKS
from app.page_content import PAGE_CONTENT


def main():
	start = timeit.default_timer()

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

	stop = timeit.default_timer()
	print('[Finished in ' + (stop - start)/60 + "m]"   


if __name__ == '__main__':
	main()