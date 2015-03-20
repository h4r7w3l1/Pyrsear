__author__ = 'chasej'
import urllib2
from bs4 import BeautifulSoup
from urlparse import urlparse

uibar = '--------------------------------------------------------'

# Use a dictionary to store our Bookmark List for the time being
bookmarks = ['https://news.ycombinator.com/', 'http://bitcoin.org', 'http://news.ycombinator.com',
             'http://news.google.com']

current_site = bookmarks[1]
current_page_url_list = []
current_page_title = 'None'

#Takes in unparsed html and the URL to the website
def parser(unparsedhtml, site):
    #create a soup object of the unparsedhtml
    soup = BeautifulSoup(unparsedhtml)

    current_page_title = str(soup.title.get_text())
    for link in soup.find_all('a'):
        if link.get('href'):
            url = link.get('href')
            #Create a parsed url object from the href
            parsnip = urlparse(url)
            #No URL Scheme http or https
            if parsnip[0] == '':
                if parsnip[1] == '':
                    print parsnip.geturl()
            if url[0] == '/':
                url = site + url
            if url[0] == '#':
                url = site + '/' + url
            url_dictionary = {'url': url, 'text': link.get_text()}
            current_page_url_list.append(url_dictionary)
    return 1


#Get page no proxies
def getPage(URL):
    response = urllib2.urlopen(URL)
    html = response.read()
    return html


parser(getPage(current_site), current_site)
i = 0

print 'URL List:'
for row in current_page_url_list:
    print '[' + str(i) + '] - ' + row['url'] + ' - Text: ' + row['text']
    i += 1
