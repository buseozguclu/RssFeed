# RssFeed
---------------IMPORTS LIBRARY-----------------
Flask

Pymongo --> Connect to Moongo Db
Use Mongo DB Compass Community Version
Localhost:27017 is default MongoDB

Feedparser --> Pull for rssdata.xml

--------------CODING----------------------------
url=('rss-url')
haberler=feedparser.parse(url) ---> pulling data

i=0
 
for x in haberler.entries:
     i+=1
     print("-----------------------")
     print(i,".haber")
     print(x.title)              --->New's Title
     print(x.link)               --->New's Link
     print(x.description)        --->New's Content
     mydict={  "title": x.title, "link": x.link,"description":x.description} ----------> In MongoDB virtualization
     mycol.insert_one(mydict)                                                 ---------> Insert to data
     print("     ")
--------------------------------------------------


         
