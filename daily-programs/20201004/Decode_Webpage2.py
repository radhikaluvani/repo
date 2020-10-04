import requests
from bs4 import BeautifulSoup

url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
article = soup.select('div p')
with open("article.txt", "w") as file:
	for each in article:
		file.write(each.text)
print("File is created")