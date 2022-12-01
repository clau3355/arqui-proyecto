from flask import render_template, Flask, request
import os
app = Flask(__name__)


@app.route('/')
def main():
     return render_template('main.html')

@app.route('/index')
def map():
     var1 = "Lucas"
     var2 = "984999965"
     var3 = "Av. los tulipanes A-18"

     return render_template('index.html', variable1 = var1, variable2 =var2, variable3 = var3 )

@app.route('/login')
def login():
     return render_template('login.html')

@app.route('/logout')
def logout():
     return "logout"

@app.route('/tiendas')
def tiendas():
     return render_template('tiendas.html')

@app.route('/pedido')
def pedido():
     return render_template('pedido.html')

@app.route('/registro')
def registro():
     return render_template('registro.html')

@app.route('/mapas')
def mapas():
     var1 = "Lima"
     var2 = "Callao"

     return render_template('mapas.html', variable1 = var1, variable2 =var2 )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))