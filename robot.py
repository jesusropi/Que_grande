"""
	Create at ./ all paths as in www.quegrande.org and download and save all 
	documents in the same sort. 
"""
import os
import urllib2
import sys

from bs4 import BeautifulSoup


URL = 'http://quegrande.org/apuntes/ETIS/'


def get_content(url):
	"""Get content html from url"""
	request = urllib2.Request(url)
	if request is not None:
		open_req = urllib2.urlopen(request)
		html = open_req.read()
		return html
	else:
		print 'Error URL: %s' % url


def get_links(html):
	"""Get all a html tag from html page"""
	urls = []
	soup = BeautifulSoup(html, 'html.parser')
	links = soup.find_all('a')
	if links:
		for l in links:
			urls.append(l.get('href'))
	return urls[5:]	


def create_folder(directory):
	"""Create directory"""
	if not os.path.exists(directory):
		os.makedirs(directory)	


def save_doc(path, name_doc, link_doc):
	"""Download name_doc from link_doc and save it at ./path"""
	u = urllib2.urlopen(link_doc)
	content = u.read()
	f = open(os.path.join(path, name_doc), 'w')
	f.write(content)
	f.close()


def is_doc(url):
	"""True if url is a documents url"""
	path, ext = os.path.splitext(url)
	if ext:
		return True
	return False


def main(url):
	"""Searchs all next links from url"""
	father = None
	html = get_content(url)
	links = get_links(html)
	father = url
	if len(links) != 5: # Without links to itself page or back page
		for l in links:
			url_next = url
			if is_doc(l):
				print 'DOC: %s' % l
				save_doc(father, l, father + l)
			else:
				father = url_next
				url_next = url_next + l
				create_folder(father + l)
				print 'PATH: %s' % url_next
				main(url_next)
	else: # There isnt more steps
		print 'Final page whithout links: %s' % url

if __name__ == '__main__':
	main(URL)