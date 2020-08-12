from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
#opening connection and grabbing page
uClient = uReq(my_url)
page_html = uClient.read()


#close the client
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")


#print(page_soup.body.li)

containers = page_soup.findAll("div",{"class":"item-container"})

filename="product.csv"
f= open(filename,"w")

header= "brand , Product_Name,Shipping"

f.write(header)


for container in containers:
    brand=container.div.div.a.img["title"]
    title_container=container.findAll("a",{"class":"item-title"})
    product_name=title_container[0].text

    shipping_container=container.findAll("li",{"class":"price-ship"})
    shipping=shipping_container[0].text.strip()

    f.write("\n")
    f.write(brand + ',' + product_name.replace(",","|") + ',' + shipping)

f.close()
