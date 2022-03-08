#basic-webscraping.py

from urllib.request import urlopen as req # as req คือ การตั้งคำสั้นๆ
from bs4 import BeautifulSoup as soup

def StockPrice(CODE):
    url = f'https://www.sanook.com/{CODE}/goldrate/'

    webopen = req(url)
    page_html = webopen.read()
    webopen.close()

    data = soup(page_html, 'html.parser')
    # print(data)
    # print('---#---')

    result = data.find('div',{'class':'jsx-4046716835 SectionRecentPrice'}).find('b',{'class':'jsx-4046716835'})

    result1 = data.find('div',{'class':'jsx-4046716835 SectionRecentPrice'}).find('span',{'class':'jsx-4046716835'})

    s = float(result.text.replace(',','')) #ถ้าหากมี , จะแปลงเป็น float ไม่ได้

    print("Value: %.2f" % float(s))
    print(type(s))

    # print(result1.text)

    return (s,result1)

    # text1 = 'เปลี่ยนแปลง+1.00'
    # text = '$%เปลี่ยนแปลงก+2.58%'
    # print(len(text1))
    # print(text1[2:4])StockPrice

gold = StockPrice('money')
print('---')
print(gold[1])