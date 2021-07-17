import os
import time
import requests
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
    "cookie": "sessionid=48607609727%3ARbkUhXL7rxCt56%3A28;"
}
username = "mohammadalhamdon"
password = "Mb803613"

options = Options()
options.add_argument("--headless")

geckodriver = os.getcwd() +"/geckodriver"
# webdriver = Firefox(options=options, executable_path=geckodriver)
webdriver = Firefox(executable_path=geckodriver)
'''
getdriver = ("https://www.instagram.com/accounts/login/")
webdriver.get(getdriver)

webdriver.find_element_by_xpath("//input[@name='username']").send_keys(username)
webdriver.find_element_by_xpath("//input[@name='password']").send_keys(password)
webdriver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(10)
'''
def download(url, name):
    session = requests.Session()
    r = session.get(url)
    with open(name, 'wb') as outfile:
        outfile.write(r.content)

def file_name(realse_date):
    suffix = '_'
    realse_date = realse_date.replace(':', '_').replace(' ', '_')
    return realse_date

def get_data(db, username):
    instagram_profile = Profile(username)
    instagram_profile.scrape(headers=headers)
    posts = instagram_profile.get_recent_posts(webdriver=webdriver, login_first=True)

    scraped_posts, unscraped_posts = scrape_posts(posts, headers=headers, pause=5, silent=False)
    
    db.posts_col()
    for p in scraped_posts:
        
        InsPostlink = IG_URL + p.shortcode
        filter = {'InsPostlink': str(InsPostlink)}
        if not db.find_one(filter):
            post = {
                'InfoUpdateDate': datetime.datetime.utcnow(),
                'InsPageLink': IG_PROFILE + username,
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
            
            _file_name = file_name(str(post['RelaseDate'])) + \
                        '_UTC' + f'_{username}'
            image_address = f'media/{_file_name}'            
            filename = f'{image_address}.jpg'
            download(p.display_url, filename)

            post['PostImagelink'] = '/root/code/ig-scraper/' + image_address + '.jpg'

            db.insert_one(post)  # Insert to Database
    res = {
    'InsPageLink': IG_PROFILE + username,
    'InsPageName': username,
    'BioText': instagram_profile.biography,
    'FolowerAtUpdate': instagram_profile.followers,
    'FolowingAtUpdate': instagram_profile.following,
    'PostCount': instagram_profile.posts,
    'SiteLink': instagram_profile.external_url,
    'Check': True,
    }
    return res

# Database setUp.
mydb = DB()
mydb.connect()
mydb.select_database('instagram_test')

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

            if result:
                mydb.refinstagram_col()
                if status:
                    mydb.delete_one(status)
                mydb.insert_one(result)

            bar()
