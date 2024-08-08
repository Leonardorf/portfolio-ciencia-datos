# import csv
# import requests

# # Define the URL for the CSV file
# url = "https://datosabiertos.renaper.gob.ar/apellidos_mas_frecuentes_pais.csv"

# # Download the CSV file
# response = requests.get(url)
# response_text = response.text

# # Print all records using the csv library
# csv_reader = csv.reader(response_text.splitlines())
# records = list(csv_reader)

# records

# import csv
# # La r se utiliza cuando queremos definir una cadena de caracteres crudos (raw string) como el caso de abajo que contiene (\)
# #with open(r"C:\Users\Leonardo Villegas\Downloads\apellidos_mas_frecuentes_pais.csv", mode='r', encoding='utf-8') as archivo:
# with open("C:/Users/Leonardo Villegas/Downloads/apellidos_mas_frecuentes_pais.csv", mode='r', encoding='utf-8') as archivo:    
#     csv = csv.reader(archivo)
#     for i in csv:
#         print(i)

# Definir la ruta del archivo

# with open("C:/Users/Leonardo Villegas/Downloads/apellidos_mas_frecuentes_pais.csv", mode='r',encoding='utf-8') as archivo:
#     csv = csv.reader(archivo)
#     next(csv)
#     filas_csv = list(csv)  # almaceno los datos del CSV en una lista ya que necesito recorrer 2 veces a CSV (iterador) si lo hiciera
#     # me daría error el segundo for de apellidos2
#     #apellidos_01 = [fila for fila in filas_csv if float(fila[1]) > 0.1]  #usando lista de comprensión
# for apellido in [fila for fila in filas_csv if float(fila[1]) > 0.1]:
#     print(apellido[0])
# for apellido2 in filas_csv:        
#         if float(apellido2[1]) > 0.1:
#             print(apellido2[0], "sin lista de comprensión")

# import pandas as pd
# df = pd.read_csv("C:/Users/Leonardo Villegas/Downloads/puntos_de_acceso_wifi_Mexico.csv")
# print(df["alcaldia"])

# import json

# with open('C:/Users/Leonardo Villegas/Downloads/Catálogo de información pública.json', 'r', encoding='utf-8') as archivo:
#     data = json.load(archivo)

# print(json.dumps(data, indent=4))

# import urllib.request
# import numpy as np
# import requests
# from io import StringIO
# import urllib
# import ssl
# import io

# import pandas as pd
# import ssl
 
# #ssl._create_default_https_context = ssl._create_unverified_context

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# df = pd.read_csv("https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv", sep=";")
# columnas=["ID_Encuestado", "P1_1", "P2_4"]

# print(df[columnas])
# import pandas as pd
# import ssl
 
# #ssl._create_default_https_context = ssl._create_unverified_context

# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
# url= "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv"
# df = pd.read_csv(url, sep=";")
# valor=df.at[319, "P7_4"]  # at o iloc
# valor=df.iloc[319]["P7_4"]  
# print(valor)

import pandas as pd
import ssl
 
#ssl._create_default_https_context = ssl._create_unverified_context

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
url= "https://www.consejotransparencia.cl/transparencia_activa/datoabierto/archivosFiscalizacion/BBDD_Funcionarios_Publicos_2020.csv"
df = pd.read_csv(url, sep=";")
df.to_csv('C:/Users/Leonardo Villegas/Downloads/Funcionarios_Chile.csv')
print(df.head)
