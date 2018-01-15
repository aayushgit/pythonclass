import urllib.request 
from bs4 import BeautifulSoup as soup
class AppURLOpener (urllib.request.FancyURLopener):  #AppURLopener which overrides the user-agent with Mozilla because sraping bot blocked
		version="Mozilla/5.0"
opener = AppURLOpener() #instance of overriding class

#url to scrape
my_url ='https://www.daraz.com.np/smartphones/'

#opening connection and grabbing the page
uClient = opener.open(my_url)
#put content in a variable
page_html = uClient.read()
#close the connection
uClient.close()
#html parsing
page_soup = soup(page_html,"html.parser")
#get the container of phones
container=page_soup.findAll("div",{"class":"sku -gallery "})
for contain in container:
	brand = contain.h2.span.text.strip()
	name = contain.div.img["alt"]
	price_container = contain.findAll("div",{"class":"price-container"})
	discount = price_container[0].span.text.strip()
	price = price_container[0].findAll("span",{"class":"price"})[0].text.strip()

	print("Brand:" +brand)
	print("Name:" +name)
	print("Discount:" +discount)
	print("Price:" +price)