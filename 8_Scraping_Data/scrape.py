import requests
from bs4 import BeautifulSoup
import pprint

def sort_stories_by_votes(list):
    return sorted(list, key=lambda k: k['votes'], reverse = True);

def create_custom_hn():
    hn = []
    
    for i in range(1, 2):
        response = requests.get('https://news.ycombinator.com/news?p=' + str(i))
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.select('.storylink')
        votes = soup.select('.score')
        subtext = soup.select('.subtext')

        for idx, item in enumerate(links):
            title = item.getText()
            href = item.get('href', '')
            vote = subtext[idx].select('.score')

            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))

                if points > 99:
                    hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn())