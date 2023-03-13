import requests
from bs4 import BeautifulSoup
from send_email import sendMail
import time

url1="https://www.trendyol.com/biggamex/aizen-gt63-i5-3470-16gb-ram-1tb-hdd-4gb-gt730-19-oyuncu-masaustu-bilgisayari-p-58663257"


def checkPrice(url,paramPrice):
    
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    page = requests.get(url, headers=headers)

    htmlPage = BeautifulSoup(page.content,'html.parser')

    productTitle=htmlPage.find("h1", class_="pr-new-br").getText()

    price = htmlPage.find("span" , class_="prc-dsc").getText()

    image = htmlPagefind("img" , class_="js-image-zoom__zoomed-area")

    convertedPrice = float(price.replace(",",".").replace(" TL",""))

    if(convertedPrice <= paramPrice):
        print("Ürün fiyatı düştü")
        htmlEmailContent= """\
            <html>
            <head></head>
            <body>
            <h3>{0}</h3>
            <br/>
            {1}
            <br/>
            <p>Ürün linki: {2}</p>
            </body>
            </html>
            """.format(productTitle, image, url)
        sendMail("KIME EMAİL","Ürünün fiyatı düştü👍👍", htmlEmailContent)
    else:
        print("ürün fiyatı düşmedi")

while(True):
    checkPrice(url1,150)
    time.sleep(3)