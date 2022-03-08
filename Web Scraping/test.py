import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/watch?v=c0GAiHMneog"
css_selector = "#movie_player > div.html5-video-container > video"

"""#Failed Beautiful Soup Attempt -----------------------------------------------------------
website = requests.get(url)
content = website.content
#content = open("yt html.txt", "r").read() #getting html code from txt works
soup = BeautifulSoup(content, "html.parser")
element = soup.select(css_selector)
#get url
for attr in element:
    print(attr["src"])"""

#Solution with Selenium -------------------------------------------------------------------

#WebDriver Downloads: https://selenium-python.readthedocs.io/installation.html

from selenium import webdriver
from time import sleep

wd_path = 'C:\AppServ\www\chromedriver.exe'

#webdriver options
option_headless = webdriver.ChromeOptions()
option_headless.add_argument("headless")
#get the driver
wdriver = webdriver.Chrome(executable_path=wd_path, options=option_headless)

#get site content
wdriver.get(url)
sleep(3)

#find element
element = wdriver.find_element_by_css_selector(css_selector)

#get video url
video_url = element.get_attribute("src")

print(video_url)

#close
wdriver.quit()