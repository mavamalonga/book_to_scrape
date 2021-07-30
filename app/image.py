import requests
import os.path

home_page = "https://books.toscrape.com/"
url = "media/cache/6d/41/6d418a73cc7d4ecfd75ca11d854041db.jpg"
book_name = "thebesthistory"
dirname = "C:\\Users\\HP\\Desktop\\book_to_scrape"


class Download_image:
    def __init__(self, home_page, book_name, url, dirname):
        os.chdir(dirname)
        self.home_page = home_page
        self.book_name = book_name
        self.url = url

    def concat(self):
        pic_url = home_page + str(self.url)
        return pic_url

    def main(self):
        pic_url = self.concat()
        filename = self.book_name + ".png"

        path_filename = os.path.join('images', filename)
        with open(path_filename, 'wb') as file:
            response = requests.get(pic_url, stream=True)
    
            for block in response.iter_content(1024):
                file.write(block)


download_image = Download_image(home_page, book_name, url, dirname)
main = download_image.main()