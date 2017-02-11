import requests
from bs4 import BeautifulSoup

def processURL(URL):
        http = requests.get(URL)
        soup = BeautifulSoup(http.content, "html.parser")
        return soup

print(processURL("http://www.imdb.com/list/ls006266261/"))