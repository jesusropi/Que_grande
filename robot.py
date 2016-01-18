import urllib2
import sys

from bs4 import BeautifulSoup


URL = 'http://quegrande.org/apuntes/ETIS/'
OUTPUT = 'output'


def get_html(url):
	req = urllib2.Request(url)
	r = urllib2.urlopen(req)
	page = r.read()
	return page


#TODO
def is_doc(url):
	"""True if the next step is a final document"""
	pass

#TODO
def get_next_steps(html):
	"""Return list of next urls"""
	urls = []

#TODO
def get_all_docs(url):
	"""Download all documents"""
	html = get_html(url)
	steps = get_next_steps(html)
	for s in steps:
		get_all_docs(s)


def main(url):
	get_all_docs(url)

#TODO
if __name__ == '__main__':
	u = 'http://quegrande.org/apuntes/ETIS'
	request = urllib2.Request(u)
	r = urllib2.urlopen(request)
	html = r.read()
	soup = BeautifulSoup(html, 'html.parser')
	links = soup.find_all('a')
	if len(links) > 4:
		links = links[5:]
		for l in links:
			print l
	else:
		print 'Error: number of links!'

	#main(URL)
	#doc = get_html('http://quegrande.org/apuntes/ETIS/1/Alx/teoria/07-08/tema_1_-_estructuras_algebraicas.pdf')
	#f = open('salida.pdf', 'wb')
	#f.write(doc)
	#f.close()