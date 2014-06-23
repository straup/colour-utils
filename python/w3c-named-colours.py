#!/usr/bin/env python

import sys
import BeautifulSoup
import urllib
import json

def named_colours(url):

    rsp = urllib.urlopen(url)

    soup = BeautifulSoup.BeautifulSoup(rsp.read())
    table = soup.find('table', {'class': 'named-color-table'})
    
    palette = {}

    for tr in table.findAll('tr') :
        
        cells = tr.findAll('td')

        if not len(cells):
            continue

        name = cells[0]['style']
        hex = cells[1]['style']
            
        name = name.replace("background:", "")
        hex = hex.replace("background:", "")
            
        palette[ hex ] = { 'name': name }

    return palette

if __name__ == '__main__':

    url = 'http://dev.w3.org/csswg/css-color/'
    palette = named_colours(url)

    print json.dumps(palette, indent=2)
    sys.exit()
