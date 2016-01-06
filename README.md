Loads metacritic reviewer data into ElasticSearch

#Usage

- Install Python 2.7
	- Requests
		- `pip install requests`
	- Elasticsearch
		- `pip install elasticsearch`

- Install ElasticSearch

- Run `python index.py`

#CLI Options

This is a command line program run by invoking `python index.py`

- **-p, --port** *Default: 9200* The elasticsearch port.

- **-a, --alias** *Default: "Banana"* The name of the elasticsearch alias for the latest movie index.

- **-i, --index** *Default: `datetime.now()`* The name of the elasticsearch index used to load movie data.