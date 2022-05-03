from bs4 import BeautifulSoup
import requests

def check_website(url):
    page = requests.get(url)
    print(page.status_code)
    if page.status_code == 200:
        return True
    else:
        return False
def get_all_tag(page):
    soup = BeautifulSoup(page.text, "html.parser")
    tag_list = []
    for tag in soup.findAll(True):
        tag_list.append(tag.name)
    # print(list(set(tag_list)))
    return list(set(tag_list))

def get_element(url,tag):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    el_list = soup.findAll(tag)
    return el_list

if __name__ == "__main__":

    print( get_element("https://habr.com/ru/post/544828/","a"))