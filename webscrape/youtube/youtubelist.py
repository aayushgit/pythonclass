import urllib.request
from bs4 import BeautifulSoup as soup
import urllib.parse as up
#imported re package
import re

class AppURLOpener(urllib.request.FancyURLopener):
	version = "Mozilla/5.0"
opener = AppURLOpener()

my_url = "https://www.youtube.com/playlist?list=PLY_geU-dV3mb3BEFXsUATnspnttym9N6C" #changed the url slightly by removing the 'class' written at last
uClient = opener.open(my_url)
html_page = uClient.read()
uClient.close()
page_soup = soup(html_page,"html.parser")
songlist = page_soup.find_all(href = re.compile('^/watch\?v=.*')) #capture the video url from the html page
for l in songlist:
    a = l.get("href")
    url_data = up.urlparse(a)
    query = up.parse_qs(url_data.query)
    video = query["v"][0]
    print(video)
