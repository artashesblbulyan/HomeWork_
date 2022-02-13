import requests
import os
import pprint
import json
import threading
import re
import sys
from bs4 import BeautifulSoup as BSHTML


class UrlImage:
    def __init__(self, json_file):
        self.image_list = []
        # self.image_name_list = []
        self.json_file = json_file

    def reads_json_file(self):
        try:
            if os.path.exists(self.json_file):
                with open(self.json_file, "r") as image_list_json:
                    data = json.load(image_list_json)
                    for i in data:
                        if requests.get(i['url']).status_code == 200:
                            self.image_list.append(i)
                    return self.image_list
            else:
                return self.image_list
        except requests.exceptions.ConnectionError as err:
            return f"ConnectionError{err}"
        except FileNotFoundError:
            return "FileNotFoundError"

    def finds_url(self, text_url):
        """
        function returns as argument text returns all
        URLs that contain an image in the LIST
        """
        data = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text_url)
        # soup = BSHTML(text_url)
        # images = soup.findAll('img')
        # for image in images:
        #     print(image['src'])
        j = 0
        for i in data:
            if ".jpg" in i or ".png" in i or ".jpeg" in i:
                j += 1
                self.image_list.append({'name': f'name_{j}', 'url': i})
            else:
                continue
        return self.image_list

    def reads_file(self, url_page):
        """
        The function takes the site url as an argument
        finds all site urls, returns a check
        all URLs that belong to the image
        """
        try:
            page_text = self.finds_url(requests.get(url_page).text)
            return page_text
        except requests.exceptions.ConnectionError as err:
            return f"ConnectionError{err}"

    def downloads_jpeg_image(self, name):
        try:
            for img_lit in self.image_list:
                if img_lit.get('name') == name and (".jpg" in img_lit.get("url") or ".jpeg" in img_lit.get("url")):
                    with open(f"a//{name}.jpg", "wb") as image_jpg:
                        if requests.get(img_lit.get('url')).status_code == 200:
                            image_jpg.write(requests.get(img_lit.get("url")).content)
                elif img_lit.get('name') == name and (".png" in img_lit.get("url")):
                    with open(f"a//{name}.png", "wb") as image_jpg:
                        if requests.get(img_lit.get('url')).status_code == 200:
                            image_jpg.write(requests.get(img_lit.get("url")).content)
                else:
                    continue
                    # return f"There is no image with that {name} in file.json"
        except requests.exceptions.ConnectionError as err:
            return "ConnectionError"

    def url_in_file(self, url, file_name):
        """
        Adds urls of all site image to JSON file
        """
        try:
            if requests.get(url).status_code == 200:
                data = self.reads_file(url)
                with open(file_name, "w") as file_:
                    json.dump(data, file_, indent=4)
        except requests.exceptions.ConnectionError:
            print('error')

    def download_all_pictures(self):
        """
        downloads all pictures
        """
        thread_list = []
        for i in self.image_list:
            print(i)
            x = threading.Thread(target=self.downloads_jpeg_image, args=(i.get('name'),))
            thread_list.append(x)
            x.start()
        for thread in thread_list:
            thread.join()


a = UrlImage("art.json")
a.reads_json_file()
# print(a.reads_file("https://apps.apple.com/us/app/google-photos/id962194608"))
# a.downloads_jpeg_image('a_1')
# a.finds_url()
a.download_all_pictures()
# a.url_in_file(url="https://yandex.ru/images/search?text=image&stype=image&lr=10262&source=serp", file_name="art.json")

















