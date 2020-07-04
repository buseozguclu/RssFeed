# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:10:24 2020

@author: Buse
"""
from flask import Flask
app = Flask(__name__)
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]
print(myclient.list_database_names())
mycol = mydb["Haberler"]
import feedparser 

#mynethaber
url=('http://www.mynet.com/haber/rss/sondakika')
haberler=feedparser.parse(url)

i=0
 
for x in haberler.entries:
     i+=1
     print("-----------------------")
     print(i,".haber")
     print(x.title)
     print(x.link)
     print(x.description)
     mydict={  "title": x.title, "link": x.link,"description":x.description}
     mycol.insert_one(mydict)
     print("     ")
         
url=('http://www.haberturk.com/rss/manset.xml')
haberler=feedparser.parse(url)
j=0
for y in haberler.entries:
    print("-----------------------")
    j+=1
    print(j,"haber")
    print(y.title)
    print(y.link)
    print(y.description)
    mydict={ "_id": y.id, "title": y.title, "link": y.link,"description":y.description}
    mycol.insert_one(mydict)
    print("                        ")    
   
url=('https://www.cnnturk.com/feed/rss/all/news')
haberler=feedparser.parse(url)
k=0
for z in haberler.entries:
    print("-----------------------")
    k+=1
    print(k,".haber")
    print(z.title)
    print(z.link)
    print(z.description)
    mydict={ "_id": z.id, "title": z.title, "link": z.link,"description":z.description}
    mycol.insert_one(mydict)
    print("                        ")

url=('https://www.sabah.com.tr/rss/gundem.xml')
haberler=feedparser.parse(url)
m=0
for t in haberler.entries:
    m+=1
    print("-----------------------")
    print(m,".haber")
    print(t.title)
    print(t.link)
    print(t.description)
    mydict={ "_id": t.id, "title": t.title, "link": t.link,"description":t.description}
    mycol.insert_one(mydict)
    print("                        ")

url=('https://www.ntv.com.tr/son-dakika.rss')
haberler=feedparser.parse(url)
p=0
for b in haberler.entries:
    print("-----------------------")
    p+=1
    print(p,".haber")
    print(b.title)
    print(b.link)
    print(b.description)
    mydict={ "_id": b.id, "title": b.title, "link": b.link,"description":b.description}
    mycol.insert_one(mydict)
    print("                       ")
    
url=('http://feeds.bbci.co.uk/turkce/rss.xml')
haberler=feedparser.parse(url)
r=0
for c in haberler.entries:
    r+=1
    print("-----------------------")
    print(r,".haber")
    print(c.title)
    print(c.link)
    print(c.description)
    mydict={ "_id": c.id, "title": c.title, "link": c.link,"description":c.description}
    mycol.insert_one(mydict)
    print("                        ")