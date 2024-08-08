


## ESTADOS DE ESTADOS UNIDOS 

# Este reto es de Repaso libreria Folium, manejo de diccionarios, funciones, transformación y cálculos de los datos.

1. Disponemos de información de ciertos estados de Estados Unidos que necesitaremos para este reto: 
• Estado: nombre del Estado 
• Población 2000: población del Estado en el año 2000 
• Población 2001: población del Estado en el año 2001 
• Residentes menores de 65 años 2000: número de personas menores de 65 años en el Estado en el año 2000 
• Residentes menores de 65 años 2001: número de personas menores de 65 años en el Estado en el año 2001 
• Muertes 2000: fallecidos en el Estado en el año 2000 
• Muertes 2001: fallecidos en el Estado en el año 2001 
• Fecha de fundación del Estado: fecha en que se fundó el Estado 
• Latitud: latitud correspondiente a la capital del Estado • Longitud: longitud correspondiente a la capital del Estado La información disponible es la siguiente: 

estados = [
    {'estado': 'Alabama', 'poblacion_2000': 4447100, 'poblacion_2001': 4451493, 'residentes_menores_65_2000': 3870598, 'residentes_menores_65_2001': 3880476, 'muertes_2000': 10622, 'muertes_2001': 15912, 'latitud': '33.258882', 'longitud': '-86.829534', 'Fecha_fundacion': '14-12-1819' },
    {'estado': 'Florida', 'poblacion_2000': 15982378, 'poblacion_2001': 17054000, 'residentes_menores_65_2000': 13237167, 'residentes_menores_65_2001': 13548077, 'muertes_2000': 38103, 'muertes_2001': 166069, 'latitud': '27.756767', 'longitud': '-81.463983','Fecha_fundacion': '03-03-1845' },
    {'estado': 'Georgia', 'poblacion_2000': 8186453, 'poblacion_2001': 8229823, 'residentes_menores_65_2000': 7440877, 'residentes_menores_65_2001': 7582146, 'muertes_2000': 14804, 'muertes_2001': 15000, 'latitud': '32.329381', 'longitud': '-83.113737', 'Fecha_fundacion': '12-02-1733' },
    {'estado': 'South Carolina', 'poblacion_2000': 4012012, 'poblacion_2001': 4023438, 'residentes_menores_65_2000': 3535770, 'residentes_menores_65_2001': 3567172, 'muertes_2000': 8581, 'muertes_2001': 9500, 'latitud': '33.687439', 'longitud': '-80.436374', 'Fecha_fundacion': '26-03-1776'  },
]
2. 


2.1. Ejercicio 1
a. Cread una lista que contenga un diccionario por cada estado. Cada elemento de la
lista será un diccionario.
b. Transformad la lista inicial en tantos diccionarios como Estados tengamos. 
PISTA: buscad la función zip para iterar listas
c. Se ha detectado que los datos de población de Florida en 2001 eran incorrectos,
corregidlo actualizando su valor a:
5
Población 2001: 16054328
d. En cada diccionario, incluid una nueva clave “Días desde fundación
nombre_estado” que sea el número de días que han pasado desde la fundación del
Estado hasta la actualidad. ¿Cuál sería el número de meses?
e. Calculad una nueva clave del diccionario que sea “Porcentaje mayores de 65 años
nombre_estado”
f. Desarrollad un programa que imprima por pantalla el nombre del Estado más
antiguo y el más moderno (es necesario que sea dinámico y que el programa sirva
para 3 estados como para 50). ¿Cuántos años de diferencia hay entre ellos?
2.2. Ejercicio 2
Vamos a asumir que la tasa de crecimiento de población para 2002 de los estados de
Alabama y South Carolina son dos números aleatorios entre 0 y 0.1. Asignaremos a
Alabama el ratio de crecimiento menor y a South Carolina el ratio de crecimiento mayor.
Vamos a asumir también la población de 2001 de ambos estados descrita en los ejercicios
anteriores.
Con esta información:
a. ¿Cuántos años tardará el estado de South Carolina en alcanzar en población a
Alabama?
b. ¿En qué año ocurrirá esto?
c. Si al planteamiento anterior le añadimos la tasa de fallecidos de cada estado.
¿Cuántos años tardará South Carolina en alcanzar en población a Alabama? Vamos
a asumir la tasa de fallecidos y la población correspondientes a 2021.
2.3. Ejercicio 3
Cread una función que genere una proyección para el año 2002, utilizando como ratio la
comparativa entre los años 2000 y 2001. De tal forma:
Población Año 2002 = Población Año 2001 / Población Año 2000 x Población año 2001.
Tras un estudio demográfico se ha determinado que el número de habitantes de cierta
población, en los próximos años, vendrá dado por la función: P(t) = 14500t + 7000/2t + 1
donde t son los años transcurridos entre la fundación del Estado y 1900.
En la misma función, devolved la población que tendría cada Estado bajo la estimación que
devuelve ese estudio demográfico.
Añadid los resultados a cada diccionario de la lista.
6
2.4. Ejercicio 4
Cread un mapa utilizando la librería Folium y utilizando bucles, donde se representen con
un marcador de color azul (color=”blue”) los datos de población del 2002 para cada uno de
los estados, estando posicionados estos círculos en las coordenadas que se facilitan.
Inicializa el mapa en las coordenadas:
Latitud: 30.101271
Longitud: -82.370146
Zoom inicial: 6
Para el tamaño de los círculos, toma como radio el resultado de dividir la población de 2002
entre 100:
Radio = Población en 2002 / 100
Nota: Es posible que Jupyter Notebook entregue un mensaje diciendo que debéis verificar
el notebook para poder incluir el mapa. Pulsad en File -> Trusted Notebook para verificarlo