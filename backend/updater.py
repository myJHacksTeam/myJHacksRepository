
import requests




def update_current_weight(value = 0, id_ = None):
	data = {
	'value' : str(value),
	'id' : str(id_)
	}
	url = 'http://10.0.2.255/update.php'
	requests.post(url=url,data=data)


def start_new_collection(value = 0, id_ = None):
	data = {
	'value' : str(value),
	'id' : str(id_)
	}
	url = 'http://10.0.2.255/newcollection.php'
	requests.post(url=url,data=data)
	


def clear_all_stats(id_ = None):	# DEBUG ONLYs
	data = {
	'id' : str(id_)
	}
	url = 'http://10.0.2.255/clear.php'
	requests.post(url=url,data=data)
	
def init_bin(id_):
	if not id_:
		raise ValueError
	data = {
	'id' : str(id_)
	}
	url = 'http://10.0.2.255/initbin.php'
	requests.post(url=url,data=data)
