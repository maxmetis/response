# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:54:57 2020

@author: Johnny TSai
"""


import requests
from bs4 import BeautifulSoup

url = 'https://response.jp/category/business/latest/'

headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4122.7 Mobile Safari/537.36'}

response = requests.get(url, headers=headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'lxml')

title_list = []
link_list = []

for i in range(5):
    data = soup.find_all('section')[i]
    title = data.find('h2').text.replace('\u3000',' ')
    link = data.find('a').get('href')
    link = 'https://response.jp/' + link
    title_list.append(title)
    link_list.append(link)

def lineNotifyMessage(token, msg):
   headers = {
       "Authorization": "Bearer " + token, 
   }
	
   payload = {'message': msg}
   r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
   return r.status_code
	
message0 = '\n' + title_list[0] + '\n' + link_list[0]
message1 = '\n' + title_list[1] + '\n' + link_list[1]
message2 = '\n' + title_list[2] + '\n' + link_list[2]
message3 = '\n' + title_list[3] + '\n' + link_list[3]
message4 = '\n' + title_list[4] + '\n' + link_list[4]
           
token = ''

lineNotifyMessage(token, message0)
lineNotifyMessage(token, message1)
lineNotifyMessage(token, message2)
lineNotifyMessage(token, message3)
lineNotifyMessage(token, message4)
