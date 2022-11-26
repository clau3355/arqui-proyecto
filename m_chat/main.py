from flask import Flask, request
import os
import re
import random
import requests
import json

app = Flask(__name__)


def get_pedido_user(usuario_id):
    pedidos = requests.get('https://lista-pedidos-2hgv6awwjq-uc.a.run.app/')
    pedidos = json.loads(pedidos.text)
    for row in pedidos:
        print(row)
        print(f'_{row["id_cliente"]}_')
        print(f'_{usuario_id}_')
        if str(row["id_cliente"]) == usuario_id:
            return f'Su pedido es el número {row["id_pedido"]} realizado a las {row["hora"]}, a la dirección {row["direccion"]} por un costo de S/.{row["monto"]}'
        else:
            return "Usuario no cuenta con pedido"


def get_respuesta(mensaje):
    print(mensaje)
    ls_mensaje = re.split(r'\s|[,:;.?!-_ ]\s*', mensaje.lower())
    print(ls_mensaje)
    respuesta = seleccionar_respuesta(mensaje, ls_mensaje)
    return respuesta


def probabilidad(ls_mensaje, palabras_reconocida, respuesta_sencilla=False, palabras_requerida=[]):
    certeza = 0
    tiene_palabras_requeridas = True

    for word in ls_mensaje:
        if word in palabras_reconocida:
            certeza += 1
    porcentaje = float(certeza) / float(len(palabras_reconocida))

    for word in palabras_requerida:
        if word not in ls_mensaje:
            tiene_palabras_requeridas = False
            break
    if tiene_palabras_requeridas or respuesta_sencilla:
        return int(porcentaje * 100)
    else:
        return 0


def seleccionar_respuesta(mensaje, ls_mensajes):
    probabilidad_max = {}

    def response(respuesta, list_of_words, single_response=False, required_words=[]):
        nonlocal probabilidad_max
        probabilidad_max[respuesta] = probabilidad(
            ls_mensajes, list_of_words, single_response, required_words)

    response('Hola, soy Alexa, su asistente virtual de soporte, en que puedo ayudarlo?', [
             'hola', 'saludos', 'buenas'], single_response=True)
    response('Conqué necesita ayuda?', [
             'soporte', 'necesito', 'ayuda', 'sientes'], single_response=True)
    response('Estamos ubicados en la Javier Prado numero 321', [
             'ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
    response('Envie usuario', ['pedido', 'estado',
             'envio'], single_response=True)
    response("get_pedido_user", ['usercode'],
             single_response=True, required_words="usercode")
    response('Esperemos haberlo ayudado', [
             'gracias', 'te lo agradezco', 'thanks'], single_response=True)

    best_match = max(probabilidad_max, key=probabilidad_max.get)
    respuesta = unknown() if probabilidad_max[best_match] < 1 else best_match
    if respuesta == "get_pedido_user":
        print(ls_mensajes)
        respuesta = get_pedido_user(mensaje.split(" ")[-1])
    return respuesta


def unknown():
    response = ['puedes decirlo de nuevo?',
                'No estoy seguro de lo quieres'][random.randrange(2)]
    return response


@app.route("/")
def home():
    mensaje = request.args.get('texto')
    print(str(mensaje))
    respuesta = get_respuesta(str(mensaje))
    print("Soporte: " + str(respuesta))
    return ("Soporte: " + str(respuesta))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))
