import requests

def send_chat_bot(texto):
    url_m_bot = "https://chat-bot-2hgv6awwjq-uc.a.run.app"
    params = {"texto":texto}
    respuesta = requests.get(url=url_m_bot, params=params)
    print(respuesta.text)
    return respuesta.text
    
def get_map(ubicacion_x, ubicacion_y):
    url_m_mapa = "https://mapas-modulo-2hgv6awwjq-uc.a.run.app"
    params = {"origin":ubicacion_x,"destination":ubicacion_y}
    respuesta = requests.get(url=url_m_mapa, params=params)
    print(respuesta.text)
    return respuesta.text

def get_map(ubicacion_x, ubicacion_y):
    url_m_mapa = "https://mapas-modulo-2hgv6awwjq-uc.a.run.app"
    params = {"origin":ubicacion_x,"destination":ubicacion_y}
    respuesta = requests.get(url=url_m_mapa, params=params)
    print(respuesta.text)
    return respuesta.text