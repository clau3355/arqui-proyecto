import os
import json

from flask import Flask, request, render_template
from google.cloud import bigquery

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fastdeliveryproject-e62677747c15.json"

client = bigquery.Client()

app = Flask(__name__)

# class Pedido:
#     def __init__(self,id_pedido,id_cliente,nombre_cliente,monto,direccion,telefono,fecha,hora):
#         self.id_pedido = id_pedido
#         self.id_cliente = id_cliente
#         self.nombre_cliente = nombre_cliente
#         self.monto = monto
#         self.direccion = direccion
#         self.telefono = telefono
#         self.fecha = fecha
#         self.hora = hora

#     def __repr__(self):
#         return f'<Pedido: {self.id_pedido}>'


def ObtenerPedidos():
    pedidos = []
    query_job = client.query(
        'select * from fastdeliveryproject.Datos_no_relacionales.tabla_pedido')

    for row in query_job.result():
        pedidos.append({"id_pedido": row["id_pedido"], "id_cliente": row["id_cliente"], "nombre_cliente": row["nombre_cliente"], "monto":row["monto"], "direccion": row["direccion"], "telefono":row["telefono"], "fecha":row["fecha"], "hora":row["hora"]})
    print (pedidos)
    return pedidos

@app.route('/')
def my_map():
    pedidos = ObtenerPedidos()
    json_string = json.dumps(pedidos)
    return json_string


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

ObtenerPedidos()
