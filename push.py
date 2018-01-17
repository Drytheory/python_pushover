import requests

user_token = 'USER_KEY'

def send_push_message(app_key, title, message):
	push_data = {'token': app_key, 'user': user_token, 'title': title, 'message': message}
	post_request = requests.post('https://api.pushover.net/1/messages.json', data=push_data)