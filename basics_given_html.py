import requests
from bs4 import BeautifulSoup

html_doc ="""
<!DOCTYPE html>

<html>
  <head>
   <meta charset="utf-8"/>
   <title>Enter SoloLearn</title>
   <link href="estilos.css" rel="stylesheet" type="text/css">
  </head>
  
  <body>
   
   <header>
     <h1>Juan Baños
     <img alt="" class="img" src= "https://api.sololearn.com/Uploads/Avatars/10580770.jpg"></h1>
   </header>
   
   <div class="enter">
    <h1>Enter SoloLearn</h1>
   </div>
   
   <div class="container">
    <video class="video"  controls> <source src="https://dl.dropbox.com/s/182fjn03g8clpit/InSoloLearn.mp4?dl=0" type="video/mp4"> Tu navegador no soporta HTML5 video. </video>
   </div>
  </body>
  
</html>
"""

soup=BeautifulSoup(html_doc,'html.parser')

#Direct
print(soup.head)


#findAll(),find
el=soup.findAll('div')[1]
print(el)
print(soup.find(class_='video'))

#select
#print(soup.select('#id'))
print(soup.select('.enter'))#in a list

#gettext() or text
for item in soup.select('header'):
      print(item.get_text())

for item in soup.select('.enter'):
      print(item.text)      

#Navigating dom
el2=soup.body.contents[1].contents[1]
el3=soup.body.contents[1].find_next_sibling() # find_previous_sibling() , find_parent()

print(el2)
print(el3)