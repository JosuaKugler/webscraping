import sys
import urllib
import urllib.request
from bs4 import BeautifulSoup
import os
import time

basicurl = "https://www.synonyme.de/"


def get_html(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8", errors = "replace")
    fp.close()
    return mystr

def get_soup(url):
    return BeautifulSoup(get_html(url), "html.parser")

def main(word):
    newurl = basicurl + word + "/"
    soup = get_soup(newurl)
    body = soup.body
    divlist = body.find_all('div')

    synonymdivlist = []

    for div in divlist:
        try:
            #print(div["class"])
            if "synonymes" in div["class"]:
                synonymdivlist.append(div)
        except:
            pass
    synonymalist = []

    for div in synonymdivlist:
        synonymalist.append(div.find("a"))

    synonymlist = []
    for a in synonymalist:
        synonymlist.append(a["href"][1:-1])

    synonymlist = list(set(synonymlist))

    synonymlist.sort()
    return synonymlist



if __name__ == "__main__":
    word = sys.argv[1]
    synonymlist = main(word)
    for synonym in synonymlist:
        print(synonym)