import requests


def send_chat_bot(texto):
    url_m_bot = "https://mchat-eop4xwh6ma-uc.a.run.app"
    params = {"texto":texto}
    respuesta = requests.get(url=url_m_bot, params=params)
    print(respuesta.text)
    return respuesta.text
    
# def get_map(ubicacion_x, ubicacion_y):
#     url_m_mapa = "https://mapas-modulo-2hgv6awwjq-uc.a.run.app"
#     params = {"origin":ubicacion_x,"destination":ubicacion_y}
#     respuesta = requests.get(url=url_m_mapa, params=params)
#     print(respuesta.text)
#     return respuesta.text

def get_pedidos():
    url_m_mapa = "https://mpedidos-eop4xwh6ma-uc.a.run.app/get"
    params = {}
    respuesta = requests.get(url=url_m_mapa, params=params)
    print(respuesta.text)
    return respuesta.text

def login(mail,psw):
    url_login = "https://m-usuarios-eop4xwh6ma-uc.a.run.app/login"
    params = {"email":mail,"password":psw}
    respuesta = requests.get(url=url_login, params=params)
    print(respuesta.text)
    return respuesta.text

def signup(user,mail,psw,ubi):
    url_signup = "https://m-usuarios-eop4xwh6ma-uc.a.run.app/signup"
    params = {"email":mail,"password":psw, "name": user, "ubi":ubi}
    respuesta = requests.get(url=url_signup, params=params)
    print(respuesta.text)
    return respuesta.text

def locacion(id,ubicacion):
    url_locacion = "https://m-usuarios-eop4xwh6ma-uc.a.run.app/ubicacion"
    params = {"id":id,"ubi":ubicacion}
    respuesta = requests.get(url=url_locacion, params=params)
    print(respuesta.text)
    return respuesta.text


