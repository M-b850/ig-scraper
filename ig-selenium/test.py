import requests

p = 'https://scontent-sof1-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/s750x750/213266039_401194054626389_8409422865125462248_n.jpg?_nc_ht=scontent-sof1-1.cdninstagram.com&_nc_cat=105&_nc_ohc=-sxCRp0y858AX84fFGd&edm=APU89FABAAAA&ccb=7-4&oh=54418f2952f0ab42ec69a48f4cf117f9&oe=60F13FC8&_nc_sid=86f79a'
filename = 'hloas.jpg'

def download(url, name):
    session = requests.Session()
    r = session.get(url)
    with open(name, 'wb') as outfile:
        outfile.write(r.content)

download(p, filename)