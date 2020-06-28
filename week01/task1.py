import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

bs_info = bs(response.text, 'html.parser')

filmdic = []

counter = 0
movieList = []
for tag in bs_info.find_all('dd', ):
    for atag in tag.find_all('div', attrs={'class': 'movie-item film-channel'}):
        if counter < 10:
            counter += 1
            movie_title = atag.find('span', attrs={'class': 'name'}).text
            movie_link = 'https://maoyan.com' + atag.find('a', attrs={'data-act': 'movie-click'}).get('href')
            hover_tags = atag.find_all('span', attrs={'class': 'hover-tag'})
            movie_cat = hover_tags[0].next_sibling.strip()
            movie_time = hover_tags[2].next_sibling.strip()
            movie = movie_title.strip() + ', category: ' + movie_cat + ', online_time: ' + movie_time + ', link: ' + movie_link.strip()
            movieList.append(movie)
        else:
            break
moviefile= pd.DataFrame(data=movieList)
moviefile.to_csv('./moviefile.csv', encoding='utf8',
              index=False, header=False)

              
     