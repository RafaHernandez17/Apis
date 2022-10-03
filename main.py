from asyncio import streams
import requests
import json

if __name__ == '__main__':
    url = 'https://dwgyu36up6iuz.cloudfront.net/heru80fdn/image/upload/c_fill,d_placeholder_voguemexico.png,fl_progressive,g_face,h_1080,q_80,w_1920/v1661803282/voguemexico_twice.jpg'

    response = requests.get(url, stream=True) # Realiza una peticion sin cerrar el contenido
    with open('image.jpg', 'wb') as file:
        for chunk in response.iter_content(): # Descarga el contenido poco a poco
            file.write(chunk)

    response.close()