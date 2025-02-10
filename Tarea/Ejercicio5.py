# Dado el siguiente diccionario:
data = {
 'Ciudad': ['Nueva York', 'Los Ángeles', 'Nueva York', 'Chicago'],
 'Ventas': [100, 150, 200, 50]
}
#Agrupe los datos por ciudad y mostrar la suma por ciudades.

def agrupar_por_ciudad(data):
    ciudades = {}
    for i in range(len(data['Ciudad'])):
        ciudad = data['Ciudad'][i]
        ventas = data['Ventas'][i]
        if ciudad in ciudades:
            ciudades[ciudad] += ventas
        else:
            ciudades[ciudad] = ventas
    return ciudades

print(agrupar_por_ciudad(data))