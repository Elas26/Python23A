###INPUT SOLO GUARDA TEXTO, SI SON NUMEROS SE UTILIXA LA FUNCION INT
preciodemanzanas= int(input("Ingresa el precio: "))
cantidaddemanzanas= int(input("Ingresa la cantidad: "))
if cantidaddemanzanas >= 10:
    descuento=(preciodemanzanas*cantidaddemanzanas)*.1
print(f"Las manzanas estan en: {preciodemanzanas} y fueron: {cantidaddemanzanas}")
if(descuento >0):
    print(f"El descuento fue de: {descuento}")
print((preciodemanzanas*cantidaddemanzanas)-descuento)