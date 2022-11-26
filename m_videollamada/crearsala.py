from flask import render_template, Flask, request
import os
from twilio.rest import Client
from google.cloud import bigquery
client = bigquery.Client()


app = Flask(__name__, static_url_path='')

def Obteneridsala(idusuario):

    query_job = client.query('')

    print ('sala es' + query_job)

    return query_job


@app.route('/videollamada')
def map():
     
     
     idsala = Obteneridsala()

     account_sid = 'AC62cce6a78007cf37f842cbff6562cff1'
     auth_token = 'f36874c09ab96c9be06b5fa87d87d01f'
     client = Client(account_sid, auth_token)

     room = client.video.v1.rooms.create(unique_name='Daily')

     print(room.sid)

     return render_template('prueba.html' )



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8085)))
