from newspaper import Article

url = "https://timesofindia.indiatimes.com/india/coronavirus-roundup-developments-in-india-and-rest-of-world/articleshow/74833346.cms"

toi_article = Article(url, language="en") # en for English

toi_article.download()
toi_article.parse()
# TODO: Use 'with' statment to open file, study about with keyword in python
hs = open("art.html", 'w')
hs.write(toi_article.text)

"""
import requests
from newspaper import fulltext
#res = requests.get("https://www.hindustantimes.com").text
res = requests.get("https://www.hindustantimes.com")
res.raise_for_status()
#text = fulltext(res)
"""
