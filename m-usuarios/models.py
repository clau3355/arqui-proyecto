import os
from google.cloud import bigquery
from datetime import date
from kms import encriptar, desencriptar


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'fastdeliveryproject-e62677747c15.json'

client = bigquery.Client()

class User:
    def __init__(self,username,password,mail,id_user,ubicacion,money, id_sala):
        self.id_user = id_user
        self.mail = mail
        self.username = username
        self.password = password
        self.ubicacion = ubicacion
        self.money = money
        self.id_sala = id_sala

    def __repr__(self):
        return f'<User: {self.username}>'

def ObtenerUsuarios():
    users = []
    query_job = client.query('select * from fastdeliveryproject.Datos_no_relacionales.tabla_test')

    for row in query_job.result():
        users.append(User(username=row["username"], ubicacion=row["ubicacion"], money=row["money"], password=row["pass"],id_user=row["id_user"], mail=row["correo"], id_sala=row["id_sala"]))
    return users

def CambiarUbicacion(a,b):
    user = BuscarUsuarioxId(a)
    user.ubicacion = b
    query_job = client.query('UPDATE fastdeliveryproject.Datos_no_relacionales.tabla_test SET ubicacion="{}" WHERE id_user ="{}"'.format(b,a))

def BuscarUsuarioxCorreo(a):
    users = ObtenerUsuarios()
    resultado = False
    for i in users:
        print(i.mail)
        print (a)
        if i.mail == a:      
            resultado = True
    return resultado
        
def BuscarUsuarioxId(a):
    users = ObtenerUsuarios()
    for i in users:
        if i.id_user == a:
            return i

def GetLastId():
    users = ObtenerUsuarios()
    resultado = len(users) + 1
    return resultado

def AñadirUser(a,b,c):
   # For this sample, the table must already exist and have a defined 
    schematable_id = 'test_table_creation'
    fecha = date.today()
    table_ref = client.dataset('Datos_no_relacionales').table('tabla_test')
    table = client.get_table(table_ref)
    # Creating a list of tuples with the values that shall be inserted into the table
    id = GetLastId()
    contra = encriptar(b)
    rows_to_insert = [(id,contra,"100",None,fecha,a,c,None)]
    errors = client.insert_rows(table, rows_to_insert) 
    print(errors)

def ValidarUsername(a,b):
    users = ObtenerUsuarios()
    for i in users:
        contra = desencriptar(i.password)
        if i.username == a:
            print("se encontró el usuario")
            if contra == b:
                print("la contraseña es correcta")
                return i.id_user

