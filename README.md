# Pyrsear

Pyrsear is a Command line based Web-Browser written in Python using BeautifulSoup4 library

  - Written in Python
  - Ignores js, could scan it in the future,
  - Great for sketchy pages you don't want to load in typically focused Browsers

### Version
v0.0.1

### Technology
Pyrsear uses only one other library to read the pages currently

* [BeautifulSoup4] - BeautifulSoup4 - Library in python to split apart HTML into objects

### Installation

You need: Python 2.7.x, BeautifulSoup4

```sh
$ pip install BeautifulSoup4
```
### Usage
```python
import pyrsear.py
prs = pyrsear
prs.bookmarks = ['https://bitcoin.org','https://google.com']
prs.parser(getPage(prs.bookmarks[0]), prs.bookmarks[0])
i = 0
print 'URL List:'
for row in prs.current_page_url_list:
    print '[' + str(i) + '] - ' + row['url'] + ' - Text: ' + row['text']
    i += 1
```
### Output
![alt text](http://i.imgur.com/iYHc9do.png "Output")

### Development
Want to contribute? Great!
Contact juju@protonmail.ch

### Todo's
 - Proxy Support 
 - Scan JS from pages
 - Reporting functionality
 - Coolness

License
----
MIT
[BeautifulSoup4]:http://www.crummy.com/software/BeautifulSoup/bs4/doc/

