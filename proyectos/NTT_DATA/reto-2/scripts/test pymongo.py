import pymongo
MONGO_URL="mongodb+srv://leonfevi:mongo@cluster0.u9xnnrf.mongodb.net/" #Recuerda que aquí tendrás que sustituir <username> por tu nombre

MONGO_BASEDATOS="test"
MONGO_COLECCION="coleccion1"
try:
 cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=1000)
#Si no declaramos un time out nos dará un error
#Vamos a conectarnos a la BBDD pasándole el nombre de la BBDD y obtenemos ese objeto dentro de una variable
 baseDatos=cliente[MONGO_BASEDATOS]
 coleccion=baseDatos[MONGO_COLECCION]
 #Recorremos los objetos que están dentro de la colección
 for documento in coleccion.find():
 #Imprimimos por pantalla el nombre de la película y el año de cada registro de la colección y convertimos la calificación a STRING para concatenarlo ya que es un entero.
  print(documento["nombre"]+" "+str(documento["año"]))
 cliente.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
 print("Tiempo excedido de carga")
except pymongo.errors.ConnectionFailure as errorConexion:
 print("Fallo al conectarse a mongodb"+errorConexion)
