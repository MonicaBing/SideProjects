#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:23:39 2020

"""

from bs4 import BeautifulSoup as bs 
import pandas as pd
pd.set_option('display.max_colwidth',500)
import time 
import requests
import random


urls = [f"http://quotes.toscrape.com/page/{i}/" for i in range (1,11)]

rate = [i/10 for i in range (10)]

quotes = []
authors = []


for url in urls:
    page = requests.get(url)
    soup = bs(page.content)
    authors.extend([i.text for i in soup.find_all(class_='author')])
    quotes.extend([i.text for i in soup.find_all(class_='text')])
    
    if len(quotes) >= 52:
        break
    time.sleep(random.choice(rate))

df = pd.DataFrame()
df['Authors'] = authors
df['Quotes'] = quotes
