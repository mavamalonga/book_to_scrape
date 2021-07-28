# -*- coding: utf-8 -*-
import requests
import csv
import os.path
from bs4 import BeautifulSoup

"""class which visits all the product pages of a category from 
the list of urls it receives and retrieves the following information :
	- product_page_url
	- universal_product_code
	- title
	- price_including_tax
	- price_excluding_tax
	- category
	- review_rating
	- image_url
At the end the information is saved in a csv file.
"""
class PAGE_CONTENT:

	def __init__(self, category_name, books_list):
		self.category_name = category_name
		self.books_list = books_list
		self.data_list = []
		self.header = ['title', 'category', 'product_description', 'image_url',
			'universal_product_code', 'price_including_tax', 'price_excluding_tax', 
			'number_available','review_rating']

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
		return number_available

	def get_review_rating(self):
		review_rating = self.tds[-1].string
		return review_rating

	def call_methods(self):
		self.data_list.append([self.get_title(), self.get_category(), self.get_description(), 
			self.get_image_url(), self.get_UPC(), self.get_price_including_tax(), 
			self.get_price_excluding_tax(), self.get_number_available(), 
			self.get_review_rating()])

	def write_data(self):
		file_name = self.category_name + ".csv"
		try:
			complete_name = os.path.join('csv/', file_name)
			with open(complete_name, 'w', encoding="utf-8") as csv_file:
				writer = csv.writer(csv_file, delimiter=',')
				writer.writerow(self.header)

				for data in self.data_list:
					writer.writerow([data[0], data[1], data[2], 
					data[3], data[4], data[5], data[6],
					data[7], data[8]])

				print("writing of " + file_name + " file finished")
		except Exception as e:
			error = "writing in the csv file failed; ERROR : " + str(e)
			print(e)
	
	def main(self):
		for book in self.books_list:
			self.make_request(book)
			self.call_methods()
		
		self.write_data()

