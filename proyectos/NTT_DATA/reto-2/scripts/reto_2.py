import json
from pymongo import MongoClient
import mysql.connector


conexion=mysql.connector.connect(user='root',
# password='',host='localhost',database='personas',port='3306',database='Cine')
password='',host='localhost',port='3306', database='estadosu')
cursor_mysql = conexion.cursor()


cursor_mysql.execute("SELECT * FROM estados")
datos_mysql = cursor_mysql.fetchall()
datos_json = []
for estado in datos_mysql:
    estado_json = {
        "estado": estado[0],
        "poblacion": {
          "poblacion_2000": estado[1],
          "poblacion_2001": estado[2]},
        "residentes_menores_65": {
            "residentes_menores_65_2000": estado[3],
            "residentes_menores_65_2001": estado[4]},
        "muertes": {
            "muertes_2000": estado[5],
            "muertes_2001": estado[6]},
        "latitud": float(estado[7]),
        "longitud": float(estado[8]),
        "fecha_fundacion": estado[9].strftime("%Y-%m-%d")
    }
    # estado_json = {
    #     "estado": estado[0],
    #     "poblacion_2000": estado[1],
    #     "poblacion_2001": estado[2],
    #     "residentes_menores_65_2000": estado[3],
    #     "residentes_menores_65_2001": estado[4],
    #     "muertes_2000": estado[5],
    #     "muertes_2001": estado[6],
    #     "latitud": float(estado[7]),
    #     "longitud": float(estado[8]),
    #     "fecha_fundacion": estado[9].strftime("%Y-%m-%d")
    # }
    datos_json.append(estado_json)


cliente = MongoClient("mongodb+srv://leonfevi:vhC47YL32KUYHOpJ@cluster1.qn8swog.mongodb.net/")
base_datos_mongodb = cliente.estados
coleccion_mongodb = base_datos_mongodb.estados

coleccion_mongodb.insert_many(datos_json)
datos_recuperados = coleccion_mongodb.find()


for estado in datos_recuperados:
     print(json.dumps(estado, indent=4,default=str))


conexion.close()
cliente.close()