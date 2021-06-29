# All functions related to collecting data are here.
import datetime
from os.path import dirname, abspath
import random
import time
from bson import Int64
from itertools import dropwhile, takewhile

from instaloader import Instaloader, Profile

import const

# Date
SINCE = datetime.datetime.now()
UNTIL = datetime.datetime.now() - datetime.timedelta(days=365)

DIR = dirname(dirname(abspath(__file__)))

def file_name(realse_date):
    suffix = '_'
    realse_date = realse_date.replace(':', '_').replace(' ', '_')
    return realse_date


def get_comments(db, post):
    db.comments_col()
    comments = post.get_comments()    
    for c in comments:
        filter = {'id': Int64(c.id)}
        if not db.find_one(filter):
            comment = {
                'id': c.id,
                'InfoUpdateDate': datetime.datetime.utcnow(),
                'InsPageLink': const.IG_PROFILE + post.owner_username,
                'InsPostlink': const.IG_URL + post.shortcode,
                'PostRelaseDate': post.date_utc,
                'CommentDate': c.created_at_utc,
                'CommetDescription': c.text,
                'CommentLike': c.likes_count,
                'ReplyCount': sum(1 for _ in comments) + 1,
            }
            db.insert_one(comment)

def get_data(L, db, inst_username):    
    profile = Profile.from_username(L.context, inst_username)

    PostFolowerPostShare = profile.followers
    PostFolowingPostShare = profile.followees
    PostCount = profile.mediacount
    all_posts = profile.get_posts()

    for one_post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, all_posts)):
    # for one_post in all_posts:
        InsPostlink = const.IG_URL + one_post.shortcode
        get_comments(db, one_post)
        """
        If object doesn't exists it will be added to database.-
        Other ways it won't.
        """
        db.posts_col()

        filter = {'InsPostlink': str(InsPostlink)}

        if not db.find_one(filter):
            print(filter)
            # Sleeep
            # insomnia = random.randint(1, 4)
            # print('\n~~~~Post Insomnia is:', insomnia)
            # time.sleep(insomnia)
            
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


    res = {
        'InsPageLink': const.IG_PROFILE + inst_username,
        'InsPageName': inst_username,
        'BioText': profile.biography,
        'FolowerAtUpdate': PostFolowerPostShare,
        'FolowingAtUpdate': PostFolowingPostShare,
        'PostCount': sum(1 for _ in all_posts) + 1,
        'SiteLink': profile.external_url
    }
    return res
