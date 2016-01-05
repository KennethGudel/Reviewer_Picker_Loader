from Retriever_Reviews import get_reviewer_list
from Retriever_Movies import get_movie_list
from JSON_format import make_json
from Loader import put, new_index
from datetime import datetime

print datetime.now()

movie_list = get_movie_list()

new_index('test-test-test2')

i = 1
for movie in movie_list:
	movie_data = get_reviewer_list(movie)
	json_data = make_json(movie_data)
	put(json_data, 'test-test-test2', i)
	i += 1