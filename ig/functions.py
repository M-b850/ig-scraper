# All functions related to collecting data are here.
from instaloader import Instaloader, Profile
import datetime
import const
from os.path import dirname, abspath
import random


DIR = dirname(dirname(abspath(__file__)))

def file_name(realse_date):
    suffix = '_'
    realse_date = realse_date.replace(':', '_').replace(' ', '_')
    return realse_date

def get_data(L, db, inst_username):
    print(inst_username)
    profile = Profile.from_username(L.context, inst_username)

    PostFolowerPostShare = profile.followers
    PostFolowingPostShare = profile.followees
    PostCount = profile.mediacount
    all_posts = profile.get_posts()

    for one_post in all_posts:
        InsPostlink = const.IG_URL + one_post.shortcode
        """
        If object doesn't exists it will be added to database.-
        Other ways it won't.
        """
        filter = {'InsPostlink': InsPostlink}
        if not db.find_one(filter):
            each_post = {
                'InfoUpdateDate': datetime.datetime.utcnow(),
                'InsPageLink': const.IG_PROFILE + inst_username,
                'PostFolowerPostShare': PostFolowerPostShare,
                'PostFolowingPostShare': PostFolowingPostShare,
                'PostCount': PostCount,
                'RelaseDate': one_post.date_utc,
                'InsPostlink': InsPostlink,
                'PostImagelink': one_post.url,
                'PostLike': one_post.likes,
                'PostComment': one_post.comments,
                'PostSaveCount': None,
                'PostSendCount': None,
                'PostDiscription': one_post.caption,
            }
            _file_name = file_name(str(each_post['RelaseDate'])) + \
                        '_UTC' + f'_{inst_username}'
            image_address = f'media/{_file_name}'
            L.download_pic(
                image_address,
                each_post['PostImagelink'],
                each_post['RelaseDate'],
            )
            each_post['PostImagelink'] = f'{DIR}/' + image_address + '.jpg'
            
            db.insert_one(each_post)  # Insert to Database

        insomnia = random.randint(1, 4)
        print('\n~~~~Post Insomnia is:', insomnia)
        time.sleep(insomnia)
    return True
