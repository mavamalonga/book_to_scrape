import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# get all titles
titles = soup.find_all("a", class_="gem-c-document-list__item-link")
title_texts = []
for title in titles:
	title_texts.append(title.string)

#get all descriptions
descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")
descriptions_texts = []
for description in descriptions:
	descriptions_texts.append(description.string)

# write titles and descriptions in csv file 
en_tete = ['title', 'description']
with open('data.csv', 'w') as csv_file:
	writer = csv.writer(csv_file, delimiter=',')
	writer.writerow(en_tete)
	for title, description in zip(title_texts, descriptions_texts):
		print(f"{title},{description}")
		writer.writerow([title, description])


