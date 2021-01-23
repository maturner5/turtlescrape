# turtlescrape

This is a very simple project to make scraping websites easier so you don't have to type all of the code for the library yourself.

This project uses these libraries: BeautifulSoup4, urllib.request and sys.

## Install
Command:
```sh
pip install turtlescrape
```
You must also have BeautifulSoup4 installed.

## Usage
Right now this project only has one function: turtlescrape().

To call it simply
```python
from turtlescrape import turtlescrape

turtlescrape(url, *args, **kwargs)
```
Look at the example project in order to get a feel for it.

## Notice
This project is most definetly broken in ways. But we all start somewhere, so input is definetly appreciated.

Not all websites let you scrape them. I have yet to figure out a workaround for that problem so in the meantime this code just throws up an error.
