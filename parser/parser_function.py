from bs4 import BeautifulSoup
import requests
import schedule
import time



class ParserContainer():
    def __init__(self, url="https://www.google.com/search?q=%D0%B2%D1%80%D0%B5%D0%BC%D1%8F&oq=%D0%B2%D1%80%D0%B5%D0%BC%D1%8F&aqs=chrome..69i57j69i59j69i61l3.1322j0j15&sourceid=chrome&ie=UTF-8"):
        self.url = url
        self.tag_list = []
        self.class_list = []
        self.id_list = []
        self.current_tag = None
        self.current_class = None
        self.current_id = None
        self.content_list = []
        self.action = None
        self.action_value = None
        self.mark = None

    def get_all_tag(self):
        if self.url is not None:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            self.tag_list = []
            for tag in soup.findAll(True):
                self.tag_list.append(tag.name)
            self.tag_list = list(set(self.tag_list))
            self.tag_list.sort()

    def get_all_class(self):
        if self.url is not None:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            self.class_list = set()
            tags = {tag.name for tag in soup.find_all()}
            for tag in tags:
                for i in soup.find_all(tag):
                    if i.has_attr("class"):
                        if len(i['class']) != 0:
                            self.class_list.add(" ".join(i['class']))
        self.class_list = list(self.class_list)

    def get_all_id(self):
        if self.url is not None:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            self.id_list = set()
            tags = {tag.name for tag in soup.find_all()}
            for tag in tags:
                for i in soup.find_all(tag):
                    if i.has_attr("id"):
                        if len(i['id']) != 0:
                            self.id_list.add(" ".join(i['id']))
        self.id_list = list(self.id_list)

    def find_content_by_type(self):
        if self.url is not None:
            page = requests.get(self.url)
            soup = BeautifulSoup(page.text, "html.parser")
            self.content_list = []
            content = None
            content = soup.find_all(self.current_tag, class_=self.current_class, id=self.current_id)
            for i in content:
                self.content_list.append(i.text)

a = ParserContainer()
a.current_class = "BNeawe iBp4i AP7Wnd"
# a.current_class = "bookmark-text-add"
a.find_content_by_type()
print(a.content_list)
# a.get_all_class()
# print(a.class_list)
# url = "https://yandex.ru/time"
# page = requests.get(url)
# soup = BeautifulSoup(page.text, "html.parser")
# content = soup.find_all(None, class_="digital-clock__seconds",id = None)
# print(content)
