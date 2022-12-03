import os
import json

from flask import Flask, request, render_template
from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fastappdeliveryproject-4a512d20426a.json'

client = bigquery.Client()

app = Flask(__name__)


def ObtenerTiendas():
    tiendas = []
    query_job = client.query(
        'select * from fastappdeliveryproject.Datos_no_relacionales.tabla_tienda')

    for row in query_job.result():
        tiendas.append({"id_tienda": row["id_tienda"], "nombre": row["nombre"], "direccion": row["direccion"],"productos": row["productos"]})
    print (tiendas)
    return tiendas

@app.route('/get')
def my_map():
    tiendas = ObtenerTiendas()
    json_string = json.dumps(tiendas)
    return json_string

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))
