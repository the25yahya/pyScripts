from sys import argv 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options

script, url = argv
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-smh-usage')


webdriver_service = Service("/home/kali/.ZAP/webdriver/linux/64/chromedriver")

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

driver.get(url)

content = driver.page_sources
driver.quit()

print(content)