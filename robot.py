"""
	Create at ./output/ all paths as in www.quegrande.org and it save all documents
	in the same sort. 
"""
import os
import urllib2
import sys

from bs4 import BeautifulSoup


URL = 'http://quegrande.org/apuntes/ETIS/'
OUTPUT = 'output'


def get_content(url):
	request = urllib2.Request(url)
	if request is not None:
		open_req = urllib2.urlopen(request)
		html = open_req.read()
		return html
	else:
		print 'Error URL: %s' % url


def get_links(html):
	urls = []
	soup = BeautifulSoup(html, 'html.parser')
	links = soup.find_all('a')
	if links:
		for l in links:
			urls.append(l.get('href'))
	return urls[5:]	

#TODO
def create_folder(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)	

#TODO
def save_doc():
	pass

def is_doc(url):
	path, ext = os.path.splitext(url)
	if ext:
		return True
	return False

#TODO
def main(url):
	# 1. Dame contenido de url
	html = get_content(url)
	# 2. Dame enlaces de url
	links = get_links(html)
	# 3. Casos:
	#	3.1 Si solo 4 enlaces, fin. 
	#	3.2 Si no:
	#		- Por cada enlace:
	#			Si es documento, lo descarga: 
	#				+ Revisa si hay directorio de url, si no, lo crea
	#				+ Guarda ahi el documento
	#			Si es enlace:
	#				+ Crea path
	#				+ main(url)
	if len(links) != 5: # There isnt more steps
		for l in links:
			create_folder(l)
			url_next = url
			if is_doc(l):
				print 'DOC: %s' % l
				#save_doc(path, f)
			else:
				url_next = url_next + l
				print 'PATH: %s' % url
				main(url_next)
	else:
		print 'Final page whithout links: %s' % url

#TODO
if __name__ == '__main__':
	u = 'http://quegrande.org/apuntes/ETIS/'
	main(u)

	#main(URL)
	#doc = get_html('http://quegrande.org/apuntes/ETIS/1/Alx/teoria/07-08/tema_1_-_estructuras_algebraicas.pdf')
	#f = open('salida.pdf', 'wb')
	#f.write(doc)
	#f.close()