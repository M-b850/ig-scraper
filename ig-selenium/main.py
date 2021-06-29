from selenium.webdriver import Chrome 
from instascrape import *

from os.path import dirname, abspath

headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
    "cookie": "sessionid=45792717507%3AbQuWYAQtBbs5Qp%3A6;"
}

DIR = dirname(abspath(__file__))
FILE = DIR + '/' + 'chromedriver'
webdriver = Chrome(FILE)

joe = Profile("bunnycolby")
joe.scrape(headers=headers)
posts = joe.get_posts(webdriver=webdriver, login_first=True)

scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=10, silent=False)
print(scraped_posts)