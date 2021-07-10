import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

geckodriver = os.getcwd() +"/geckodriver"

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path=geckodriver)
driver.get("http://google.com/")
print ("Headless Firefox Initialized")
driver.quit()

