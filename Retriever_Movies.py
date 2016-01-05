import requests
import string
from HTMLParser import HTMLParser
import elasticsearch

header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
movies = []
forward = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
		global movies
		global forward
        # Only parse the 'anchor' tag.
		if tag == "a":
           # Check the list of defined attributes.
			for name, value in attrs:
				# If href is defined, print it.
				if name == "href":
					if value[0:7] == '/movie/':
						movies.append(value[7:])
		if tag == 'p':
			for name, value in attrs:
				if value == 'no_data':
					forward.append(True)

# instantiate the parser
parser = MyHTMLParser()

def get_movies(html):
	parser.feed(html)

def get_movie_list():
	global movies 
	global forward
	movies = []
	forward = []
	base = 'http://www.metacritic.com/browse/movies/title/dvd'
	page_base = '?page='
	letters = [letter for letter in string.ascii_lowercase]
	letters.append('')
	letters = ['']
	s = requests.session()
	for letter in letters:
		print letter
		forward.append(False)
		url = base + '/' + letter
		page = s.get(url, headers=header)
		get_movies(page.text)
		number = 1
		while forward[-1] == False:
			print number
			url_page = url + page_base + str(number)
			page = s.get(url_page, headers=header)
			get_movies(page.text)
			number += 1
	return movies
