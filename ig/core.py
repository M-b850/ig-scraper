from os.path import dirname, abspath
import time
import random

from instaloader import Instaloader, Profile
from alive_progress import alive_bar

from functions import get_data
from exporter import export_json
from database import DB
import const

DIR = dirname(dirname(abspath(__file__)))

"""
FILE = f'{DIR}/docs/ig-credentials'
user_credentials = open(FILE, 'r').readline().strip()
USERNAME = user_credentials.split(':')[0]
PASSWORD = user_credentials.split(':')[1]
"""
# Get instance
L = Instaloader()

# L.login(USERNAME, PASSWORD)
'''
Accounts:
jackrobinson6750
lanakoben
mohammadalhamdon
pharmasearch
yourboy.newton
'''
acc_name = 'jackrobinson6750'
FILE = DIR + '/Accounts/' + acc_name
L.load_session_from_file(acc_name, FILE)
if L.test_login():
    print(L.test_login(), 'has logined successfully. (＾ ▽ ＾)\n')

profile = Profile.from_username(L.context, 'pharmasearch')

# Database setUp.
mydb = DB()
mydb.connect()
mydb.select_database('instagram')

count = profile.followees

with alive_bar(count) as bar:
    with open('utils/usernames.txt') as f:
        # Progress bar
        # profile.get_followees()
        username_list = f.readlines()    
        for acc in username_list:
            acc = acc.strip()
            
            ig_uni_key = const.IG_PROFILE + acc
            
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
            result = get_data(L, mydb, acc)
            if result:
                mydb.refinstagram_col()
                if status:
                    mydb.delete_one(status)
                mydb.insert_one(result)

            # insomnia = random.randint(100, 150)
            # print('\n~~~~Page Insomnia is:', insomnia)
            bar()
