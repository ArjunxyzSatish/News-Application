#!/usr/bin/python3

import pandas  as pd
import requests
from bs4 import BeautifulSoup

def football_news():
    page = requests.get('https://www.skysports.com/football/news')
    site = BeautifulSoup(page.content, 'html.parser')
    full = site.find(class_='site-layout-secondary block page-nav__offset grid')
    allnews = full.find_all(class_='news-list__headline')



    heading = [head.text.replace('\n', '') for head in allnews]
   
    news = pd.DataFrame(
            {
                'Category': heading,

            }
                        )
    pd.set_option('display.max_colwidth', -1)

    print(news)

def general_news():
    page = requests.get('https://inshorts.com/en/read/')
    full = BeautifulSoup(page.content, 'html.parser')
    news = full.find_all(itemprop="headline")
    headline = [head.text.replace('\n', ' ') for head in news]
    
    final = pd.DataFrame(
            {
             'News Headlines': headline
            }
                        )
    pd.set_option('display.max_colwidth', -1)
    print(final)

def in_detail(index): 
    page = requests.get('https://inshorts.com/en/read/')
    full = BeautifulSoup(page.content, 'html.parser')
    detail_all = full.find_all(itemprop="articleBody")
    print('\n')
    print(detail_all[index].text)
    print('\n')


print("NEWS APP")
print("1. FOOTBALL NEWS")
print("2. GENERAL NEWS")
print("3. EXIT")
option = int(input("Please select your option: "))

if option == 1:
    football_news()

elif option == 2:
    general_news()
    while True:
        head = input("Which headline would you like to read in detail?(Ctrl-C to exit): ")
        in_detail(int(head))

elif option == 3:
    print("Okay. Have a great day! :)")
