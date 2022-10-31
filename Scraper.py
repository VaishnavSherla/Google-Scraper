# Usage --
    # pip install requests-html
    # python Scraper.py

import os
from requests_html import HTMLSession

os.system('cls' if os.name == 'nt' else 'clear')

Query = input('Enter Your Query : ')
Limit = int(input('Enter No. Of Urls To Scrape : '))

file = open('Results.txt', 'w')

s = HTMLSession()

headers = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.5',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

params = {
    'q': Query,
    'num': Limit,
}

response = s.get('https://www.google.com/search', params=params)

if 'did not match any documents' in response.text:
    exit('No Results Found')
elif 'Our systems have detected unusual traffic from your computer' in response.text:
    exit('Captcha Triggered!\nUse Vpn Or Try After Sometime.')
else:
    links = list(response.html.absolute_links)
    for url in links[:]:
        if not 'google' in url:
            print(url)
            file.write(url+'\n')
