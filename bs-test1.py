from bs4 import BeautifulSoup

html = """
<html><body>
	<h1>testh1</h1>
	<p>test1p</p>
	<p>test2p</p>

</body></html>
"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.body.h1
links = soup.find_all("a")

print(soup)
print(h1)
print(h1.string)

# リンクを取得して出力する
for a in links:
	href = a.attrs['href']
	text = a.string
	print(text, ">", href)
	