"""
books_list = ['http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html', 'http://books.toscrape.com/catalogue/tsubasa-world-chronicle-2-tsubasa-world-chronicle-2_949/index.html', 'http://books.toscrape.com/catalogue/this-one-summer_947/index.html', 
'http://books.toscrape.com/catalogue/the-nameless-city-the-nameless-city-1_940/index.html', 'http://books.toscrape.com/catalogue/saga-volume-5-saga-collected-editions-5_923/index.html', 'http://books.toscrape.com/catalogue/rat-queens-vol-3-demons-rat-queens-collected-editions-11-15_921/index.html', 'http://books.toscrape.com/catalogue/princess-jellyfish-2-in-1-omnibus-vol-01-princess-jellyfish-2-in-1-omnibus-1_920/index.html', 'http://books.toscrape.com/catalogue/pop-gun-war-volume-1-gift_918/index.html', 'http://books.toscrape.com/catalogue/patience_916/index.html', 'http://books.toscrape.com/catalogue/outcast-vol-1-a-darkness-surrounds-him-outcast-1_915/index.html', 'http://books.toscrape.com/catalogue/orange-the-complete-collection-1-orange-the-complete-collection-1_914/index.html', 'http://books.toscrape.com/catalogue/lumberjanes-vol-2-friendship-to-the-max-lumberjanes-5-8_907/index.html', 'http://books.toscrape.com/catalogue/lumberjanes-vol-1-beware-the-kitten-holy-lumberjanes-1-4_906/index.html', 'http://books.toscrape.com/catalogue/lumberjanes-vol-3-a-terrible-plan-lumberjanes-9-12_905/index.html', 'http://books.toscrape.com/catalogue/i-hate-fairyland-vol-1-madly-ever-after-i-hate-fairyland-compilations-1-5_899/index.html', 'http://books.toscrape.com/catalogue/i-am-a-hero-omnibus-volume-1_898/index.html', 'http://books.toscrape.com/catalogue/giant-days-vol-2-giant-days-5-8_895/index.html', 'http://books.toscrape.com/catalogue/danganronpa-volume-1_889/index.html', 'http://books.toscrape.com/catalogue/codename-baboushka-volume-1-the-conclave-of-death_887/index.html', 'http://books.toscrape.com/catalogue/camp-midnight_886/index.html', 'http://books.toscrape.com/catalogue/bitch-planet-vol-1-extraordinary-machine-bitch-planet-collected-editions_882/index.html', 'http://books.toscrape.com/catalogue/the-shadow-hero-the-shadow-hero_860/index.html', 'http://books.toscrape.com/catalogue/fables-vol-1-legends-in-exile-fables-1_806/index.html', 'http://books.toscrape.com/catalogue/batman-the-long-halloween-batman_793/index.html', 'http://books.toscrape.com/catalogue/batman-the-dark-knight-returns-batman_792/index.html', 'http://books.toscrape.com/catalogue/wonder-woman-earth-one-volume-one-wonder-woman-earth-one-1_783/index.html', 'http://books.toscrape.com/catalogue/we-are-robin-vol-1-the-vigilante-business-we-are-robin-1_778/index.html', 'http://books.toscrape.com/catalogue/through-the-woods_772/index.html', 'http://books.toscrape.com/catalogue/superman-vol-1-before-truth-superman-by-gene-luen-yang-1_739/index.html', 'http://books.toscrape.com/catalogue/so-cute-it-hurts-vol-6-so-cute-it-hurts-6_734/index.html', 'http://books.toscrape.com/catalogue/robin-war_730/index.html', 'http://books.toscrape.com/catalogue/red-hoodarsenal-vol-1-open-for-business-red-hoodarsenal-1_729/index.html', 'http://books.toscrape.com/catalogue/naruto-3-in-1-edition-vol-14-includes-vols-40-41-42-naruto-omnibus-14_721/index.html', 'http://books.toscrape.com/catalogue/lowriders-to-the-center-of-the-earth-lowriders-in-space-2_712/index.html', 'http://books.toscrape.com/catalogue/el-deafo_691/index.html', 'http://books.toscrape.com/catalogue/batman-europa_668/index.html', 'http://books.toscrape.com/catalogue/art-ops-vol-1_664/index.html', 'http://books.toscrape.com/catalogue/adulthood-is-a-myth-a-sarahs-scribbles-collection_659/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-9-fruits-basket-9_563/index.html', 'http://books.toscrape.com/catalogue/roller-girl_540/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-7-fruits-basket-7_468/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-6-fruits-basket-6_427/index.html', 'http://books.toscrape.com/catalogue/death-note-vol-6-give-and-take-death-note-6_425/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-5-fruits-basket-5_376/index.html', 'http://books.toscrape.com/catalogue/death-note-vol-5-whiteout-death-note-5_368/index.html', 'http://books.toscrape.com/catalogue/the-demon-prince-of-momochi-house-vol-4-the-demon-prince-of-momochi-house-4_344/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-4-fruits-basket-4_321/index.html', 'http://books.toscrape.com/catalogue/the-wicked-the-divine-vol-3-commercial-suicide-the-wicked-the-divine_287/index.html', 'http://books.toscrape.com/catalogue/the-sandman-vol-3-dream-country-the-sandman-volumes-3_279/index.html', 'http://books.toscrape.com/catalogue/saga-volume-3-saga-collected-editions-3_216/index.html', 'http://books.toscrape.com/catalogue/prodigy-the-graphic-novel-legend-the-graphic-novel-2_207/index.html', 'http://books.toscrape.com/catalogue/persepolis-the-story-of-a-childhood-persepolis-1-2_206/index.html', 'http://books.toscrape.com/catalogue/original-fake_203/index.html', 'http://books.toscrape.com/catalogue/grayson-vol-3-nemesis-grayson-3_164/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-3-fruits-basket-3_159/index.html', 'http://books.toscrape.com/catalogue/black-butler-vol-1-black-butler-1_130/index.html', 'http://books.toscrape.com/catalogue/awkward_124/index.html', 'http://books.toscrape.com/catalogue/the-sandman-vol-2-the-dolls-house-the-sandman-volumes-2_110/index.html', 'http://books.toscrape.com/catalogue/saga-volume-2-saga-collected-editions-2_107/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-2-fruits-basket-2_100/index.html', 'http://books.toscrape.com/catalogue/y-the-last-man-vol-1-unmanned-y-the-last-man-1_98/index.html', 'http://books.toscrape.com/catalogue/the-wicked-the-divine-vol-1-the-faust-act-the-wicked-the-divine_86/index.html', 'http://books.toscrape.com/catalogue/the-sandman-vol-1-preludes-and-nocturnes-the-sandman-volumes-1_79/index.html', 'http://books.toscrape.com/catalogue/the-complete-maus-maus-1-2_62/index.html', 'http://books.toscrape.com/catalogue/skip-beat-vol-01-skip-beat-1_55/index.html', 'http://books.toscrape.com/catalogue/saga-volume-1-saga-collected-editions-1_48/index.html', 'http://books.toscrape.com/catalogue/rat-queens-vol-1-sass-sorcery-rat-queens-collected-editions-1-5_46/index.html', 'http://books.toscrape.com/catalogue/paper-girls-vol-1-paper-girls-1-5_44/index.html', 'http://books.toscrape.com/catalogue/ouran-high-school-host-club-vol-1-ouran-high-school-host-club-1_43/index.html', 'http://books.toscrape.com/catalogue/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html', 'http://books.toscrape.com/catalogue/hawkeye-vol-1-my-life-as-a-weapon-hawkeye-1_24/index.html', 'http://books.toscrape.com/catalogue/giant-days-vol-1-giant-days-1-4_22/index.html', 'http://books.toscrape.com/catalogue/fruits-basket-vol-1-fruits-basket-1_21/index.html', 'http://books.toscrape.com/catalogue/bleach-vol-1-strawberry-and-the-soul-reapers-bleach-1_7/index.html', 'http://books.toscrape.com/catalogue/ajin-demi-human-volume-1-ajin-demi-human-1_4/index.html']
category_name = "sequential-art"
page_content = PAGE_CONTENT(category_name, books_list)
page_content.main()
"""