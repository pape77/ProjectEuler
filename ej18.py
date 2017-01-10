# leer datos
datos = []
with open('problem-18-data') as f:
    for line in f:
        datos.append([int(i) for i in line.rstrip('\n').split(" ")])

#print(datos)

"""
La idea es, empezando desde la anteultima fila, ir reemplazando
la suma más grande por cada elemento de esa fila, y moverse hacia arriba
Al final de todo, la maxima suma estará en el tope de la pirámide
"""

def encontrarMaximaSuma(datos,filaActual):
    for i in range(len(datos[filaActual])):
        #me fijo el de la izquierda abajo y el de la derecha abajo
        datos[filaActual][i] += (max(datos[filaActual+1][i],datos[filaActual+1][i+1]))
    if filaActual != 0:
        return encontrarMaximaSuma(datos,filaActual-1)
    else:
        return datos[0][0]


print(encontrarMaximaSuma(datos,len(datos)-2))
