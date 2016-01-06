from elasticsearch import Elasticsearch, RequestsHttpConnection
from datetime import datetime


def new_index(name, es):
	es.indices.create(index=name, ignore=400)
	if es.indices.exists(index=name):
		return True
	else:
		return False

def put(doc, index_name, number, es):
	es.index(index=index_name, doc_type='movie', id = number, body = doc)

def alias(index_name, alias_name, es):
	if es.indices.exists_alias(name=alias_name) == True:
		al_cur = es.indices.get_alias(name=alias_name)
		body = atomic_alias(alias_name, al_cur, index_name)
		es.indices.update_aliases(body=body)
	else:
		es.indices.put_alias(index=index_name, name=alias_name)

def atomic_alias(alias_name, al_cur, index_name):
	body = '''{
		"actions" : [
			{"remove" : { "index" : "%s", "alias": "%s"}},
			{"add" : { "index" : "%s", "alias": "%s"}}
		]
	}''' % (al_cur.keys()[0], alias_name, index_name, alias_name)
	return body