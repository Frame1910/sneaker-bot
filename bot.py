import bs4
import webbrowser
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os

class Bot():
    def __init__(self):
        self.cwd = os.getcwd()
        self.chrome_options = Options()
        self.chrome_options.add_argument("--window-size=1920,1080")

    def urlgen(self, model, size):
        BaseSize = 580
        #BaseSize is for Shoe Size 6.5
        ShoeSize = int(size) - 6.5
        ShoeSize = ShoeSize * 20
        RawSize = ShoeSize + BaseSize
        ShoeSizeCode = int(RawSize)
        self.url = 'http://www.adidas.com.au/' + str(model) + '.html?forceSelSize=' + str(model) + '_' + str(ShoeSizeCode)
        print("Generated URL:", self.url)
    
    def launchDriver(self):
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options, executable_path=self.cwd + '/chromedriver')
        self.driver.get(self.url)
        print("Lauching WebDriver with generated link")

    def __del__(self):
        print("Finished. Closing WebDriver")
        self.driver.close()

bot = Bot()
bot.urlgen("EE5696", 8)
bot.launchDriver()
del bot