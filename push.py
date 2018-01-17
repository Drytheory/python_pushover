import requests


#Hier den User Key eintragen
user_token = 'unej1vrdhj91xvz6o4q88i3aair6bq'



def send_push_message(app_key, title, message):
	push_data = {
		'token': app_key, 
		'user': user_token, 
		'title': title, 
		'message': message
	}

	post_request = requests.post('https://api.pushover.net/1/messages.json', data=push_data)