from elasticsearch import Elasticsearch, RequestsHttpConnection
from datetime import datetime

es = Elasticsearch(connection_class=RequestsHttpConnection)

def new_index(name):
	es.indices.create(index=name, ignore=400)
	if es.indices.exists(index=name):
		return True
	else:
		return False

def put(doc, index_name, number):
	es.index(index=index_name, doc_type='movie', id = number, body = doc)

def alias(index_name, alias_name):
	if es.indices.exists_alias(name=alias_name) == True:
		al_cur = es.indices.get_alias(name=alias_name)
		es.indices.delete_alias(index='_all', name=alias_name)
		es.indices.put_alias(index=index_name, name=alias_name)
	else:
		es.indices.put_alias(index=index_name, name=alias_name)