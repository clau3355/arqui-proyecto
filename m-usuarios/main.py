from flask import Blueprint, render_template, Flask, request
from models import AñadirUser, BuscarUsuarioxCorreo, ValidarUsername, BuscarUsuarioxId, CambiarUbicacion
import os
import json
app = Flask(__name__)

@app.route('/ubicacion')
def cambiar_ubicacion():
    ubicacion = request.args.get('ubi')
    userid = request.args.get('id')
    CambiarUbicacion(userid, ubicacion)
    return "Se cambió la ubicación con éxito"
        
@app.route('/login')
def login_post():
    email = request.args.get('email')
    password = request.args.get('password')
    resultado = ValidarUsername(email,password)
    if resultado!= False:
        json_string = json.dumps(ValidarUsername(email,password))
        return json_string
    else:
        return 'No se encontró el usuario'

@app.route('/signup')
def signup_post():
    email = request.args.get('email')
    name = request.args.get('name')
    password = request.args.get('password')
    ubicacion = request.args.get('ubi')

    resultado = BuscarUsuarioxCorreo(email)
    
    if resultado!=True:
        AñadirUser(name,password,email,ubicacion)
        return "usuario añadido"
    else:
        return 'el registro no fue posible'

@app.route('/id_search')
def id_search():
    id = request.args.get('id')
    resultado = BuscarUsuarioxId(id)
    
    if resultado!=True:
        json_string = json.dumps(BuscarUsuarioxId(id))
        return json_string 
    else:
        return 'False'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))


