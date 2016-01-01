from urllib import FancyURLopener
import string
from HTMLParser import HTMLParser
import elasticsearch

#
class MyOpener(FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
myopener = MyOpener()

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
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

def get_movie_list(letters, base, page_base):
	for letter in letters:
		print letter
		forward.append(False)
		url = base + '/' + letter
		page = myopener.open(url)
		get_movies(page.read())
		number = 1
		while forward[-1] == False:
			print number
			url_page = url + page_base + str(number)
			page = myopener.open(url_page)
			get_movies(page.read())
			number += 1
	return set(movies)

movies = []
forward = []

base = 'http://www.metacritic.com/browse/movies/title/dvd'
page_base = '?page='


letters = [letter for letter in string.ascii_lowercase]
letters.append('')

get_movie_list(letters, base, page_base)

print len(movies)