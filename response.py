# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 11:35:08 2020

@author: ultsai
"""

import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

url_pc= 'https://response.jp/category/motorcycle/latest'
response_pc = requests.get(url_pc, headers=headers)
response_pc.raise_for_status()
soup = BeautifulSoup(response_pc.text, 'lxml')
data = soup.find('div', 'news-list')

title = [item.find('h2').text.replace('\u3000',' ') for item in data.find_all('section')][:5]
link = [item.find('a').get('href') for item in data.find_all('section')][:5]
img = [item.find('img').get('src') for item in data.find_all('section')][:5]

#https://response.jp/
#https://response.jp/category/motorcycle/latest