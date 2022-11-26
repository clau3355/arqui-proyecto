from flask import render_template, Flask, request
import os
app = Flask(__name__)

@app.route('/map')
def map():
     var1 = request.args.get('origin')
     var2 = request.args.get('destination')

     return render_template('mapa.html', variable1 = var1, variable2 =var2 )
     
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))
