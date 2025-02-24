# Import Libraries
from bs4 import BeautifulSoup
import requests

import cloudscraper
import json

def main():
    url = "https://www.coinbase.com/ventures"

    scraper = cloudscraper.create_scraper(browser={
        'browser': 'chrome',
        'platform': 'android',
        'desktop': False
    })  # returns a CloudScraper instance

    Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
    html = scraper.get(url).text
    
    soup = BeautifulSoup(html, 'html.parser')

    # find script tag with id "server-app-state"
    script = soup.find('script', id='server-app-state')
    # replace </script
    script = str(script)

    script = script.replace('</script>', '')
    # replace <script id="server-app-state" type="application/json">
    script = script.replace('<script id="server-app-state" type="application/json">', '')

    data = json.loads(script)
    print(data)
    data1 = []

    # print(data['initialData']['data']['content']['fields']['content'][2]['fields']['content'][0]['fields']['content'][0])
    for asset in data['initialData']['data']['content']['fields']['content'][2]['fields']['content'][0]['fields']['content']:
        asset = asset['fields']

        title = asset['title']
        subtitle = asset['subtitle']
        url = asset['url'].replace('\u002F', '/')
        image = "https:" + asset['image']['fields']['file']['url'].replace('\u002F', '/')

        # asset = Assets(company=fk, name=title, url=url, image=image)
        data1.append(asset)

    print(data1)

main()