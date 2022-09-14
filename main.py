import requests

if __name__ == '__main__':
    url = 'https://www.google.com.mx/'
    response = requests.get(url)

    #Muestra la estructura html del url
    #if response.status_code == 200:
        #print(response.content)
    
    #Guardar el contenido de la pag web

    if response.status_code == 200:
        content = response.content
        file = open('google.html', 'wb')
        file.write(content)
        file.close()