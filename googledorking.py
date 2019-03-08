#! usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import requests
import urllib
import json
import re
from bs4 import BeautifulSoup

"""

parser = argparse.ArgumentParser(description='Scanner de Sqlmap + Google Dorking')
parser.add_argument("-t", "--tor", help="Utilizar anonimáto", action="store_true")
parser.add_argument("-d","--dork", help="Dork a ejecutar", required=True)
parser.add_argument("-f", "--file", help="Nombre de archivo de salida")
args = parser.parse_args()

#UTILIZAR ANONIMATO
if args.tor:
	print args.tor
if args.dork:
	print "El Dork es "+args.dork
if args.file:
	print "Fichero "+args.file

"""


urls = set()
urlgoogle = 'http://www.google.com/search'
dork='inurl:gallery.php?id='
#payload = {'q':args.dork,'start':'0'}
payload = {'q':dork,'start':'0'}
user_agent = { 'User-agent' : 'Mozilla/11.0' }
r = requests.get(urlgoogle, params = payload, headers = user_agent )
soup = BeautifulSoup( r.text, 'html.parser' )
h3tags = soup.find_all( 'h3', class_='r' )
for h3 in h3tags:
    try:
        url = re.search('url\?q=(.+?)\&sa', h3.a['href']).group(1)
	url = urllib.unquote(url).decode('utf8')
	urls.add(url)
	
    except:
        continue






