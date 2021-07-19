import requests
from bs4 import BeautifulSoup
import csv

"""
product_page_url #
universal_ product_code (upc) #
title
price_including_tax #
price_excluding_tax #
number_available #
product_description
category
review_rating #
image_ur
"""

product_page_url = "http://books.toscrape.com/catalogue/night-shift-night-shift-1-20_335/index.html"
page = requests.get(product_page_url)
soup = BeautifulSoup(page.content, 'html.parser')

def get_table_informations():
	table_striped = soup.find_all("table", class_="table table-striped")
	tds = table_striped[0].find_all("td")

	universal_product_code = tds[0].string
	price_including_tax = tds[3].string
	price_excluding_tax = tds[2].string
	number_available = tds[5].string
	review_rating = tds[-1].string



