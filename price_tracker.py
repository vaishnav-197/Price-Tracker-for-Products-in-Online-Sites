import requests
import smtplib
import time

from bs4 import BeautifulSoup


URL='https://www.amazon.in/Tetley-Green-Ginger-Mint-Lemon/dp/B00MGFZEVW/ref=lp_21246951031_1_9?srs=21246951031&ie=UTF8&qid=1587071732&sr=8-9'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'}
 
def check_price() :
    page = requests.get(URL , headers=headers)

    soup= BeautifulSoup(page.content , 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:5])

    print(title.strip())
    print(converted_price)

    if converted_price<320 :
        send_mail()

def send_mail()  :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    
    server.login('username' , 'generated password')
    
    subject = 'Price Decreased'
    body= 'https://www.amazon.in/Tetley-Green-Ginger-Mint-Lemon/dp/B00MGFZEVW/ref=lp_21246951031_1_9?srs=21246951031&ie=UTF8&qid=1587071732&sr=8-9'
    msg= f"Subject : {subject}\n\n{body}"
    
    server.sendmail(
        'mailid',
        'mailid',
        msg
    )
    print("MAIL SENT")
    server.quit()
    
    while True :
     check_price()
     time.sleep(60*60*60)
    