
import requests




def update_current_weight(value = 0, id_ = None):
	data = {
	'value' : str(value),
	'id' : str(id_)
	}
	url = 'http://10.205.255.121/frontend/backend/php/update.php'
	return requests.post(url=url,data=data)


def start_new_collection(value = 0, id_ = None):
	data = {
	'value' : str(value),
	'id' : str(id_)
	}
	url = 'http://10.205.255.121/frontend/backend/php/newcollection.php'
	return requests.post(url=url,data=data)
	


def clear_all_stats(id_ = None):	# DEBUG ONLYs
	data = {
	'id' : str(id_)
	}
	url = 'http://10.205.255.121/frontend/backend/php/clear.php'
	return requests.post(url=url,data=data)
	
def init_bin(id_):
	if not id_:
		raise ValueError
	data = {
	'id' : str(id_)
	}
	url = 'http://10.205.255.121/frontend/backend/php/initbin.php'
	return requests.post(url=url,data=data)
