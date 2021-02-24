import re
import json
import time
import os.path
import inspect
import configparser
import urllib.request
from selenium import webdriver

views = 10  # Number of time to play the video
wait = 0   # wait = 0, the script will wait the video length before reloading the page
video_array = ["ofMKdOFjZ0w", "ofMKdOFjZ0w"]  # video_id

driver_path = '/Users/roger-that/Documents/Roger-That/Dev/2-Drivers/Selenium_Drivers/chromedriver'
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
config = configparser.ConfigParser()
config.read(f'{path}/auth.ini')
api_key = config.get('credentials', 'GOOGLE_API_KEY')


def get_video_length(video_id, api_key):
    searchUrl = f'https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=contentDetails&part=snippet'
    response = urllib.request.urlopen(searchUrl).read()
    data = json.loads(response)
    all_data = data['items']
    video_title = all_data[0]['snippet']['title']
    contentDetails = all_data[0]['contentDetails']
    duration = contentDetails['duration'][2:]

    if re.search('H', duration):
        match = re.findall(r"(\d+)H(\d+)M(\d+)S", duration)
        seconds = int(match[0][0])*3600 + \
            int(match[0][1])*60 + int(match[0][2])
    elif re.search('M', duration):
        match = re.findall(r"(\d+)M(\d+)S", duration)
        seconds = int(match[0][0])*60 + int(match[0][1])
    else:
        match = re.findall(r"(\d+)S", duration)
        seconds = int(match[0])

    return {'seconds': seconds, 'duration': duration, 'title': video_title}


def run_viewer(video_id, views, google_chrome):
    video_obj = get_video_length(video_id, api_key)
    video_length_seconds = video_obj['seconds']
    video_title = video_obj['title']
    video_duration = video_obj['duration'].replace(
        'H', ':').replace('M', ':').replace('S', '')
    print(
        f'Title: {video_title} - {video_duration} ({video_length_seconds}s)')

    for i in range(views):
        print(f'View count: {i+1} of {views}')
        time.sleep(wait if wait else video_length_seconds)
        google_chrome.refresh()


def init():
    for video_id in video_array:
        print('Loading browser...')
        google_chrome = webdriver.Chrome(driver_path)
        google_chrome.get(f'https://www.youtube.com/watch?v={video_id}')
        time.sleep(10)
        google_chrome.refresh()
        run_viewer(video_id, views, google_chrome)
        google_chrome.close()
        time.sleep(1)


if __name__ == '__main__':
    init()
