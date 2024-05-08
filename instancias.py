from te import Te

# Creando dos instancias de la clase Te
te1 = Te()
te2 = Te()

# Almacenando el tipo de dato de cada instancia
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Mostrando el tipo de dato de cada instancia
print("Tipo de te1:", tipo_te1)
print("Tipo de te2:", tipo_te2)

# Verificando si ambos tipos almacenados son iguales
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
