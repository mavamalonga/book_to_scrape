import requests
from bs4 import BeautifulSoup
import csv

class Extract_page_content:

	def __init__(self, url):

		product_page_url = url
		self.header = ['title', 'category', 'product_description', 'image_url',
			'universal_product_code', 'price_including_tax', 'price_excluding_tax', 
			'number_available','review_rating']

		response = requests.get(product_page_url)
		if response.status_code == requests.codes.ok:
			self.soup = BeautifulSoup(response.content, 'html.parser')
			self.table_striped = self.soup.find_all("table", class_="table table-striped")
			self.tds = self.table_striped[0].find_all("td")

			self.request_200 = True
		else:
			self.request_200 = False
		
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

	def get_image(self):
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

	def main(self):

		if self.request_200:
			try:
				with open('data.csv', 'w') as csv_file:
					writer = csv.writer(csv_file, delimiter=',')
					writer.writerow(self.header)
					writer.writerow([self.get_title(), self.get_category(), self.get_description(), 
						self.get_image(), self.get_UPC(), self.get_price_including_tax(), self.get_price_excluding_tax(),
						self.get_number_available(), self.get_review_rating()])
				print("Extract successful !")
			except Exception as e:
				raise e
	
		else:
			print("Error; check your url value or your connection internet.")



i = Extract_page_content("http://books.toscrape.com/catalogue/join_902/index.html")
i.main()







