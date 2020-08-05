from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphic+cards'
#opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()

#close the client
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

print(page_soup.h1)


