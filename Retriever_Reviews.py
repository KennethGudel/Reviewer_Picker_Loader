import requests
from HTMLParser import HTMLParser

header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
current_movie = ''
reviews = []
reviewers = []

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.recording_date = 0
        self.recording_reviewers = 0
        self.recording_reviews = 0
        self.recording_title = 0
        self.date = ''
        self.title = ''
        self.tag = [
            'metascore_w medium movie positive indiv perfect', 
            'metascore_w medium movie positive indiv', 
            'metascore_w medium movie mixed indiv', 
            'metascore_w medium movie negative indiv'
            ]

    def handle_starttag(self, tag, attributes):
        #using global variable over difficulty passing variable to parser
        global current_movie
        if self.recording_reviewers: self.recording_reviewers += 1
        if self.recording_reviews: self.recording_reviews += 1
        if self.recording_title: self.recording_title += 1  
        for name, value in attributes:
            if name == 'class' and value in self.tag:
                self.recording_reviews = 1
                return
            if name == 'class' and value == 'author':
                self.recording_reviewers = 1
      	        return
            if name == 'href' and value == current_movie:
      	        self.recording_title = 1
      	        return

    def handle_data(self, data):
        global reviewers, reviews
        if self.recording_date and data.strip() != '':
            self.date= data.strip()
            self.recording_date = 0
        if data == 'Release Date:':
        	self.recording_date = 1
        if self.recording_reviewers and data != 'Reviewed by:':
            reviewers.append(data)
        if self.recording_reviews:
   	        reviews.append(data)
        if self.recording_title and data != 'Summary':
            self.title = data.strip()

    def handle_endtag(self, tag):
        if self.recording_reviews:
            self.recording_reviews -= 1
        if self.recording_reviewers:
            self.recording_reviewers -= 1
        if self.recording_title:
            self.recording_title -= 1

# instantiate the parser
parser = MyHTMLParser()

def get_reviewer_list(movie, base = 'http://www.metacritic.com/movie/', critics_base = '/critic-reviews'):
    global current_movie, reviews, reviewers
    reviews = reviewers = []
	#using global variable over difficulty passing variable to parser
    current_movie = '/movie/' + movie
    banana = requests.get(base + movie + critics_base, headers = header)
    parser.feed(banana.text)
    return[parser.title, parser.date, reviewers, reviews]