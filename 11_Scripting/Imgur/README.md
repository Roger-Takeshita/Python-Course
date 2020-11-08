<h1 id='contents'>Table of Contents</h1>

- [IMGUR](#imgur)
  - [Setup](#setup)
    - [Packages](#packages)
    - [Imgur Keys](#imgur-keys)
    - [auth.ini](#authini)
      - [Pin](#pin)
      - [Tokens](#tokens)
      - [Album Id](#album-id)
  - [Imgur App](#imgur-app)
    - [Alias](#alias)

# IMGUR

- Custom image uploader to [imgur.com](imgur.com) using Imgur's API

## Setup

### Packages

[Go Back to Contents](#contents)

- Install the following python packages

  ```Bash
    pip install imgurpython
    pip install pyperclip
    pip install configparser
  ```

### Imgur Keys

[Go Back to Contents](#contents)

- Register a new application

  - On [https://api.imgur.com/oauth2/addclient](https://api.imgur.com/oauth2/addclient)

    - Application name: `Image Uploader`
    - Authorization: `OAuth2 authorization without callback URL`
    - Application website (optional)
    - Email: `your_email@email.com`
    - Description: `Image Uploader`
    - Click on **Submit**

      ![](https://i.imgur.com/7JaFwB4.png)

  - Copy `Client ID` and `Client secret`

    - Client ID: `7446947c8b38f2c`
    - Client secret: `28f7ebbc6d16488b05159adc3da37370e4fed1b6`

      ![](https://i.imgur.com/tS6CeOC.png)

### auth.ini

[Go Back to Contents](#contents)

- Create a new file `auth.ini` file

  ```Bash
    touch auth.ini
  ```

- in `auth.ini`

  - Final configuration

    ```Bash
      [credentials]
      CLIENT_ID=c8b4e28d514f55f
      CLIENT_SECRET=a6d3b54b2ca7d773280517cc7fc20248796e95b1
      PIN=da4daab8d4
      ACCESS_TOKEN=5fbbd0042c05bcebc574cc97895b7771fade606b
      REFRESH_TOKEN=a2bd6b1034c9fb32e1385fc966407a7ab811fe2f

      [album]
      ALBUM_ID=xC3vltP
    ```

#### Pin

[Go Back to Contents](#contents)

- When we first run the script, our `PIN` is an empty string and will give us the following message

  ![](https://i.imgur.com/RJPM22B.png)

- Accessing the link `https://api.imgur.com/oauth2/authorize?client_id=c8b4e28d514f55f&response_type=pin`

  - Click on **allow**

    ![](https://i.imgur.com/ytI7bfg.png)

  - This will generate a new **pin**

    - This **pin** is an unique pin and can only be used once. The pin is responsible to authenticate our request to generate the `ACCESS_TOKEN` and `REFRESH_TOKEN`

    ![](https://i.imgur.com/T6Hnsz0.png)

#### Tokens

[Go Back to Contents](#contents)

- After adding our **pin** in our `auth.ini`. We can ran the same command again

  - this will generate our tokens

    ```Bash
      ACCESS_TOKEN=5fbbd0042c05bcebc574cc97895b7771fade606b
      REFRESH_TOKEN=a2bd6b1034c9fb32e1385fc966407a7ab811fe2f
    ```

    ![](https://i.imgur.com/kW0hKIa.png)

#### Album Id

[Go Back to Contents](#contents)

- If we don't specify an album, this means the photo will be **public**
- If we specify an album this means the photo is **private**
- To find an **album id** we need to inspect imgur page

  ![](https://i.imgur.com/JfnpgbL.png)

  ![](https://i.imgur.com/bHkh0K7.png)

## Imgur App

[Go Back to Contents](#contents)

- Run `python3 Imgur.py path/filename.png`

  - The link `https://i.imgur.com/j1kLhBo.png` is automatically copied to clipboard.

    ![](https://i.imgur.com/lglpz1Z.png)

### Alias

[Go Back to Contents](#contents)

- zshell alias
- in `~/.zshrc`

  ```Bash
    alias @img='python3 your_path/Imgur.py'
  ```

  ![](https://i.imgur.com/hHMJO8n.png)
