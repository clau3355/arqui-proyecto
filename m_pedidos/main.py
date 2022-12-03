import os
import json

from flask import Flask, request, render_template
from google.cloud import bigquery
from datetime import date


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'fastappdeliveryproject-4a512d20426a.json'

client = bigquery.Client()

app = Flask(__name__)


def ObtenerPedidos():
    pedidos = []
    query_job = client.query(
        'select * from fastappdeliveryproject.Datos_no_relacionales.tabla_pedido')

    for row in query_job.result():
        pedidos.append({"id_pedido": row["id_pedido"], "id_cliente": row["id_cliente"], "nombre_cliente": row["nombre_cliente"], "monto":row["monto"], "direccion": row["direccion"], "telefono":row["telefono"], "fecha":row["fecha"], "hora":row["hora"]})
    print (pedidos)
    return pedidos

@app.route('/get')
def getpedidos():
    pedidos = ObtenerPedidos()
    json_string = json.dumps(pedidos)
    return json_string

def GetLastId():
    users = ObtenerPedidos()
    resultado = len(users) + 1
    return resultado

@app.route('/crear_pedido')
def crearpedidos():
    bq_client = bigquery.Client()
    table_ref = client.dataset('Datos_no_relacionales').table('tabla_pedido')
    table = client.get_table(table_ref)
    id = GetLastId()
    bq_client.insert_rows(table,[{"id_pedido": id, 
                                                                                     "id_cliente": request.args.get('id_cliente'), 
                                                                                     "nombre_cliente": request.args.get('nombre_cliente'),
                                                                                     "monto":request.args.get('monto'), 
                                                                                     "direccion": request.args.get('direccion'), 
                                                                                     "telefono":request.args.get('telefono'), 
                                                                                     "fecha": request.args.get('fecha'), 
                                                                                     "hora":request.args.get('hora')}])
    return "subido"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('port', 8080)))
