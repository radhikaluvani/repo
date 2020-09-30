import requests
from bs4 import BeautifulSoup
url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html, "lxml")

for titles in soup.find_all(class_ = "story"):
	title = titles.a
	print(title.string)

