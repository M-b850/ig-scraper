from os.path import dirname, abspath

from instaloader import Instaloader, Profile
from alive_progress import alive_bar

from functions import get_data
from exporter import export_json
from database import DB

DIR = dirname(dirname(abspath(__file__)))
FILE = DIR + '/' + 'pharmasearch'

"""
FILE = f'{DIR}/docs/ig-credentials'
user_credentials = open(FILE, 'r').readline().strip()
USERNAME = user_credentials.split(':')[0]
PASSWORD = user_credentials.split(':')[1]
"""
# Get instance
L = Instaloader()

# L.login(USERNAME, PASSWORD)
L.load_session_from_file('pharmasearch', FILE)
if L.test_login():
    print(L.test_login(), 'has logined successfully. (＾ ▽ ＾)\n')

profile = Profile.from_username(L.context, 'pharmasearch')

# Database setUp.
mydb = DB()
mydb.connect()
mydb.select_database('instagram')
mydb.posts_col()

count = profile.followees

with alive_bar(count) as bar:
    # Progress bar    
    for acc in profile.get_followees():
        result = get_data(L, mydb, acc.username)
        bar()
