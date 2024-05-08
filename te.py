class Te:
    # Definición de atributos de clase para los precios de los dos formatos
    precio_300gr = 3000
    precio_500gr = 5000

    # Método estático para obtener el tiempo de preparación y recomendación según el sabor
    @staticmethod
    def obt_timp_recomen(sabor):
        if sabor == 1:
            return 3, "Al desayuno"
        elif sabor == 2:
            return 5, "Al medio día"
        elif sabor == 3:
            return 6, "Al atardecer"

    # Método estático para obtener el precio según el formato
    @staticmethod
    def obtener_precio(formato):
        if formato == 300:
            return Te.precio_300gr
        elif formato == 500:
            return Te.precio_500gr
