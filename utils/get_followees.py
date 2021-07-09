from instaloader import *
from os.path import dirname, abspath

DIR = dirname(dirname(abspath(__file__)))
FILE = DIR + '/' + 'yourboy.newton'

L = Instaloader()

L.load_session_from_file('yourboy.newton', FILE)
if L.test_login():
    print(L.test_login(), 'has logined successfully. (＾ ▽ ＾)\n')

profile = Profile.from_username(L.context, 'pharmasearch')

with open('utils/usernames.txt', 'w+') as f:
    for followee in profile.get_followees():
        f.write(f'{followee.username}\n')
        print(followee.username)
