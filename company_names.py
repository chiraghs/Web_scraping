import requests
from bs4 import BeautifulSoup
from csv import writer


source=requests.get("https://www.hackerearth.com/companies/")

soup=BeautifulSoup(source.text,"html.parser")

el=soup.find_all(class_='company-card-container')


#csv writer

with open('/home/chiraghs/my_codes/Web_scraping/Company_names with links/names.csv','w') as f:
   elem=writer(f)
   headeres=['Title','Location ','Link']
   elem.writerow(headeres)

   #get items or data
   for item in el:
      # print(item)
      print("\n")
      title=item.find(class_='name ellipsis').get_text().replace('\n',"")
      link=item['link']
      print(title +" : " +link)
      elem.writerow([title,link])
