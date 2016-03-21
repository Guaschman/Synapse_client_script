import requests
import random
import json

#TODO: Refactor the copy pasta

class Client:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register_with_password(self):
        self.user_grade = 'normal'
        print("----------------------------REGISTERING---------------------------------------")
        payload = {
            'username': self.username,
            'password': self.password
        }

        request = requests.post('http://172.17.0.2:8008/_matrix/client/r0/register', json=payload)
        text = json.loads(request.text)

        #print("Everything: ", text)
        print("Flow: ", text['flows'])
        print("Stages:", text['flows'][0]["stages"][0])
        print("Stages: ", text['flows'][1]["stages"][0])
        payload = {
            'auth': {
                'type': text['flows'][0]["stages"][0],
                'session': text['session'],
            }
        }
        request = requests.post('http://172.17.0.2:8008/_matrix/client/r0/register', json=payload)
        text = json.loads(request.text)
        #print("Everything: ", text)
        print("Access Token: ", text['access_token'])
        print("User ID: ", text['user_id'])
        print("Home server: ", text['home_server'])

    def register_guest(self):
        self.user_grade = 'guest'
        print("----------------------------REGISTERING AS GUEST---------------------------------------")
        payload = {
            'username': self.username,
            'password': self.password
        }

        request = requests.post('http://172.17.0.2:8008/_matrix/client/r0/register?kind=guest', json=payload)
        text = json.loads(request.text)

        #print("Everything: ", text)
        print("Access Token: ", text['access_token'])
        print("User ID: ", text['user_id'])
        print("Home server: ", text['home_server'])

    def login_with_password(self):
        print("----------------------------LOGGING IN---------------------------------------")
        payload = {
            'password': self.password,
            'type': 'm.login.password',
            'user': self.username
        }

        request = requests.post('http://172.17.0.2:8008/_matrix/client/r0/login', json=payload)
        text = json.loads(request.text)
        #print("Everything: ", text)
        print("Access Token: ", text['access_token'])
        print("User ID: ", text['user_id'])
        print("Home server: ", text['home_server'])
        print("Refresh Token: ", text['refresh_token'])

def main ():
    username = 'a' + repr(random.random())[2:]
    client = Client(username, 'password')
    client.register_guest()

if __name__ == '__main__':
    main()
