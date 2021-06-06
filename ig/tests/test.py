import json
import datetime

def export_json(result):
    """ Serializing json """
    with open('sample/output.json', 'w') as f:
        # json_object = json.dumps(result, ensure_ascii=False, indent=4)
        json.dump(result,
        f,
        ensure_ascii=False,
        indent=4,
        sort_keys=True,
        default=str)
a = [{'PostFolowerPostShare': 137, 'PostFolowingPostShare': 24, 'PostCount': 3, 'InfoUpdateDate': datetime.datetime(2021, 6, 6, 14, 49, 50, 116275), 'PostRelaseDate': datetime.datetime(2021, 5, 14, 12, 56, 54), 'InsPageLink': 'http://instagram.com/p/CO2qrVFBqsT', 'PostImagelink': 'https://instagram.fgyd4-1.fna.fbcdn.net/v/t51.2885-15/e35/184904968_1372455986487211_6126405076022640987_n.jpg?tp=1&_nc_ht=instagram.fgyd4-1.fna.fbcdn.net&_nc_cat=107&_nc_ohc=HfZpYA3tAlUAX-MKXh3&edm=ALQROFkBAAAA&ccb=7-4&oh=d17c457d2a6d3db9809812df030f1e19&oe=60C46BFF&_nc_sid=30a2ef&ig_cache_key=MjU3MzQzMTkzMjYxMjY4NDU2Mw%3D%3D.2-ccb7-4', 'PostLike': 19, 'PostComment': 0, 'PostDiscription': '.\nاین حس و حال، ارزش به اشتراک گذاشتن داره :)\n.\n#نِبیگ \n#فصل_تازه_کتاب'}, {'PostFolowerPostShare': 137, 'PostFolowingPostShare': 24, 'PostCount': 3, 'InfoUpdateDate': datetime.datetime(2021, 6, 6, 14, 49, 51, 609054), 'PostRelaseDate': datetime.datetime(2021, 5, 14, 12, 54, 3), 'InsPageLink': 'http://instagram.com/p/CO2qWefByUZ', 'PostImagelink': 'https://instagram.fgyd4-2.fna.fbcdn.net/v/t51.2885-15/e35/186797351_669063317247423_2161908913139365941_n.jpg?tp=1&_nc_ht=instagram.fgyd4-2.fna.fbcdn.net&_nc_cat=103&_nc_ohc=QpazK3DIsG4AX_-HQG3&edm=ALQROFkBAAAA&ccb=7-4&oh=f35b96a476702215a13b7b090c27fa54&oe=60C3913F&_nc_sid=30a2ef&ig_cache_key=MjU3MzQzMDQ5OTYwMzU4ODM3Nw%3D%3D.2-ccb7-4', 'PostLike': 21, 'PostComment': 2, 'PostDiscription': '.\nنِبیگ در حال آماده شدنه.\nما معتقدیم حس و حال کتاب خوندن، چه وقتی که در حال خواندنیم و چه زمانی که تمومش می\u200cکنیم\nبهترین و مفیدترین چیزی هست که می\u200cتونیم با دیگران به اشتراک بزاریم.\nپس نِبیگ میاد تا همین امکان رو به شما بده.\n.\n#نِبیگ \n#فصل_جدید_کتاب\n#کتاب #کتابخوانی_باهم #کتاب_خوب #کتابخوانی #یار_مهربان #استارتاپ'}, {'PostFolowerPostShare': 137, 'PostFolowingPostShare': 24, 'PostCount': 3, 'InfoUpdateDate': datetime.datetime(2021, 6, 6, 14, 49, 53, 576620), 'PostRelaseDate': datetime.datetime(2021, 5, 14, 12, 50, 34), 'InsPageLink': 'http://instagram.com/p/CO2p8-yh8fv', 'PostImagelink': 'https://instagram.fgyd4-2.fna.fbcdn.net/v/t51.2885-15/e35/185373933_2758242157772440_9010853836565159084_n.jpg?tp=1&_nc_ht=instagram.fgyd4-2.fna.fbcdn.net&_nc_cat=104&_nc_ohc=jiopFjmJeQEAX9SYP-H&edm=ALQROFkBAAAA&ccb=7-4&oh=1d8ed8d248bb5239473eed93c7d86800&oe=60C42FB8&_nc_sid=30a2ef&ig_cache_key=MjU3MzQyODc0NzU4NDEyOTAwNw%3D%3D.2-ccb7-4', 'PostLike': 17, 'PostComment': 0, 'PostDiscription': '.\nHello World :)'}]

export_json(a)