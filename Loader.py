from elasticsearch import Elasticsearch, RequestsHttpConnection
from datetime import datetime

es = Elasticsearch(connection_class=RequestsHttpConnection)

def new_index(name):
	es.indices.create(index = name, ignore=400)

def put(doc, index_name, number):
	es.index(index=index_name, doc_type='movie', id = number, body = doc)