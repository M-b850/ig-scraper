import os
import time

from instascrape import *

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

IG_URL = 'http://instagram.com/p/' # IG_URL + shortocde = post url
IG_PROFILE = 'http://instagram.com/' # IG_PROFILE + username = profile url

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=47914511585%3AUjbHBFROUTyDfB%3A7"
}
username = "mohammadalhamdon"
password = "Mb803613"

options = Options()
options.add_argument("--headless")

geckodriver = os.getcwd() +"/geckodriver"
webdriver = Firefox(executable_path=geckodriver)
# webdriver = Firefox(executable_path=geckodriver)

getdriver = ("https://www.instagram.com/accounts/login/")
webdriver.get(getdriver)
time.sleep(10)
webdriver.find_element_by_xpath("//button[text()='Accept All']").click()
time.sleep(10)


webdriver.find_element_by_xpath("//input[@name='username']").send_keys(username)
webdriver.find_element_by_xpath("//input[@name='password']").send_keys(password)
webdriver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(10)