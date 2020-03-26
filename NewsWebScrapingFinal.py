import webbrowser
import newspaper
from newspaper import Article

url = "https://www.hindustantimes.com/india-news/pm-modi-asks-g20-for-an-effective-global-response-to-coronavirus-reports/story-myRgcYwmAhEX077ZZdGCbP.html"

toi_article = Article(url, language="en") # en for English

toi_article.download()
toi_article.parse()
toi_article.nlp()
f = open('art.html','w')
a = "https://www.hindustantimes.com/rf/image_size_960x540/HT/p2/2020/03/26/Pictures/ahmedabad-ahmedabad-unorganised-hindustan-addresses-siddharaj-minister_1342d1d6-6f7e-11ea-ad54-628e87a77846.jpg"

message = """<html>
<head></head>
<body>
<h1>{title}</h1>
<h3>Authors:{auth}</h3>
<img src="{URL}">
<article>
  <h4>Article Publish Date: {date} </h4>
  <p>Summary:{summ}</p>
  <p>Detailed News: {text}</p>
</article>
</body>
</html>"""

new_message = message.format(URL=a,title=toi_article.title,auth=toi_article.authors,summ=toi_article.summary,text=toi_article.text,date=toi_article.publish_date )
# I've put the formatted message in a new variable
# so you can reuse "message" as a template
f.write(new_message)
f.close()

filename = '/home/ro.bansal/PycharmProjects/PythonTasksWFHmar/' + 'art.html'
webbrowser.open_new_tab(filename)

