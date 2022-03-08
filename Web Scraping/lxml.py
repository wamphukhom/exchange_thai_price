#basic-webscraping.py

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup # as soup คือ การตั้งคำสั้นๆ

def StockPrice():
    url = 'https://trade.bitazza.com/cdn-cgi/bm/cv/669835187/api.js'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    web_byte = urlopen(req)
    webpage = web_byte.read().decode('utf-8')
    web_byte.close()

    data = soup(webpage, 'html.parser')
    result = data.find_all('script')
    return (data)

# gold = StockPrice()
# print(gold)

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)