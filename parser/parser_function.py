from bs4 import BeautifulSoup
import requests


class ParserContainer():
    def __init__(self, url="https://bik.sfu-kras.ru/elib/view?id=BOOK1-84%284%D0%90%29-444/%D0%9C%20805-521870"):
        self.url = url
        self.tag_list = []
        self.class_list = []
        self.id_list = []
        self.current_tag = "..."
        self.current_class = "..."
        self.current_id = "..."
        self.content_list = []

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
            if self.current_tag != "...":
                content = soup.find_all(tag=self.current_tag)
                if self.current_class != "...":
                    content = soup.find_all(tag=self.current_tag, class_=self.current_class)
                    if self.current_id != "...":
                        content = soup.find_all(tag=self.current_tag, class_=self.current_class, id=self.current_id)
            else:
                if self.current_class != "...":
                    content = soup.find_all(class_=self.current_class)
                    if self.current_id != "...":
                        content = soup.find_all(class_=self.current_class, id=self.current_id)
                else:
                    if self.current_id != "...":
                        content = soup.find_all(id=self.current_id)

            for i in content:
                self.content_list.append(i.text)


# a = ParserContainer()
# a.find_element()
# a.get_all_class()
# print(a.class_list)
url = "https://bik.sfu-kras.ru/elib/view?id=BOOK1-84%284%D0%90%29-444/%D0%9C%20805-521870"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
content = soup.find_all(None, class_='list',id = None)
print(content)