# -*- coding: utf-8 -*-
import os 

class Config:
	def __init__(self):
		self.home_page = "https://books.toscrape.com"
		self.catalog_page = "http://books.toscrape.com/catalogue"
		self.book_page = "http://books.toscrape.com/catalogue/category/books/"
		self.header = ['title', 'category', 'product_description', 'image_url',
			'universal_product_code', 'price_including_tax', 'price_excluding_tax', 
			'number_available','review_rating']

	def get_directory_path(self):
		path = os.getcwd()
		return path

	def parse_directory_path(self, path):
	 	path = path.replace('\\', "\\\\")
	 	return path

	def main(self):
	 	path = self.get_directory_path()
	 	main_directory_path = self.parse_directory_path(path)
	 	return main_directory_path

"""
config = Config()
dirname = config.get_dirname()
config.parse_dirname(dirname)
"""
