from bs4 import BeautifulSoup
import requests
import time
import smtplib
import os
from twilio.rest import Client


account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
password = os.environ['password']


client = Client(account_sid, auth_token)

buy_message = """
    Subject: Buy DOGE\

    This is the best time to buy doge. Happy Trading...."""
sell_message = """
    Subject: Sell DOGE\

    This is the best time to sell doge. Happy Trading...."""

def alert():
    URL = """https://coinswitch.co/coins/dogecoin/buy-dogecoin-in-india#:~:text=What%20is%20the%20current%20price,is%20trading%20at%20%E2%82%B9%2041.741694644037835."""
    r = requests.get(URL)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    current_price = str(soup.find_all(class_="content__block__info--data")[0])
    day_high = str(soup.find_all(class_="content__block__info--data")[1])
    day_low = str(soup.find_all(class_="content__block__info--data")[2])

    current_price_int = float(current_price[40:46].strip())
    day_high_int = float(day_high[40:46].strip())
    day_low_int = float(day_low[40:46].strip())

    print(current_price_int)
    print(day_high_int)
    print(day_low_int)


    # Algorithm to sell the doge
    if int(current_price_int) == int(day_high_int)-2:
        call = client.calls.create(
                        url='https://arshadaman.github.io/callmsg/sell.xml',
                        to='+917978518687',
                        from_='+18174403957'
                    ) 
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login("arshadcryptoagency@gmail.com", password)
            server.sendmail("arshadcryptoagency@gmail.com", "arshadaman202@gmail.com", sell_message)

    elif int(current_price_int) == int(day_high_int)-3:
        call = client.calls.create(
                        url='https://arshadaman.github.io/callmsg/sell.xml',
                        to='+917978518687',
                        from_='+18174403957'
                    )
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login("arshadcryptoagency@gmail.com", password)
            server.sendmail("arshadcryptoagency@gmail.com", "arshadaman202@gmail.com", sell_message)


    # Algorithm to buy the doge
    elif current_price_int == int(day_low_int)+2:
        call = client.calls.create(
                url='https://arshadaman.github.io/callmsg/buy.xml',
                to='+917978518687',
                from_='+18174403957'
            )
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login("arshadcryptoagency@gmail.com", password)
            server.sendmail("arshadcryptoagency@gmail.com", "arshadaman202@gmail.com", buy_message)

    elif current_price_int == int(day_low_int)+3:
        call = client.calls.create(
                url='https://arshadaman.github.io/callmsg/buy.xml',
                to='+917978518687',
                from_='+18174403957'
            )
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login("arshadcryptoagency@gmail.com", password)
            server.sendmail("arshadcryptoagency@gmail.com", "arshadaman202@gmail.com", buy_message)

while True:
    alert()
    time.sleep(10)




