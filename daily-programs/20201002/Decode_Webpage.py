import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"
r = requests.get(url).text

soup = BeautifulSoup(r,'lxml')

for article in soup.find_all("article"):
    headline = article.h2
    try:
        print(headline.get_text())
    except Exception as e:
        print(None)

