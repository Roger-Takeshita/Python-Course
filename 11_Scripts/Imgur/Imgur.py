
#! Developed by Roger Takeshita
#! https://github.com/Roger-Takeshita

from authenticate import authenticate_user
from time import strftime, localtime
from imgurpython.helpers.error import ImgurClientError
from configparser import ConfigParser
import pyperclip
import os.path
import inspect
import sys

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
config = ConfigParser()
config.read(f'{path}/auth.ini')
album = config.get('album', 'ALBUM_ID') or None
image_path = sys.argv[1]


def upload_image(client):
    """Uploads an image to imgur"""
    timestamp = strftime("%Y-%m-%d_%H:%M:%S", localtime())
    config = {
        'album': album,
        'name': 'Dev_{0}'.format(timestamp),
        'title': 'Dev_{0}'.format(timestamp),
        'description': 'Image generated: {0}'.format(timestamp)
    }
    print('Uploading image...')
    image = client.upload_from_path(image_path, config=config, anon=False)
    print('Done')
    return image


if __name__ == "__main__":
    try:
        client = authenticate_user()
        image = upload_image(client)
        pyperclip.copy(image['link'])
        print(image['link'])
    except (ImgurClientError, ValueError) as error:
        print(error)
