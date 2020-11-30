# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:49:39 2020

@author: Ray
"""

import requests
from bs4 import BeautifulSoup

#the important variables
dotwin = "https://thedonald.win"
html = requests.get(dotwin)
soup = BeautifulSoup(html.text, 'html.parser')
body = soup.body
#Get top 10 post titles
posts = soup.find_all('div', class_='post')
for i in range(10):
    print(posts[i].find('a', class_='title').text)
