from flask import render_template, Flask
import os
app = Flask(__name__, static_url_path='')



@app.route('/')
def map():
     print('Ubicacion1:')
     var1 = input()


     print('Ubicacion2:')
     var2 = input()

     return render_template('mapa.html', variable1 = var1, variable2 =var2 )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
