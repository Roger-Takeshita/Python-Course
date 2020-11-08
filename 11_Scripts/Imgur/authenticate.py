
#! Developed by Roger Takeshita
#! https://github.com/Roger-Takeshita

import configparser
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError

config = configparser.ConfigParser()
config.read('auth.ini')


def authenticate_user():
    try:
        pin = config.get('credentials', 'PIN')
        client_id = config.get('credentials', 'CLIENT_ID')
        client_secret = config.get('credentials', 'CLIENT_SECRET')
        client = ImgurClient(client_id, client_secret)
        access_token = config.get('credentials', 'ACCESS_TOKEN')
        refresh_token = config.get('credentials', 'REFRESH_TOKEN')

        if refresh_token == '':
            try:
                credentials = client.authorize(pin, 'pin')
                access = credentials['access_token']
                refresh = credentials['refresh_token']
                raise ValueError(
                    f'ACCESS_TOKEN={access} REFRESH_TOKEN={refresh}')
            except ImgurClientError as error:
                print(f'ERROR: Invalid pin {pin}')
                authorization_url = client.get_auth_url('pin')
                raise ValueError(
                    f'Please visit {authorization_url} to generate a new pin.')
        else:
            client.set_user_auth(access_token, refresh_token)
            return client

    except configparser.NoOptionError:
        raise ValueError('ERROR: CLIENT_ID/CLIENT_SECRET not found.')

    except configparser.NoSectionError:
        raise ValueError('ERROR: auth.ini not found.')

    except TypeError as error:
        raise ValueError(error)


if __name__ == '__main__':
    authenticate_user()
