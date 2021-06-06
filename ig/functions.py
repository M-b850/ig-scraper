# All functions related to collecting data are here.
from instaloader import Instaloader, Profile
import datetime
import const
res = []

def get_data(L, inst_username: str) -> list[dict]:
    profile = Profile.from_username(L.context, inst_username)

    PostFolowerPostShare = profile.followers
    PostFolowingPostShare = profile.followees
    PostCount = profile.mediacount

    all_posts = profile.get_posts()
    for one_post in all_posts:
        each_post = {
            'PostFolowerPostShare': PostFolowerPostShare,
            'PostFolowingPostShare': PostFolowingPostShare,
            'PostCount': PostCount,
            'InfoUpdateDate': datetime.datetime.utcnow(),
            'PostRelaseDate': one_post.date_utc,
            'InsPageLink': const.IG_URL + one_post.shortcode,
            'PostImagelink': one_post.url,
            'PostLike': one_post.likes,
            'PostComment': one_post.comments,
            'PostDiscription': one_post.caption,
        }
        res.append(each_post)
    return res
