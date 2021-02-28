<h1 id='table-of-contents'>TABLE OF CONTENTS</h1>

- [YOUTUBE VIEWS](#youtube-views)
  - [YouTube API Key](#youtube-api-key)
  - [Packages](#packages)
  - [Files](#files)
  - [Configuration](#configuration)
  - [Run YouTube_Views.py](#run-youtube_viewspy)

# YOUTUBE VIEWS

## YouTube API Key

[Go Back to Contents](#table-of-contents)

Create a new Google API KEY

- [https://console.developers.google.com/cloud-resource-manager](https://console.developers.google.com/cloud-resource-manager)
- On `Manage resources` page

  - Click on **CREATE PROJECT**

    ![](https://i.imgur.com/Lsay651.png)

- On `New Project` page

  - Project name\*: `youtube-views`
  - Click on **CREATE**

    ![](https://i.imgur.com/rI2GyMW.png)

- Open up the sidebar menu

  ![](https://i.imgur.com/AYi1Wng.png)

  - Select `APIs & Services > Dashboard`

    ![](https://i.imgur.com/Upnke5w.png)

- On `APIs & Services` page

  - Select your project (`youtube-views`)
  - Click on **+ ENABLE APIS AND SERVICES**

    ![](https://i.imgur.com/yce89hA.png)

- Search for `youtube`

  - Click on `YouTue Data API v3`

    ![](https://i.imgur.com/PxiH7ig.png)

  - Then click on **ENABLE**

    ![](https://i.imgur.com/0btpYAh.png)

- On `YouTube Data API v3 Overview` page

  - Click on **CREATE CREDENTIALS**

    ![](https://i.imgur.com/SyBSrso.png)

- On `Credentials` page

  - Select:
    - `YouTube Data API v3`
    - `Other UI (e.g. Windows, CLI Tools)`
    - `Public Data`
  - Click on **What credentials do I need?**

    ![](https://i.imgur.com/6ZlRcUi.png)

  - Copy Your API key

    - Click on **Done**

    ![](https://i.imgur.com/MuZDxo4.png)

  - Edit our new `API key 1`

    ![](https://i.imgur.com/dGIk6R0.png)

    - Restrict our API key to only have access to our `YouTube Data API v3`
    - Click on **SAVE**

      ![](https://i.imgur.com/laFSaOY.png)

![](https://i.imgur.com/7KOsisq.png)

## Packages

[Go Back to Contents](#table-of-contents)

**Install Selenium**

```Bash
  pip3 install selenium
```

**Download Selenium Driver**

- We are going to use `Chrome`
- Check `Chrome` version

  - Go to `Chrome Settings > Help > About Google Chrome`

    ![](https://i.imgur.com/uXy2cRP.png)

  - In my case it is version `88`

    ![](https://i.imgur.com/KCduAjN.png)

- [Download Selenium Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

  ![](https://i.imgur.com/2WDIq8g.png)

## Files

[Go Back to Contents](#table-of-contents)

Create `auth.ini` file in the same folder of the `YouTube_Views.py`

```Bash
  touch auth.ini
```

In `auth.ini`

- Add your API key

  ```Bash
    [credentials]
    GOOGLE_API_KEY=AIzaSyA0YLfi2YN3loZTwuKq3L5dQFtItvK6sMk
  ```

## Configuration

[Go Back to Contents](#table-of-contents)

In `YouTube_Views.py`

- We have the following custom fields:

  - `views`, number of times that you want to play the video
  - `wait`, number of seconds before reloading the page. `0` means that the script will play the entire video before refreshing the page
  - `speed`, playback speed
  - `mute`, no sound (the value is a string `'true'` or `'false'`)
  - `hide_browser`, if you want to run the browser in the background (`True/False` - Title case, python boolean)
  - `video_array`, add multiple videos using an array of strings separated by comma e.g. `['video_id_1', 'video_id_2', ...]`
  - `driver_path`, path to your chrome driver

  **NOTE:** From my tests the `wait/speed` doesn't seem to increase the number view. This means that you have to play the entire video to increase the number of views (not 100% tested).

```Python
  views = 10  # Number of time to play the video
  wait = 0   # wait = 0, the script will wait the video length before reloading the page
  speed = 1  # 1-16, 1 = normal playback
  mute = 'true'  # true/false - type string (all lowercase)
  hide_browser = True  # True/False - type boolean (Title case)
  video_array = ['ofMKdOFjZ0w']  # video_id
  driver_path = '/Users/roger-that/Documents/Roger-That/Dev/2-Drivers/Selenium_Drivers/chromedriver'
```

## Run YouTube_Views.py

[Go Back to Contents](#table-of-contents)

On `Terminal`

```Bash
  python path_to/YouTube_Views.py
  # Loading Browser... 1s
  # Loading Browser... 2s
  # Loading Browser... 3s
  # Loading Browser... 4s
  # Loading Browser... 5s
  # Loading Browser... 6s
  # Loading Browser... 7s
  # Loading Browser... 8s
  # Loading Browser... 9s
  # Loading Browser... 10s
  # Title: Dog Feeder 2.0 - 1:32 (92s) - Speed: 1x
  # View count: 1 of 10
  # View count: 2 of 10
  # View count: 3 of 10
  # View count: 4 of 10
  # View count: 5 of 10
```

- The script will wait 10 seconds to load the browser
- Then it will use the API to get the video information
