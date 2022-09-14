import requests
import json

if __name__ == '__main__':
    url = 'http://httpbin.org/post'
    payload = {'nombre': 'Rafael', 'curso': 'python'}

    #response = requests.post(url, json=payload)
    response = requests.post(url, data=json.dumps(payload))

    #json post se encarga de serializarlos
    #data entonces nosotros de serializarlos
    print(response.url)

    if response.status_code == 200:
        print(response.content)