from datetime import datetime

def make_json(data, json = {}):
	print 'title: ' + data[0]
	print 'release date: ' + data[1]
	print 'reviews: ' + str(len(data[2]))

	json = {
		'title' : data[0],
		'release date' : data [1],
		'time stamp' : datetime.now(),
		'critics' : {}
	}

	for i in range(len(data[2])):
		json['critics'][data[2][i]] = data[3][i]

	return json