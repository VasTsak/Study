# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os 
os.chdir("/home/vasilis/github/Work_study/Text")

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

###### Making Web Requests ######

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)
    
    
strava_profile = simple_get("https://www.strava.com/athletes/44711221")

len(strava_profile)

html = BeautifulSoup(strava_profile, 'html.parser')

for p in html.select('page container'):
    if p['id'] == 'walrus':
        print(p.text)
        
        
for i, d in enumerate(html.find_all('div')):
    if "view" in str(d):
        print(i, d)
    
    if "page container" in str(d):
        print(i, d)
    if "id=\"athlete-profile\"" in str(d):
        print(i, d)
        
for i, li in enumerate(html.select('div')):
    print(i, li.text)
    
html.title
html.title.string
html.title.parent.name
html.div['class'][0]

for i, d in enumerate(html.find_all('div')):
    if "class=\"container smartbanner-content pt-md pb-md affix\"" in d:
        print(i, d)
        
        
html.get_text()
os.chdir("/home/vasilis/github/Work_study/Text/data_collection")
file1 = open("/home/vasilis/github/Work_study/Text/data_collection/myfile.txt","w") 
file1.write(html.get_text()) 
file1.close() 
