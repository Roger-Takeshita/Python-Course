
#! Developed by Roger Takeshita
#! https://github.com/Roger-Takeshita

from authenticate import authenticate_user
from time import strftime, localtime
from imgurpython.helpers.error import ImgurClientError
import pyperclip
import sys

image_path = sys.argv[1]


def upload_image(data):
    """Uploads an image to imgur"""
    timestamp = strftime("%Y-%m-%d_%H:%M:%S", localtime())
    config = {
        'album': data['album'],
        'name': 'Dev_{0}'.format(timestamp),
        'title': 'Dev_{0}'.format(timestamp),
        'description': 'Image generated: {0}'.format(timestamp)
    }
    print('Uploading image...')
    image = data["client"].upload_from_path(
        image_path, config=config, anon=False)
    print('Done')
    return image


if __name__ == "__main__":
    try:
        data = authenticate_user()
        image = upload_image(data)
        pyperclip.copy(image['link'])
        print(image['link'])
    except (ImgurClientError, ValueError) as error:
        print(error)
