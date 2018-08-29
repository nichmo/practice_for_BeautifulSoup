from bs4 import BeautifulSoup
import urllib.request as req

url = "https://www.shimz.co.jp/index.html"

res = req.urlopen(url)

# soup = BeautifulSoup(res, "html.parser")
h1 = soup.html.body.h1
print(h1)

links = soup.find_all("a")

for a in links:
	href = a.attrs["href"]
	text = a.string
	print(text, ">", href)
