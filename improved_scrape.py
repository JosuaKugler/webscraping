#import libraries
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(firefox_options=options, executable_path = '/home/josua/Programme/geckodriver')

urlpage = 'https://groceries.asda.com/search/yogurt'
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(5)
results = driver.find_elements_by_xpath("//*[@id='componentsContainer']//*[contains(@id,'listingsContainer')]//*[@class='product active']//*[@class='title productTitle']")
print('Number of results', len(results))
driver.quit()
