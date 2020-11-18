
#! Developed by Roger Takeshita
#! https://github.com/Roger-Takeshita

from authenticate import authenticate_user, colors
from time import strftime, localtime
from imgurpython.helpers.error import ImgurClientError
import pyperclip
import sys

try:
    image_path = sys.argv[1]
except IndexError as error:
    print(f'{colors.red}ERROR:{colors.default} Please provide an image first.')
    exit()


def upload_image(data):
    """Uploads an image to imgur"""
    timestamp = strftime("%Y-%m-%d_%H:%M:%S", localtime())
    config = {
        'album': data['album'],
        'name': 'Dev_{0}'.format(timestamp),
        'title': 'Dev_{0}'.format(timestamp),
        'description': 'Image generated: {0}'.format(timestamp)
    }
    print(f'{colors.orange}Uploading image...{colors.default}')
    image = data["client"].upload_from_path(
        image_path, config=config, anon=False)
    print(f'{colors.green}Done!{colors.default}')
    return image


if __name__ == "__main__":
    try:
        data = authenticate_user()
        image = upload_image(data)
        link = image['link']
        pyperclip.copy(link)
        print(f'{colors.blue}{link}{colors.default}')
    except (ImgurClientError, ValueError) as error:
        if error == '(403) Invalid client_id ':
            print(f'{colors.red}ERROR:{colors.blue} CLIENT_ID{colors.default}')
        else:
            print(f'{colors.red}ERROR:{colors.default} {error}')
    except Warning as warning:
        print(warning)
