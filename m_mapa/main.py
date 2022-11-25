from flask import Blueprint, render_template, Flask, request, redirect, url_for,session, g, abort
from models import AñadirUser, BuscarUsuarioxCorreo, ValidarUsername, BuscarUsuarioxId, CambiarUbicacion
import os
app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    print(g.user)
    if not g.user:
        return redirect("login")
    return render_template('profile.html')

@app.route('/profile', methods=["POST"])
def profile_post():
    ubicacion = request.form.get("ubicacion")
    g.user.ubicacion = ubicacion
    CambiarUbicacion(g.user.id_user, ubicacion)
    #return redirect(url_for('profile'))
    return redirect("/")

@app.route('/mapa')
def map():
    if not g.user:
        return redirect("login")
    return render_template('mapa.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.before_request
def before_request():
    g.user = None 
    if 'id_user' in session:
        user = BuscarUsuarioxId(session['id_user'])
        g.user = user
        
@app.route('/login', methods=["POST"])
def login_post():
    session.pop('id_user',None)
    email = request.form.get('email')
    name = request.form.get('username')
    password = request.form.get('password')

    resultado = ValidarUsername(name,password)
    #print(resultado)

    if resultado!= False:
        session['id_user'] = resultado
        return redirect("profile")
    else:
        return redirect("login")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=["POST"])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    resultado = BuscarUsuarioxCorreo(email)
    #print(resultado)
    if resultado!=True:
        AñadirUser(name,email,password)
    else:
        return redirect('signup')
    return redirect('login')

@app.route('/logout')
def logout():
    session.pop('id_user', None)
    g.user = None
    return redirect('/')

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SESSION_TYPE'] = 'filesystem'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
