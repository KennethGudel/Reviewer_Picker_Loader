from Retriever_Reviews import get_reviewer_list
from Retriever_Movies import get_movie_list
from JSON_format import make_json
from Loader import put, new_index, alias
from datetime import datetime
import string

def index():

	alias_name = 'banana'

	index_name = str(datetime.now()).lower().replace(' ', '_')
	print index_name	

	movie_list = get_movie_list()

	print 'creating index'

	if not new_index(index_name):
		print 'index creation failed'
		return

	print 'indexing'

	i = 1
	for movie in movie_list:
		movie_data = get_reviewer_list(movie)
		json_data = make_json(movie_data)
		put(json_data, index_name, i)
		i += 1

	alias(index_name, alias_name)

index()