#This is a song downloading app. This downloads Aladeen Songs.
#Author:Nuclear Nadal
from bs4 import BeautifulSoup
import re
spaghetti = BeautifulSoup(open('aladeen.html'),'html.parser')
for link in spaghetti.find_all('a',href=re.compile("\.mp3$")):
	print(link.get('href'))
