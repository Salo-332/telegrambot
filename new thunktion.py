from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://codingprojects.ru/login'
data = urlopen(url).read()
html = data.decode('utf-8')
parsed_html = BeautifulSoup(html, features='lxml')

print(
    parsed_html.find_all("input", class_="form-control-lg form-control")
)