
#! Developed by Roger Takeshita
#! https://github.com/Roger-Takeshita

from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
import configparser
import os.path
import inspect

filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
config = configparser.ConfigParser()
config.read(f'{path}/auth.ini')

class colors:
    default='\033[39m'
    red='\033[31m'
    green='\033[32m'
    blue='\033[34m'
    orange='\033[38;5;202m'


def authenticate_user():
    try:
        pin = config.get('credentials', 'PIN')
        client_id = config.get('credentials', 'CLIENT_ID')
        client_secret = config.get('credentials', 'CLIENT_SECRET')
        access_token = config.get('credentials', 'ACCESS_TOKEN')
        refresh_token = config.get('credentials', 'REFRESH_TOKEN')
        album = config.get('album', 'ALBUM_ID') or None
        client = ImgurClient(client_id, client_secret)

        if refresh_token == '':
            try:
                credentials = client.authorize(pin, 'pin')
                access = credentials['access_token']
                refresh = credentials['refresh_token']
                raise Warning(
                    f'{colors.blue}ACCESS_TOKEN={colors.default}{access} {colors.blue}REFRESH_TOKEN={colors.default}{refresh}')
            except ImgurClientError as error:
                print(f'{colors.red}ERROR:{colors.default} Invalid pin {colors.orange}{pin}{colors.default}')
                authorization_url = client.get_auth_url('pin')
                raise Warning(
                    f'Please visit {colors.blue}{authorization_url}{colors.default} to generate a new pin.')
        else:
            client.set_user_auth(access_token, refresh_token)
            return {
                "client": client,
                "album": album
            }

    except configparser.NoOptionError:
        raise ValueError(f'{colors.red}ERROR:{colors.blue} CLIENT_ID{colors.default}/{colors.blue}CLIENT_SECRET{colors.default} not found.')

    except configparser.NoSectionError:
        raise ValueError(f'{colors.red}ERROR:{colors.orange} auth.ini{colors.default} not found.')

    except TypeError as error:
        raise ValueError(error)


if __name__ == '__main__':
    authenticate_user()
