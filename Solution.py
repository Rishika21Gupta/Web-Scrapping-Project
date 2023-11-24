import requests
import cloudscraper
from bs4 import  BeautifulSoup
import pandas as pd

Names=[]
Date=[]
Image_url = []
Like=[]
Blogs=[]
img_url_copy=[]


for i in range(1,45):
    url="https://rategain.com/blog/page/"+str(i)
    scraper=cloudscraper.create_scraper()
    r=scraper.get(url)
    soup=BeautifulSoup(r.text,'lxml')
    np=soup.find("a",class_="next page-numbers").get("href")
    names=soup.find_all("div",class_="content")

    for i in names:
        n=i.find("h6").text
        Names.append(n) 

    D=[]
    date=soup.find_all("div",class_="bd-item")
    for i in date:
        sp=i.find("span")
        s=sp.text
        D.append(s)
    for k in range(len(D)):
        if k%2==0:
            Date.append(D[k])

    Image=[]
    for link in soup.find_all("a"):
        a=link.get("data-bg")
        Image.append(a)
    Image_url=[]
    for val in Image:
        if val != None :
            Image_url.append(val)
    for i in Image_url:
        l=len(Image_url)
        if(l<9):
            Image_url.append("---") 
    for item in Image_url: 
        img_url_copy.append(item) 
    
    l=soup.find_all("a",class_="zilla-likes")
    for i in l:
        e=i.find('span').text
        m=e[:-5]
        Like.append(m)
df=pd.DataFrame({"Blog title":Names,"Blog date":Date,"Blog image URL":img_url_copy,"Blog likes count":Like})
df.to_csv("blogSolution.csv")