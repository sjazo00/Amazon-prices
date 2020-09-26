import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.ebay.com/itm/SALE-Nikon-D780-Digital-SLR-Camera-Body-Only/184380024307?epid=5036225075&hash=item2aede7e5f3:g:P64AAOSwjj1fINYm'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()
    converted_price = float(price[4:9])

    if(converted_price < 1.300):
        send_mail()

    print(converted_price)
    print(title.strip())

    
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('E-mail', 'Google App Passwords') #fill

    subject = 'Price fell down!'
    body = 'Check the link https://www.ebay.com/itm/SALE-Nikon-D780-Digital-SLR-Camera-Body-Only/184380024307?epid=5036225075&hash=item2aede7e5f3:g:P64AAOSwjj1fINYm'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'SendingEmail', #fill 
        'ReceivingEmail', #fill
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)




