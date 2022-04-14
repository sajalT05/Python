import os
from selenium import webdriver
os.environ['PATH'] += 'resources/chromedriver'
driver=webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/')
driver.find_element_by_id('downloadButton').click()

