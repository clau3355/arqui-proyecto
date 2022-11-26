from flask import Blueprint, render_template, Flask, request, redirect, url_for,session, g, abort
from models import AñadirUser, BuscarUsuarioxCorreo, ValidarUsername, BuscarUsuarioxId, CambiarUbicacion
import os
app = Flask(__name__, static_url_path='')


@app.before_request
def before_request():
    g.user = None 
    if 'id_user' in session:
        user = BuscarUsuarioxId(session['id_user'])
        g.user = user
        
@app.route('/login')
def login_post():
    session.pop('id_user',None)
    print("ingresa tu correo")
    email = input()
    print("ingresa tu nombre")
    name = input()
    print("ingresa tu contraseña")
    password = input()

    resultado = ValidarUsername(name,password)
    #print(resultado)

    if resultado!= False:
        session['id_user'] = resultado
        return 'conectado'
    else:
        return 'no se pudo iniciar sesión'

@app.route('/signup')
def signup_post():
    print("ingresa tu correo")
    email = input()
    print("ingresa tu nombre")
    name = input()
    print("ingresa tu contraseña")
    password = input()
    resultado = BuscarUsuarioxCorreo(email)
    
    if resultado!=True:
        AñadirUser(name,password,email)
        return ("Usuario " + name + " registrado")
    else:
        return ("no se pudo registrar")
    

@app.route('/logout')
def logout():
    session.pop('id_user', None)
    g.user = None
    return "se ha cerrado la sesion"

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SESSION_TYPE'] = 'filesystem'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


