#import nltk
#nltk.download('punkt')
import newspaper
from newspaper import Article

#A new article from TOI
toi_paper = newspaper.build("https://www.hindustantimes.com/")

#DOUBT -- HOW TO PRINT URLs OF FIRST 5 TOI_ARTICLES ONLY FROM THE LIST TOI_PAPER_ARTICLES ????
for toi_article in toi_paper.articles :
    print(toi_article.url)

#for toi_category in toi_paper.category_urls():
 #   print(toi_category)

"""
#For different language newspaper refer above table
toi_article = Article(url, language="en") # en for English
"""

toi_article = toi_paper.articles[1]

#toi_article = toi_paper.articles[1]
#To download the article
toi_article.download()

#To parse the article
toi_article.parse()

#To perform natural language processing ie..nlp
toi_article.nlp()

#To extract title
print("Article's Title:")
print(toi_article.title)
print("\n")

#To extract publish date
print("Article Publish Date:")
print(toi_article.publish_date)
print("\n")

#To extract authors
print("Article's authors:")
print(toi_article.authors)
print("\n")

#To extract text
print("Article's Text:")
print(toi_article.text)
print("\n")

#To extract summary
print("Article's Summary:")
print(toi_article.summary)
print("\n")

#To extract keywords
print("Article's Keywords:")
print(toi_article.keywords)
print("\n")
#To extract HTML
print("Article's HTML:")
#print(toi_article.html)
toi_article.html