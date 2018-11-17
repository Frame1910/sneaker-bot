import random
import bs4
import webbrowser
import csv
import re
import urllib3
import requests
from selenium import webdriver

# Fake Headers: headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def urlgen(model, size):
    BaseSize = 580
    #BaseSize is for Shoe Size 6.5
    ShoeSize = int(size) - 6.5
    ShoeSize = ShoeSize * 20
    RawSize = ShoeSize + BaseSize
    ShoeSizeCode = int(RawSize)
    url = 'http://www.adidas.com.au/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
    print(url)
    return url

def CheckStock(url):
    # These methods DO NOT work if desired elements are rendered with JavaScipt
    # hdr = {'User-Agent': 'Mozilla/5.0'}
    # req = requests.get(url, headers=hdr)\
    driver = webdriver.Chrome('C:/Users/dpmei/Documents/GitHub/sneaker-bot/chromedriver')
    driver.get(url)
    req = driver.page_source
    page = bs4.BeautifulSoup(req, "html.parser")
    title = page.title.string
    print(title)
    ListOfSizesRaw = page.find_all("select", attrs={"aria-label":"Select Size"})
    print(ListOfSizesRaw)

def Main(model, size):
    URL = urlgen(model, size)
    CheckStock(URL)


Main('AQ0943', 8)
