from os.path import dirname, abspath
import time
import random

from instaloader import Instaloader, Profile
from alive_progress import alive_bar

from functions import get_data
from exporter import export_json
from database import DB

DIR = dirname(dirname(abspath(__file__)))
FILE = DIR + '/' + 'yourboy.newton'

"""
FILE = f'{DIR}/docs/ig-credentials'
user_credentials = open(FILE, 'r').readline().strip()
USERNAME = user_credentials.split(':')[0]
PASSWORD = user_credentials.split(':')[1]
"""
# Get instance
L = Instaloader()

# L.login(USERNAME, PASSWORD)
L.load_session_from_file('yourboy.newton', FILE)
if L.test_login():
    print(L.test_login(), 'has logined successfully. (＾ ▽ ＾)\n')

profile = Profile.from_username(L.context, 'pharmasearch')

# Database setUp.
mydb = DB()
mydb.connect()
mydb.select_database('instagram')

count = profile.followees

with alive_bar(count) as bar:
    # Progress bar    
    for acc in profile.get_followees():
        print(acc.username)
        result = get_data(L, mydb, acc.username)
        if result:
            mydb.refinstagram_col()
            filter = {'InsPageLink': result['InsPageLink']}
            mydb.find_delete(filter)
            mydb.insert_one(result)
        # insomnia = random.randint(150, 300)
        # print('\n~~~~Page Insomnia is:', insomnia)
        bar()
