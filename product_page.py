import requests
from bs4 import BeautifulSoup
import csv

"""
product_page_url #
universal_ product_code (upc) #
title #
price_including_tax #
price_excluding_tax #
number_available #
product_description #
category #
review_rating #
image_url #
"""

def get_table_information():

	product_page_url = "http://books.toscrape.com/catalogue/night-shift-night-shift-1-20_335/index.html"
	page = requests.get(product_page_url)
	soup = BeautifulSoup(page.content, 'html.parser')


	table_striped = soup.find_all("table", class_="table table-striped")
	tds = table_striped[0].find_all("td")

	universal_product_code = tds[0].string
	price_including_tax = tds[3].string
	price_excluding_tax = tds[2].string
	number_available = tds[5].string
	review_rating = tds[-1].string


def get_header_information():
	product_page_url = "http://books.toscrape.com/catalogue/night-shift-night-shift-1-20_335/index.html"
	page = requests.get(product_page_url)
	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find("title").string
	balise_product_description = soup.find(attrs={"name":"description"})
	product_decription = balise_product_description['content']

	div_product_gallery = soup.find("div", id="product_gallery")
	image_url = div_product_gallery.find("img")["src"]


	block_ul = soup.find("ul", class_="breadcrumb")
	block_all_a = block_ul.find_all("a")
	category = block_all_a[-1].string
	print(category)



get_header_information()



