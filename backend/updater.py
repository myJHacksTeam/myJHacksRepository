
import requests




def update_current_weight(value = 0, id = None):
	data = {
	'value' : str(value),
	'id' : str(id)
	}
	url = '10.0.2.255/update.php'
	requests.post(url=url,data=data)


def start_new_collection(value = 0, id = None):
	data = {
	'value' : str(value),
	'id' : str(id)
	}
	url = '10.0.2.255/newcollection.php'
	requests.post(url=url,data=data)
	


def clear_all_stats(id = None):	# DEBUG ONLYs
	data = {
	'id' : str(id)
	}
	url = '10.0.2.255/clear.php'
	requests.post(url=url,data=data)
	
