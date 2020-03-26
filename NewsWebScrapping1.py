#import nltk
#nltk.download('punkt')

from newspaper import Article

#A new article from TOI
url = "https://timesofindia.indiatimes.com/india/mahabharata-battle-won-in-18-days-war-against-coronavirus-will-take-21-days-pm-modi/articleshow/74813107.cms"

#For different language newspaper refer above table
toi_article = Article(url, language="en") # en for English

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