# this is an example of how to use turtlescrape :)
from turtlescrape import turtlescrape

url = 'https://www.marketwatch.com/investing/stock/tsla?mod=quote_search'

turtlescrape(url, class_="value", field="Last")

# for the arguments, the url goes first and then you just start listing tags
# until you get the value you're looking for. Class tags must be listed
# as 'class_' because class is a reserved word in python.
