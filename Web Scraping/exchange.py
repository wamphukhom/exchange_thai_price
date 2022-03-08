
from os import link
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from tkinter import *
from tkinter import ttk, messagebox
import time

def writetext(page_html):
    
    filename = 'data.txt'
    with open(filename, 'a',encoding='utf-8') as file:
        file.write(page_html)

driverpath = r'C:\AppServ\www\chromedriver.exe'

#webdriver options
option_headless = webdriver.ChromeOptions()
option_headless.add_argument("headless")

driver1 = webdriver.Chrome(executable_path=driverpath, options=option_headless)
driver2 = webdriver.Chrome(executable_path=driverpath, options=option_headless)
driver3 = webdriver.Chrome(executable_path=driverpath, options=option_headless)

url1 = "https://trade.bitazza.com/th/exchange"
url2 = "https://www.bitkub.com/market/BTC"
url3 = "https://trade.zipmex.com/th/trade/BTCTHB"

driver1.get(url1)
driver2.get(url2)
driver3.get(url3)

time.sleep(3)

GUI = Tk()
GUI.geometry('800x500')
GUI.title('ดูราคา BTC ของ EXCHANGE ไทย')

L1 = Label(GUI, text='ดูไป 2 Exchange ก่อน ZMT หาไม่เจอ', font=('Angsana New',30,'bold'),fg='green')
L1.pack() # .plasc(x,y) , .grid(row=0,column=0)

def calculate(event=None):#none ฟังชั่นไหนต้องการทั้งปุ่มกดและคีย์บอร์ดต้องใส่
    page_html1 = driver1.page_source
    data1 = soup(page_html1, 'html.parser')
    result1 = data1.find('span',{'class':'instrument-table__value instrument-table__value--last-price'})

    page_html2 = driver2.page_source
    data2 = soup(page_html2, 'html.parser')
    result2 = data2.find('div',{'class':'textright market__stat-value text--green'}).find('span')

    L2['text'] = "Bitaza BTC ราคา = "+result1.text
    L3['text'] = "Bitkub BTC ราคา = "+result2.text

s = ttk.Style()
s.configure('my.TButton', font=('Angsana New', 20, 'bold'))
B1 = ttk.Button(GUI, text='แสดงค่า',command=calculate, style='my.TButton')
B1.pack(ipadx=30, ipady=20, pady=10)

L2 = Label(GUI, text='Bitaza BTC ราคา = ', font=('Angsana New',30,'bold'),fg='green')
L2.pack() # .plasc(x,y) , .grid(row=0,column=0)

L3 = Label(GUI, text='Bitkub BTC ราคา = ', font=('Angsana New',30,'bold'),fg='green')
L3.pack() # .plasc(x,y) , .grid(row=0,column=0)

GUI.mainloop()