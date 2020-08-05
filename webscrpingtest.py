'''
Created on Dec 23, 2019

@author: natra
'''
import requests
from bs4 import BeautifulSoup
vg='https://www.tripadvisor.com/Restaurant_Review-g46392-d1060844-Reviews-Veggie_Heaven-Denville_Morris_County_New_Jersey.html#REVIEWS'
nga='https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'
page = requests.get(nga)
print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
# Remove bottom links
last_links = soup.find(class_='AlphaNav')
last_links.decompose()

artist_name_list = soup.find(class_='BodyText')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.text,':' ,artist_name['href'])