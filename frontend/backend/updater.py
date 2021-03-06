
import requests
import time



def update_current_weight(value = 0, id_ = None):
	data = {
	'value' : str(value),
	'id' : str(id_)
	}
	url = 'http://reuniversity.org/backend/php/update.php'
	return requests.post(url=url,data=data)


def start_new_collection(value = 0, id_ = None):
	data = {
	'value' : str(value),
	'id' : str(id_)
	}
	url = 'http://reuniversity.org/backend/php/newcollection.php'
	return requests.post(url=url,data=data)



def clear_all_stats(id_ = None):	# DEBUG ONLYs
	data = {
	'id' : str(id_)
	}
	url = 'http://reuniversity.org/backend/php/clear.php'
	return requests.post(url=url,data=data)

def init_bin(location, nickname):

	if not location:
		location = str(time.time())
	if not nickname:
		nickname = str(time.time())
	data = {
	'location' : location,
	'nickname' : nickname
	}
	

	initurl = 'http://reuniversity.org/backend/php/initbin.php'
	initreq = requests.post(url=initurl,data=data)
	print(initreq.text)
	if initreq.text !='valid':
		return False

	idurl = 'http://reuniversity.org/backend/php/idbynickname.php'
	idreq = requests.post(url=idurl,data=data)
	#print(idreq.text)
	if idreq.text == 'Id not found':
		raise ValueError
	
	id_ = idreq.text
	with open('id.txt','w+') as f:
		f.write(id_)

	return initreq

def addone(id_ = None):
	if not id_:
		raise ValueError

	data = {
	'id': str(id_)
	}

	url = 'http://reuniversity.org/backend/php/addone.php'
	req = requests.post(url=url,data=data)
	#print(req.text)
	return req
	
