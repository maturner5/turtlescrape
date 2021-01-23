# this is a file to make scraping the web easier by creating new functions
# to handle all the busy shit the scrape api does so you don't have to 
# remember anything.

from bs4 import BeautifulSoup 
from urllib.request import urlopen
import sys

# makes error message only one line
sys.tracebacklimit = 0 

url = 'https://www.marketwatch.com/investing/stock/tsla?mod=quote_search'
# function to search for text using html tags as arguments
def turtlescrape(url, *args, **kwargs):
    try:
        page = urlopen(url)
    except:
        print("Failed to load page. This is probably because the site you tried"                " to load doesn't allow you to scrape it.")
    text = page.read()
    soup = BeautifulSoup(text, 'html.parser')
    if (soup):
        for i in soup.findAll(*args, **kwargs):
            print(''.join(i.findAll(text=True)))
        return 0
    else:
        print("Failed to load soup.")
        return 1        

# to format args: 'h3'; to format kwargs: 'class_='value''
