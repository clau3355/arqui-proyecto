import os
import json

from flask import Flask, request, render_template
from google.cloud import bigquery

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fastdeliveryproject-e62677747c15.json"

client = bigquery.Client()

app = Flask(__name__)


def ObtenerPedidos():
    pedidos = []
    query_job = client.query(
        'select * from fastdeliveryproject.Datos_no_relacionales.tabla_pedido')

    for row in query_job.result():
        pedidos.append({"id_pedido": row["id_pedido"], "id_cliente": row["id_cliente"], "nombre_cliente": row["nombre_cliente"], "monto":row["monto"], "direccion": row["direccion"], "telefono":row["telefono"], "fecha":row["fecha"], "hora":row["hora"]})
    print (pedidos)
    return pedidos

@app.route('/get')
def my_map():
    pedidos = ObtenerPedidos()
    json_string = json.dumps(pedidos)
    return json_string

@app.route('/crear_pedido')
def my_map():
    bq_client = bigquery.Client()
    bq_client.insert_rows("fastdeliveryproject.Datos_no_relacionales.tabla_pedido",[{"id_pedido": request.args.get('id_pedido'), 
                                                                                     "id_cliente": request.args.get('id_cliente'), 
                                                                                     "nombre_cliente": request.args.get('nombre_cliente'),
                                                                                     "monto":request.args.get('monto'), 
                                                                                     "direccion": request.args.get('direccion'), 
                                                                                     "telefono":request.args.get('telefono'), 
                                                                                     "fecha":request.args.get('fecha'), 
                                                                                     "hora":request.args.get('hora')}])
    return "subido"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))
