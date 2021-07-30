import os 

class Config:

	def __init__(self):
		self.home_page = "https://books.toscrape.com"
		self.catalogue_page = "http://books.toscrape.com/catalogue"
		self.book_page = "http://books.toscrape.com/catalogue/category/books/"
		self.header = ['title', 'category', 'product_description', 'image_url',
			'universal_product_code', 'price_including_tax', 'price_excluding_tax', 
			'number_available','review_rating']

	def get_dirname(self):
		path = os.getcwd()
		return path

	def parse_dirname(self, path):
	 	og_path = path.replace('\\', "\\\\")
	 	print(og_path)
	 	return og_path

	def main(self):
	 	path = self.get_dirname()
	 	og_path = self.parse_dirname(path)
	 	return og_path

config = Config()
dirname = config.get_dirname()
config.parse_dirname(dirname)
