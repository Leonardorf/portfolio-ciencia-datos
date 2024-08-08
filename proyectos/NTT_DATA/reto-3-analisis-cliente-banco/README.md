
# Proyecto NTT DATA - RETO 3: Análisis Clientes Banco -  Objetivo anticipar el cierre de cuenta y abandono de la entidad
Una entidad bancaria americana que opera en California, Texas y Alabama pretende implementar un modelo de abandono de clientes (modelo Churn) con el objetivo de poder anticiparse a la marcha de estos y poder realizar acciones comerciales para, precisamente, evitar la pérdida implícita en el abandono de los clientes. 

La entidad bancaria, nos facilita una base de datos con 10.000 registros de información que contienen las siguientes variables contenidas en el df estados bank (csv): 


 • RowNumber: número de registro.
 
 • CustomerId: identificador único de cliente.

 • Surname: apellido del cliente.

 • CreditScore: puntuación de crédito del cliente.

 • Geography: estado del cliente.

 • Gender: género del cliente.

 • Age: edad del cliente.

 • Tenure: número de años que el cliente lleva en el banco.

 • Balance: balance del cliente.

 • NumOfProducts: número de productos que el cliente tiene en el banco.

 • HasCrCard: si el cliente tiene o no tarjeta de crédito.

 • IsActiveMember: es cliente activo o no de la entidad.

 • EstimatedSalary: salario que la entidad estima que ingresa mensualmente el cliente.

 • Exited: es la variable objetivo: o 1: el cliente abandonó la entidad o 0: el cliente no abandonó la entidad


 2. ESTADOS DE ESTADOS UNIDOS
 En este reto, vamos a profundizar un pocovbmás en cómo se podrían comportar las personas de tres de estos estados, en relación con su banco.
En concreto, una entidad bancaria americana que opera en California, Texas y Alabama
pretende implementar un modelo de abandono de clientes (modelo Churn) con el objetivo
de poder anticiparse a la marcha de estos y poder realizar acciones comerciales para,
precisamente, evitar la pérdida implícita en el abandono de los clientes.

Leed el fichero de texto df_estados_bank.csv que se corresponde con el conjunto de datos
a trabajar en este reto.

Realizad una correcta limpieza de datos inicial con el objetivo de preparar la base de
datos previa a entrenar el modelo. Sin haber entrenado el modelo, dad respuesta a las
siguientes preguntas:

• ¿Consideráis que todas las variables del conjunto de datos son útiles de cara a la
predicción? ¿Cuáles sí y cuáles no? Justificad vuestra respuesta.
• ¿A qué tipo de modelo os enfrentáis? Justificad vuestra respuesta.

2.2. Ejercicio 2
Atendiendo a la segunda respuesta del ejercicio anterior, plantead, al menos, 2 algoritmos
diferentes que predigan el abandono (o no) del cliente. Realizad todos los pasos
necesarios antes de la aplicación del modelo predictivo.
• ¿Qué algoritmo es el que os ha arrojado mejores resultados?
• ¿Cómo habéis evaluado la bondad del ajuste? Justificad vuestra
respuesta.
• ¿Podéis explicar qué características son las que más inciden en la
decisión de un cliente para abandonar definitivamente la entidad?

2.3. Ejercicio 3
Escogiendo el mejor algoritmo del ejercicio anterior, planteaos la posibilidad de que los
resultados puedan ser más ajustados si utilizáis un modelo diferente por cada estado en
que la entidad opera.
• ¿Tenéis algún problema de desbalanceo de datos? Si es así, solucionadlo.
• ¿Obtenéis mejores resultados planteando modelos diferenciados por estado?

2.4. Ejercicio 4
Plantead un algoritmo de clusterización en el que se pretenda encontrar grupos de
clientes homogéneos.
• ¿Qué características tienen los clientes de cada uno de los grupos?
