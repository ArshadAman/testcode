from bs4 import BeautifulSoup
import requests
import time
import smtplib
from twilio.rest import Client

account_sid = "AC04d09d522ca2d8be4c84dc4d1eac7afa"
auth_token = "5a080764de31a80d27d307c0fa126100"

client = Client(account_sid, auth_token)

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

    print(int(current_price_int))
    print(int(day_high_int))
    print(int(day_low_int))

    

    if int(current_price_int) == int(day_high_int)-2:
        message = """\
            Subject: Buy DOGE

            This is the best time to buy doge. Happy Trading...."""

        call = client.calls.create(
                        url='https://arshadaman.github.io/callmsg/sell.xml',
                        to='+917978518687',
                        from_='+18174403957'
                    )
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as server:
            server.starttls()
            server.login("arshadcryptoagency@gmail.com", "ek baar baap bol")
            server.sendmail("arshadcryptoagency@gmail.com", "arshadaman202@gmail.com", message)

    elif current_price_int == int(day_low_int)+2:
        call = client.calls.create(
                url='https://arshadaman.github.io/callmsg/buy.xml',
                to='+917978518687',
                from_='+18174403957'
            )

while True:
    alert()
    time.sleep(200)




