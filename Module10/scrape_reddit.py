from bs4 import BeautifulSoup as BS
import urllib2

test_url = urllib2.urlopen("http://www.reddit.com")
readhtml = test_url.read()
test_url.close()

soup = BS(readhtml)
first_10_a_tags = soup.find_all("a", limit=10)

for links in first_10_a_tags:
    print links.get('href')