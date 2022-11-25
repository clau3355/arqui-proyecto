import socket
import threading
import json
from queue import Queue
from google.cloud import storage
from google.cloud import bigquery
import os
from datetime import datetime

serviceAccount = r'fastdeliveryproject-0ff8eca1ffb4.json'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = serviceAccount
TZ_05 = datetime.strptime('-0500','%z')
q_messages = Queue()

table_id = 'fastdeliveryproject.monitoreo_chat.chat-enters'

class hilo(threading.Thread):
    def __init__(self, conexion, direccion, sockets, user, room):
        threading.Thread.__init__(self)
        self.conexion = conexion
        self.direccion = direccion
        self.sockets = sockets
        self.user = user
        self.room = room

    def run(self):
        print("Nueva conexción: ", self.direccion[0])
        
        bq_client = bigquery.Client()
        row = [
            {
                "ip": str(self.direccion),
                "user": str(self.user),
                "datetime": datetime.strftime(datetime.now(TZ_05.tzinfo),'%Y-%m-%d %H:%M:%S'),
                "room": str(self.room),
            },
        ]
        errors = bq_client.insert_rows_json(table_id, row)
        if errors == []:
            print("New rows have been added.")
        else:
            print("Encountered errors while inserting rows: {}".format(errors))
            
        for socket in self.sockets:
            if socket[2] == self.room:
                mensaje = self.direccion[0] + ": conectado"
                socket[0].send(mensaje.encode())
                print("enviado")

        while True:
            try:
                data = json.loads(self.conexion.recv(
                    2048).decode().replace("\'", "\""))
                mensaje = str(self.direccion[0]) + ">" + str(data)
                print(mensaje)
                q_messages.put((self.room,self.user,data))

                for socket in self.sockets:
                    if socket[2] == self.room:
                        socket[0].send(mensaje.encode())
                        print("enviado")
            except Exception as E:
                print(E)
                pass


class servidor():
    def iniciar():
        clientes_sockets = []
        hilos = []
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ('', 3389)
        # host = ('localhost',8080)
        server.bind(host)
        server.listen(3)
        print("Socket creado")
        while True:
            c, addr = server.accept()

            print("Connection from: " + str(addr))
            data = json.loads(c.recv(2048).decode().replace("\'", "\""))
            clientes_sockets.append((c, data["user"], data["room"]))

            hl = hilo(c, addr, clientes_sockets, data["user"], data["room"])
            hl.start()
            hilos.append(hl)

            for i in hilos:
                i.sockets = clientes_sockets


def save_chat():
    print("save_chat activado")
    chats = {}
    while True:
        while not q_messages.empty():
            data = q_messages.get()
            room = data[0]
            chat = []
            
            if room in chats.keys():
                chat = chats[room]
            
            
            chat.append(str(data[1])+ ": "+str(data[2]["mensaje"]))
            chats[room] = chat
            # print(data[2]["mensaje"])
            if data[2]["mensaje"] == "end":
                with open(os.path.join("tmp",room+".txt"), 'w') as fp:
                    for item in chat:
                        # write each item on a new line
                        fp.write("%s\n" % item)
                    fp.close()
                storage_client = storage.Client()
                bucket_name = "ulima_22"
                bucket = storage_client.get_bucket(bucket_name)
                blob = bucket.blob(room+".txt")
                blob.upload_from_filename(os.path.join("tmp",room+".txt"))
                chats.pop(room)
            
            
tchat = threading.Thread(target=save_chat)   
tchat.start()     
servidor.iniciar()
