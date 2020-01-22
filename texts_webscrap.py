import requests
from bs4 import BeautifulSoup



def check(url):
	words_list=[]
	source=requests.get(url).text
	
	soup=BeautifulSoup(source,'html.parser')
	
	for text_cont in soup.findAll('h1'):
		textcontent=text_cont.text
		
	words=textcontent.lower().split()
	
	for each_word in words:
		words_list.append(each_word)
		
	print(words_list)
	#cleanwords(words_list)

	
def cleanwords(words_list):
	cleanlist=[]
	symbols='!@#$%^&*()_-+={[}]|\;:"<>?/., '
	
	for word in words_list:
		for i in range(0,len(symbols)):
			word.replace(symbols[i],'')
			
		if(len(word)>0):
			cleanlist.append(word)
		
	createdictionary(cleanlist)
	
def createdictionary(cleanlist):
	word_count={}
	
	for word in cleanlist:
		if word in word_count:
			word_count[word]+=1
		else:
			word_count =1

	
			
urlx=input('Enter the url to check :')	
check(urlx)