from flask import render_template, Flask, request, redirect, url_for,session, g
import os
from utils import signup
app = Flask(__name__)


@app.route('/')
def main():
     return render_template('main.html')

@app.before_request
def before_request():
    g.user = None 
    if 'id_user' in session:
        user = "hola"
        g.user = user

@app.route('/index')
def index():
     if not g.user:
        return redirect("login")
        
     var1 = "Lucas"
     var2 = "984999965"
     var3 = "Av. los tulipanes A-18"

     return render_template('index.html', variable1 = var1, variable2 =var2, variable3 = var3 )

@app.route('/login')
def login_post():
    session.pop('id_user',None)
    email = request.form.get('email')
    name = request.form.get('username')
    password = request.form.get('password')

    resultado = True
    #print(resultado)

    if resultado!= False:
        session['id_user'] = resultado
        return redirect("index")
    else:
        return redirect("login")

@app.route('/login', methods=["POST"])
def login():
     return render_template('login.html')

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
     signup(name,email,password,ubicacion)
     return redirect('/login')

@app.route('/mapas')
def mapas():
     if not g.user:
        return redirect("login")
     var1 = "Lima"
     var2 = "Callao"

     return render_template('mapas.html', variable1 = var1, variable2 =var2 )

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))