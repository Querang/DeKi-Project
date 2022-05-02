from bs4 import BeautifulSoup
import requests

url = 'https://bik.sfu-kras.ru/elib/view?id=BOOK1-84%284%D0%90%29-444/%D0%9C%20805-521870'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
print(soup.find_all('li'))