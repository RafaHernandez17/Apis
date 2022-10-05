from urllib import response
import requests

if __name__ == '__main__':
    
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('al063778@uacam.mx','5289hudson')

    response = session.get(url)
    if response.ok:
        response = session.get('https://github.com/RafaHernandez17')
        if response.ok:
            
