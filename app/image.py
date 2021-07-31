import requests
import os.path

"""
home_page = "https://books.toscrape.com/"
image_url = "../../media/cache/c7/26/c7260547c468dbe78af92cf3927c2a1c.jpg"
book_name = "thebesthistory"
dirname = "C:\\Users\\HP\\Desktop\\book_to_scrape"
"""

class Download_image:
    def __init__(self, home_page, book_name, image_url, directory):
        self.home_page = home_page
        self.book_name = book_name
        self.image_url = image_url
        self.directory = directory

    def parse_image_url(self):
        pathfile =  ""
        words = self.image_url.split("/")
        del words[0:2]

        for w in words:
            pathfile = pathfile + "/" + w
        return pathfile
        
    def create_pic_url(self, pathfile):
        pic_url = self.home_page + pathfile
        return pic_url

    def parse_book_name(self):
        filename = self.book_name.replace(" ", "").replace("\n", "") + ".png"
        return filename

    def save_img(self, filename, pic_url):
        local_path_filename = 'images' + "/" + str(self.directory) + '/' + filename
        with open(local_path_filename, 'wb') as file:
            response = requests.get(pic_url, stream=True)
    
            for block in response.iter_content(1024):
                file.write(block)

    def main_image(self):
        pathfile = self.parse_image_url()
        pic_url = self.create_pic_url(pathfile)
        filename = self.parse_book_name()

        self.save_img(filename, pic_url)


"""
download_image = Download_image(home_page, book_name, image_url, dirname)
main = download_image.main()
"""