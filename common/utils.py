import requests
import os
import urllib.request
import urllib
import imghdr
import posixpath
import re

from googletrans import Translator
from difflib import SequenceMatcher


def get_translate(text, src, dest):
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text


class Bing:
    def __init__(self, query, limit=10, output_dir=None, adult=False, timeout=5, filters=''):
        self.download_count = 0
        self.query = query
        self.output_dir = output_dir
        self.adult = adult
        self.filters = filters

        assert type(limit) == int, "limit must be integer"
        self.limit = limit
        assert type(timeout) == int, "timeout must be integer"
        self.timeout = timeout

        self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.page_counter = 0
        self.__links = []
        self.__find_links()

    @property
    def links(self):
        return self.__links

    def save_image(self, link, file_path):
        request = urllib.request.Request(link, None, self.headers)
        image = urllib.request.urlopen(request, timeout=self.timeout).read()
        if not imghdr.what(None, image):
            print('[Error]Invalid image, not saving {}\n'.format(link))
            raise
        with open(file_path, 'wb') as f:
            f.write(image)

    def download_image(self, link):
        try:
            path = urllib.parse.urlsplit(link).path
            filename = posixpath.basename(path).split('?')[0]
            file_type = filename.split(".")[-1]
            if file_type.lower() not in ["jpe", "jpeg", "jfif", "exif", "tiff", "gif", "bmp", "png", "webp", "jpg"]:
                file_type = "jpg"

            print(f"[%] Downloading Image #{self.download_count} from {link}")

            self.save_image(
                link,
                f"{os.getcwd()}/{self.output_dir}/{self.query}/Image_{self.download_count}.{file_type}"
            )

            print("[%] File Downloaded !\n")
        except Exception as e:
            print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))

    def __find_links(self):
        while len(self.__links) < self.limit:
            request_url = (
                f"https://www.bing.com/images/async?q="
                f"{urllib.parse.quote_plus(self.query)}&first={str(self.page_counter)}&count={str(self.limit)}&adlt="
                f"{'on' if self.adult else 'off'}&qft={self.filters}"
            )

            request = urllib.request.Request(request_url, None, headers=self.headers)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf8')
            for item in re.findall('murl&quot;:&quot;(.*?)&quot;', html):
                try:
                    r = requests.get(item, timeout=10)
                    if r.status_code == 200 and not self.__find_similar_link(item):
                        if len(self.__links) >= self.limit:
                            return
                        self.__links.append(item)
                except Exception as e:
                    raise e

            self.page_counter += 1

    def __find_similar_link(self, link):
        for item in self.__links:
            similarity = SequenceMatcher(None, link, item).ratio()
            if similarity > 0.7:
                return True

        else:
            return False


class Image:
    """
    find image from engine
    if use bing engine command for example is
       Image("bing", {"query": "star wars last jedi", "limit": 5}).find_images_link()
    """
    def __init__(self, engine, params):
        self.__engine = engine
        self.__params = params

    def find_images_link(self):
        """
        self.params sample for bing engine
            {
              "query": "star wars last jedi",
              "limit": 5
            }
        """
        if str(self.__engine).lower() == "bing":
            return Bing(**self.__params).links
