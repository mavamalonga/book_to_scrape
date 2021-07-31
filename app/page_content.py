# -*- coding: utf-8 -*-
import requests
import csv
import os.path
from bs4 import BeautifulSoup
from app.image import Download_image

"""class which visits all the product pages of a category from 
the list of urls it receives and retrieves the following information :
product_page_url, universal_product_code, title, price_including_tax,
price_excluding_tax, category, review_rating, image_url.
At the end the information is saved in a csv file.
"""

class PAGE_CONTENT(Download_image):
	def __init__(self, category_name, books_list, dirname, header, home_page):
		self.dirname = dirname
		self.category_name = category_name
		self.books_list = books_list
		self.data_list = []
		self.header = header
		self.home_page = home_page
		os.chdir(self.dirname)

	def make_request(self, page):
		try:
			response = requests.get(page)
			self.soup = BeautifulSoup(response.content, 'html.parser')
			self.table_striped = self.soup.find_all("table", class_="table table-striped")
			self.tds = self.table_striped[0].find_all("td")
		except Exception as e:
			error = "Failed request!; ERROR :" + str(e)
	
	def get_title(self):
		title = self.soup.find("title").string
		title = title.split('|')[0] #parse title
		return title

	def get_category(self):
		block_ul = self.soup.find("ul", class_="breadcrumb")
		category = block_ul.find_all("a")[-1].string
		return category

	def get_description(self):
		product_description = self.soup.find(attrs={"name":"description"})["content"]
		return product_description

	def get_image_url(self):
		image_url = self.soup.find("div", id="product_gallery").find("img")["src"]
		return image_url

	def get_UPC(self):
		universal_product_code = self.tds[0].string
		return universal_product_code

	def get_price_including_tax(self):
		price_including_tax = self.tds[3].string
		return price_including_tax

	def get_price_excluding_tax(self):
		price_excluding_tax = self.tds[2].string
		return price_excluding_tax

	def get_number_available(self):
		number_available = self.tds[5].string
		# parse number available
		number_available = number_available.split()[2]
		number_available = number_available.replace("(", "").replace(")", "")
		number_available = number_available.split()[0]
		return number_available

	def get_review_rating(self):
		review_rating = self.tds[-1].string
		return review_rating

	def call_methods(self):
		self.data_list.append([self.get_title(), self.get_category(), self.get_description(), 
			self.get_image_url(), self.get_UPC(), self.get_price_including_tax(), 
			self.get_price_excluding_tax(), self.get_number_available(), 
			self.get_review_rating()])

	def create_image_category(self):
		directory = self.category_name
		parent_dir = str(self.dirname) + "//" + "images"
		path = os.path.join(parent_dir, directory)
		os.mkdir(path)

	def write_data(self):
		file_name = self.category_name + ".csv"
		self.create_image_category()
		try:
			complete_name = os.path.join('csv/', file_name)
			with open(complete_name, 'w', encoding="utf-8") as csv_file:
				writer = csv.writer(csv_file, delimiter=',')
				writer.writerow(self.header)

				for data in self.data_list:
					writer.writerow([data[0], data[1], data[2], 
					data[3], data[4], data[5], data[6],
					data[7], data[8]])
					Download_image.__init__(self, self.home_page, 
						data[0], data[3], self.category_name)
					self.main_image()

				print("writing of " + file_name + " file finished")
		except Exception as e:
			error = "writing in the csv file failed; ERROR : " + str(e)
			print(e)
	
	def main(self):
		for book in self.books_list:
			self.make_request(book)
			self.call_methods()
		
		self.write_data()
