# All functions related to collecting data are here.
from instaloader import Instaloader, Profile
import datetime
import const
from os.path import dirname


DIR = dirname(dirname(__file__))
res = []

def file_name(realse_date: datetime):
    suffix = '_'
    realse_date = realse_date.replace(':', '_').replace(' ', '_')
    return realse_date

def get_data(L, db: object, inst_username: str) -> list[dict]:
    print(inst_username)
    profile = Profile.from_username(L.context, inst_username)

    PostFolowerPostShare = profile.followers
    PostFolowingPostShare = profile.followees
    PostCount = profile.mediacount
    all_posts = profile.get_posts()
    for one_post in all_posts:
        each_post = {
            'InfoUpdateDate': datetime.datetime.utcnow(),
            'InsPageLink': const.IG_PROFILE + inst_username,
            'PostFolowerPostShare': PostFolowerPostShare,
            'PostFolowingPostShare': PostFolowingPostShare,
            'PostCount': PostCount,
            'RelaseDate': one_post.date_utc,
            'InsPostlink': const.IG_URL + one_post.shortcode,
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
        
        # Insert to Database
        """
        If object exists it would be found and be deleted after that -
        it will be inserted again.
        """
        filter = {'InsPostlink': each_post['InsPostlink']}
        if not db.find_one(filter):
            db.insert_one(each_post)
        
        res.append(each_post)
    return res
