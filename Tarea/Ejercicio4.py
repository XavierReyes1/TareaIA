##Crea un programa que almacene información sobre productos y sus precios en un diccionario, esta información debe ser ingresada desde teclado.

def productos():
    productos = {}
    while True:
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        productos[producto] = precio
        continuar = input("Desea ingresar otro producto? (s/n): ")
        if continuar == "n":
            break
    return productos

print(productos())

