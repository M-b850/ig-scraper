from os.path import dirname

from instaloader import Instaloader

from functions import get_data

DIR = dirname(dirname(__file__))
FILE = F'{DIR}/docs/ig-credentials'

user_credentials = open(FILE, 'r').readline().strip()
USERNAME = user_credentials.split(':')[0]
PASSWORD = user_credentials.split(':')[1]

# Get instance
L = Instaloader()
L.login(USERNAME, PASSWORD)
if L.test_login():
    print(L.test_login(), 'has logined successfully. (＾▽＾)')

get_data(L, 'kendalljenner')
