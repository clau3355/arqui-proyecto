from flask import render_template, Flask, request, redirect, url_for,session, g, flash
import os
import time
from utils import signup, login
import json
from types import SimpleNamespace

app = Flask(__name__)


@app.route('/')
def main():
     return render_template('main.html')

@app.before_request
def before_request():
    g.user = None 
    if 'id_user' in session:
        g.user = session['id_user']

@app.route('/index')
def index():
     if not g.user:
        return redirect("login")
        
     var1 = g.user['username']
     var3 = g.user['ubicacion']

     return render_template('index.html', variable1 = var1, variable3 = var3 )

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_post():
     session.pop('id_user',None)
     email = request.form.get('correo')
     password = request.form.get('password')
     respuesta = login(email,password)
     tipo = type(respuesta) 
     try:
          x = json.loads(respuesta)
          if(x!=None):
               session['id_user'] = x
               return redirect(url_for('index'))
     except:
          flash('Error en inicio de sesión')
          return redirect(url_for('login_page'))

@app.route('/logout')
def logout():
     session.pop('id_user', None)
     g.user = None
     return redirect('/')

@app.route('/tiendas')
def tiendas():
     if not g.user:
        return redirect("login")

     return render_template('tiendas.html')

@app.route('/pedido')
def pedido():
     if not g.user:
        return redirect("login")

     return render_template('pedido.html')

@app.route('/registro')
def registro():
     return render_template('registro.html')

@app.route('/registro', methods=["POST"])
def registro_post():
     email = request.form.get('email')
     name = request.form.get('name')
     password = request.form.get('password')
     ubicacion = request.form.get('ubicacion')
     respuesta = signup(name,email,password,ubicacion)
     flash(respuesta)
     return render_template('registro.html')

#cambios

@app.route('/mapas')
def mapas():
     if not g.user:
        return redirect("login")
     var1 = "Callao"
     var2 = g.user['ubicacion']

     return render_template('mapas.html', variable1 = var1, variable2 =var2 )

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))