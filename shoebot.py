import bs4
import webbrowser
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
<<<<<<< HEAD
from download import download
=======
import urllib3
import os
>>>>>>> 4f454527e932a80578d3b87cb4b3fea37dc91c76

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
    print("Selecting quantity...")
    quantitySelect.click()

def findIframe():
    driver.switch_to.frame(3)


def recaptcha():
    # Click on checkbox to initate challenge
    try:
        waitele = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#g-recaptcha > div > div > iframe")))
    finally:
        captchaButton = driver.find_element_by_css_selector("#g-recaptcha > div > div > iframe")
        captchaButton.click()
    # Switch to challange iframe
    print("Scrolling...")
    driver.execute_script("window.scrollTo(0, 270)")
    findIframe()
    try:
        print("Searching for audio button...")
        waitele = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-audio-button']")))
    finally:
        print("Found! Clicking...")
        audioChallenge = driver.find_element_by_class_name("rc-button-audio")
        audioChallenge.click()
    url = driver.current_url()
    downloadFile(url)



def addToCart():
    recaptcha()
    try:
        waitele = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div > div:nth-child(1) > div.empty_pdp_space_reserver___IFQzq > div > div.hero___2YuNz > div.container.hero_container___nM-YT > div.order_information___z33d1.col-s-12.col-l-8.col-hg-7 > div > div > form > div.row.no-gutters.add_to_bag_container___16ts0 > button')))
    finally:
        addToCart = driver.find_element_by_css_selector('#app > div > div:nth-child(1) > div.empty_pdp_space_reserver___IFQzq > div > div.hero___2YuNz > div.container.hero_container___nM-YT > div.order_information___z33d1.col-s-12.col-l-8.col-hg-7 > div > div > form > div.row.no-gutters.add_to_bag_container___16ts0 > button')
        addToCart.click()
        print("Adding to Cart...")
    print("Successful!")
    try:
        print("Waiting for element to appear...")
        waitele = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#modal-root > div.gl-modal.gl-modal--regular.gl-modal--mobile-full.gl-modal--active.glass-modal___1JNyq > div.gl-modal__dialog.no-gutters.col-l-12 > div > div > div > div.row.no-gutters.gl-hidden-s-m.undefined > div.col-l-12 > div > a.gl-cta.gl-cta--primary.gl-cta--full-width.gl-vspacing-s")))
    finally:
        viewbag = driver.find_element_by_css_selector("#modal-root > div.gl-modal.gl-modal--regular.gl-modal--mobile-full.gl-modal--active.glass-modal___1JNyq > div.gl-modal__dialog.no-gutters.col-l-12 > div > div > div > div.row.no-gutters.gl-hidden-s-m.undefined > div.col-l-12 > div > a.gl-cta.gl-cta--primary.gl-cta--full-width.gl-vspacing-s")
        print("Element found! Clicking...")
        viewbag.click()


def paypal():
    checkoutPaypal = driver.find_element_by_css_selector("#content > div.cart-wrapper.row > div.container.clearfix > div.cart-right.col-4.co-delivery-right.vertical-callout-container.rbk-mobile-shadow-block > div.mobile-cart-summary.rbk-mobile-shadow-block.clear.clearfix > div > div.co-actions.cart-bottom-actions > a > button")
    checkoutPaypal.click()

def card():
    checkoutCard = driver.find_element_by_css_selector("")

def payment(method):
    if method == "paypal":
        print("Wise choice :)")
        paypal()
    if method == "card":
        card()

def Main(model, size, quantity):
    URL = urlgen(model, size)
    driver.get(URL)
    print("Loading page...")
    #CheckStock(URL)
    selectQuantity(URL, quantity)
    addToCart()
    method = input("Payment Method? ")
    payment(method)
    print("End of script. Closing Driver...")
    driver.quit()

cwd = os.getcwd()
chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=cwd + '/chromedriver')

productCode = "G27805"  #input("Input Product Code: ")
Size = 8  #input("Input Size of Shoe: ")
Amount = 1  #input("Input quantity of pairs: ")

#try:
Main(productCode, Size, Amount)
#except:
    #print("Error occurred, closing Driver.")
    #driver.quit()
