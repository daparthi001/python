from bs4 import BeautifulSoup as BS, SoupStrainer as SS
import requests

url = "http://www.imdb.com/search/title"

# genres=action&languages=en&release_date=2015,2016&user_rating=7.5,

params = dict()
params['genres'] = 'action'
params['user_rating'] = '8.0,'
params['release_date'] = '2016-11-01,'

resp = requests.get(url, params=params)

print resp.url#, resp.content
print
ss = SS('a')
soup = BS(resp.content, 'html.parser', parse_only=ss)
resp.close()

#print soup
#print soup.find_all(title="Inside Out (2015)")#Mission: Impossible - Rogue Nation (2015)")

#fl = open('movie_titles','w')
for movie_title in soup.find_all('a'):
    print movie_title.string

#fl.close()