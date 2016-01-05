from Retriever_Reviews import get_reviewer_list
from Retriever_Movies import get_movie_list
from JSON_format import make_json
from Loader import put, new_index, alias
from datetime import datetime
import string
import argparse
from elasticsearch import Elasticsearch, RequestsHttpConnection

#command line parser
parser = argparse.ArgumentParser(description = 'Loads metacritic reviewer into elasticsearch')
parser.add_argument('-p', '--port', help = 'The elasticsearch port, defaults to 9200', type=int, default=9200)
parser.add_argument('-i', '--index', help = 'The name given to the elasticsearch index, defaults to datetime.now()')
parser.add_argument('-a', '--alias', help = 'The name given to the elasticsearch alias, defaults to "banana"', default='banana')
args = parser.parse_args()

def index():

	#connect to elasticsearch
	es = Elasticsearch(connection_class=RequestsHttpConnection, port=args.port)

	if args.index: index_name = args.index
	else: index_name = str(datetime.now()).lower().replace(' ', '_')
	print 'index name: ' + index_name	

	movie_list = get_movie_list()

	print 'creating index'

	if not new_index(index_name, es):
		print 'index creation failed'
		return

	print 'indexing'

	i = 1
	for movie in movie_list:
		movie_data = get_reviewer_list(movie)
		json_data = make_json(movie_data)
		put(json_data, index_name, i, es)
		i += 1

	alias(index_name, args.alias, es)

index()