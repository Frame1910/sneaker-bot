import random
import bs4
import webbrowser
import csv
import re
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    req = driver.page_source
    page = bs4.BeautifulSoup(req, "html.parser")
    title = page.title.string
    print(title)
    SizeSelectorRaw = page.find("select", attrs={"aria-label": "Select size"})
    SizeSelectorRaw = SizeSelectorRaw.find_all("option")
    ArrayOfSizes = []
    i = 0
    while i < len(SizeSelectorRaw):
        Text = SizeSelectorRaw[i].get_text()
        print(Text)
        ArrayOfSizes.append(Text)
        i += 1
    ArrayOfSizes.remove("")
    print("Sizes Available:")
    print(ArrayOfSizes)


def selectQuantity(url, no):
    dropdownSelector = "#app > div > div:nth-child(1) > div.empty_pdp_space_reserver___IFQzq > div > div.hero___2YuNz > div.container.hero_container___nM-YT > div.order_information___z33d1.col-s-12.col-l-8.col-hg-7 > div > div > form > div.row.no-gutters.size_quantity_row___1pgH7 > div.quantity_selector___1qWYG.col-s-3 > div > div"
    selectionSelectorAddon = " > div.gl-dropdown__options > ul > li:nth-child"
    quantityDrop = driver.find_element_by_css_selector(dropdownSelector)
    quantityDrop.click()
    num = str(no)
    quantitySelect = driver.find_element_by_css_selector(dropdownSelector + selectionSelectorAddon + "(" + num + ")")
    quantitySelect.click()


def submit():
    element = driver.find_element_by_css_selector('#app > div > div:nth-child(1) > div.empty_pdp_space_reserver___IFQzq > div > div.hero___2YuNz > div.container.hero_container___nM-YT > div.order_information___z33d1.col-s-12.col-l-8.col-hg-7 > div > div > form > div.row.no-gutters.add_to_bag_container___16ts0 > button')
    element.click()
    try:
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(By.CSS_SELECTOR, "#modal-root > div.gl-modal.gl-modal--regular.gl-modal--mobile-full.gl-modal--active.glass-modal___1JNyq > div.gl-modal__dialog.no-gutters.col-l-12 > div > div > div > div.row.no-gutters.gl-hidden-s-m.undefined > div.col-l-12 > div > a.gl-cta.gl-cta--primary.gl-cta--full-width.gl-vspacing-s"))
    finally:
        viewbag = driver.find_element_by_css_selector("#modal-root > div.gl-modal.gl-modal--regular.gl-modal--mobile-full.gl-modal--active.glass-modal___1JNyq > div.gl-modal__dialog.no-gutters.col-l-12 > div > div > div > div.row.no-gutters.gl-hidden-s-m.undefined > div.col-l-12 > div > a.gl-cta.gl-cta--primary.gl-cta--full-width.gl-vspacing-s")
        viewbag.click()


def Main(model, size, quantity):
    URL = urlgen(model, size)
    driver.get(URL)
    #CheckStock(URL)
    selectQuantity(URL, quantity)
    submit()

driver = webdriver.Chrome('C:/Users/dpmei/Documents/GitHub/sneaker-bot/chromedriver')
Main('AQ0943', 8, 2)
