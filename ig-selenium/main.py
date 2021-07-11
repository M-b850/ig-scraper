import os
import time
import datetime

from alive_progress import alive_bar
from instascrape import *
from database import DB

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
webdriver = Firefox(options=options, executable_path=geckodriver)
# webdriver = Firefox(executable_path=geckodriver)

getdriver = ("https://www.instagram.com/accounts/login/")
webdriver.get(getdriver)

webdriver.find_element_by_xpath("//input[@name='username']").send_keys(username)
webdriver.find_element_by_xpath("//input[@name='password']").send_keys(password)
webdriver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(10)

def get_data(mydb, username):
    instagram_profile = Profile(username)
    instagram_profile.scrape(headers=headers)
    posts = instagram_profile.get_posts(webdriver=webdriver)

    scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=10, silent=False)

    for p in scraped_posts:
        post = {
            'InfoUpdateDate': datetime.datetime.utcnow(),
            'InsPageLink': IG_PROFILE + p.username,
            'PostFolowerPostShare': instagram_profile.followers,
            'PostFolowingPostShare': instagram_profile.following,
            'PostCount': len(posts),
            'RelaseDate': p.upload_date,
            'InsPostlink': IG_URL + p.shortcode,
            'PostImagelink': p.display_url,
            'PostLike': p.likes,
            'PostComment': p.comments,
            'PostSaveCount': None,
            'PostSendCount': None,
            'PostDiscription': p.caption,
        }

'''

# Database setUp.
mydb = DB()
mydb.connect()
mydb.select_database('instagram')

with alive_bar(4325) as bar:
    with open('usernames.txt') as f:
        username_list = f.readlines()    
        for acc in username_list:
            acc = acc.strip()
            
            ig_uni_key = IG_PROFILE + acc
            
            mydb.refinstagram_col()
            filter = {'InsPageLink': ig_uni_key}
            status = mydb.find_one(filter)
            try:
                if status['Check'] == True:
                    print('Passed.')
                    bar()
                    continue
            except KeyError:
                pass
            except TypeError:
                pass

            print(acc)
            result = get_data(mydb, acc)


            # insomnia = random.randint(100, 150)
            # print('\n~~~~Page Insomnia is:', insomnia)
            bar()
            
            '''

mydb = 1
get_data(mydb, 'bunnycolby')