import requests
from bs4 import BeautifulSoup

#Get amazon url for the particular product
URL = 'https://www.amazon.in/Dark-Fantasy-Choco-Fills-300g/dp/B01L7A0CU4/ref=sr_1_2_sspa?dchild=1&fpw=pantry&keywords=biscuits&qid=1609320773&s=pantry&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNkFVNjhQWE5OVllVJmVuY3J5cHRlZElkPUEwODA2MzQ4TTFMV1lRTEtRQTBQJmVuY3J5cHRlZEFkSWQ9QTA4NTE2MDExVlBMV1FHM09ZODYwJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

#type my user agent in google - to get the user agent
myuseragent= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'


def check_price():
      headers = {"User-Agent": myuseragent}
      page = requests.get(URL, headers=headers)
      soup = BeautifulSoup(page.content,'html.parser')
      price = soup.find(id='priceblock_ourprice').get_text().strip()
      #price = float(price[2:])
      return price

res=check_price()
print("Today's Price of Dark Fantasy : ",res)