from http import server
import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Rafael', 'curso': 'python'}
    #enviando datos en formato json
    headers = {'Conten-Type': 'application/json', 'access-token': '12345'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.url)

    if response.status_code == 200:
        #print(response.content)
        headers_response = response.headers #Dic
        #print(headers_response)
        server = headers_response['Server']
        print(server)