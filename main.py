import requests

client_id = 'b3e6970bf3b7909fed65'
client_secret = '535666638ddfa1ca915d82ba8d03dc2f1128ef48'
code='31cc211460269892a4f6'

if __name__ == '__main__':
    
    url = 'https://github.com/login/oauth/access_token'
    payload = {'client_id': client_id, 'client_secret': client_secret, 'code': code}
    headers = {'Accept' : 'application/json'}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        response_json =  response.json()

        access_token = response_json["access_token"]
        print(access_token)
#https://github.com/login/oauth/authorize?client_id=b3e6970bf3b7909fed65&scope=repo    

  