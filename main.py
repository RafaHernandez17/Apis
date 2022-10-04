import requests

if __name__ == '__main__':
    
    url = 'https://httpbin.org/cookies'
    cookies = {'my-cookie': 'Trues'}

    response = requests.get(url, cookies=cookies)

    if response.ok:
        cookies = response.cookies
        print(cookies)

        print("El contenido es:")
        print(response.content)
    