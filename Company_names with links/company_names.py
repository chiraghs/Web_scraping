import requests
from bs4 import BeautifulSoup
from csv import writer


source=requests.get("https://www.hackerearth.com/companies/")

soup=BeautifulSoup(source.text,"html.parser")

el=soup.find_all(class_='company-card-container')

for item in el:
   # print(item)
    print("\n")
    title=item.find(class_='name ellipsis').get_text().replace('\n',"")
    place=item.find(class_='company-info').get_text().replace('\n',"")
    link=item['link']
    print(title +" : "+ place +" -- "+link)
