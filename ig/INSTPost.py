from os.path import dirname

from instaloader import Instaloader, Profile

from functions import get_data
from exporter import export_json
from database import DB

DIR = dirname(dirname(__file__))
FILE = f'{DIR}/docs/ig-credentials'

user_credentials = open(FILE, 'r').readline().strip()
USERNAME = user_credentials.split(':')[0]
PASSWORD = user_credentials.split(':')[1]

# Get instance
L = Instaloader()
L.login(USERNAME, PASSWORD)
if L.test_login():
    print(L.test_login(), 'has logined successfully. (＾ ▽ ＾)\n')

profile = Profile.from_username(L.context, 'pharmasearch')
all = []
# Database setUp.
mydb = DB()
mydb.connect()
mydb.select_database('instagram')
mydb.posts_col()

for acc in profile.get_followees():
    result = get_data(L, mydb, acc.username)
    all.append(result)
