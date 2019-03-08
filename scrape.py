import pandas as pd
import numpy
import string
import requests
import bs4 as bs # beautiful soup for web scraping

# list for appending links to
link_list = []
text_body = ''
url = 'https://www.springfieldspringfield.co.uk/'
html = requests.get('https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=silicon-valley-2014')
soup = bs.BeautifulSoup(html.text, 'html.parser')
for link in soup.find_all('a', class_="season-episode-title"):
    # grab the links from a tags
    link_list.append(link.get('href'))
    text = requests.get('{}{}'.format(url, link.get('href')))
    transcripts = bs.BeautifulSoup(text.text, 'html.parser')
    scripts = transcripts.find('div', class_="scrolling-script-container")
    text_body += scripts.get_text()
all_text = text_body.replace('-', '')
with open('SV-text-file.txt', 'w+') as file:
    file.write(all_text)
