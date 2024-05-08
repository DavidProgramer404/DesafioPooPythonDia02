from te import Te

# Mostrando las opciones de sabor al usuario
print("Ingrese el número correspondiente al sabor:")
print("1: Té negro")
print("2: Té verde")
print("3: Agua de hierbas")

# Pedir al usuario el sabor
sabor = int(input("Opción: "))
print("---------------------------------------")

# Mostrar mensaje indicando el sabor seleccionado
if sabor == 1:
    print("Has seleccionado Té negro.")
elif sabor == 2:
    print("Has seleccionado Té verde.")
elif sabor == 3:
    print("Has seleccionado Agua de hierbas.")

# Pedir al usuario el formato
formato = int(input("Ingrese el formato (300 para 300 gr, 500 para 500 gr): "))

print("---------------------------------------")

# Obtener el tiempo y recomendación según el sabor ingresado
tiempo, recomendacion = Te.obt_timp_recomen(sabor)

# Obtener el precio según el formato ingresado
precio = Te.obtener_precio(formato)

# Mostrar en pantalla el detalle del pedido
print("Detalle del pedido:")
print("Sabor:", end=" ")
if sabor == 1:
    print("Té negro")
elif sabor == 2:
    print("Té verde")
elif sabor == 3:
    print("Agua de hierbas")

print("Formato:", formato, "gr")
print("Precio: $", precio)
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)
