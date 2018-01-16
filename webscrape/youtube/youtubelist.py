import urllib.request
from bs4 import BeautifulSoup as soup
class AppURLOpener(urllib.request.FancyURLopener):
	version = "Mozilla/5.0"
opener = AppURLOpener()

my_url = "https://www.youtube.com/playlist?list=PLY_geU-dV3mb3BEFXsUATnspnttym9N6Cclass"
uClient = opener.open(my_url)
html_page = uClient.read()
uClient.close()
page_soup = soup(html_page,"html.parser")
songlist = page_soup.findAll
for l in songlist:
	print (l.get("href"))
