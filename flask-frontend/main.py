from flask import render_template, Flask, request
import os
app = Flask(__name__)

@app.route('/')
def map():
     return render_template('index.html')
     
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))