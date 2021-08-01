# -*- coding: utf-8 -*-
import timeit
from app.catalogue import Catalogue
from app.category import Categories
from app.book import Books
from app.page_content import PAGE_CONTENT
from app.image import Download_image
from config import Config 

"""
main retrieves all modules from the app
main is the function that executes the program
"""
def main():
	start = timeit.default_timer()

	config = Config()
	dirname = config.main()
	catalogue = Catalogue(config.home_page)
	categories_list = catalogue.main()
	# deletion of the first value which corresponds to the list of all books
	del categories_list[0]

	for category_name, category_index_page in categories_list:

		categories = Categories(category_name, category_index_page, config.book_page)
		other_pages_urls = categories.main()

		book = Books(category_name, other_pages_urls, config.catalog_page)
		all_books = book.main()

		page_content = PAGE_CONTENT(category_name, all_books, dirname, config.header, config.home_page)
		page_content.main()

	stop = timeit.default_timer()
	time = (stop - start)/60
	print('[Finished in ' + str(round(time, 2)) + "m]")


if __name__ == '__main__':
	main()