###INPUT SOLO GUARDA TEXTO, SI SON NUMEROS SE UTILIXA LA FUNCION INT
preciodemanzanas= int(input("Ingresa el precio: "))
cantidaddemanzanas= int(input("Ingresa la cantidad: "))
print("Vas a pagar")
print(preciodemanzanas * cantidaddemanzanas)

#PROCESO DE CONCATENACION

print("las manzanas estan en: " + str(preciodemanzanas))
print("y fueron: " ,cantidaddemanzanas)
print(f"Total a pagar: {preciodemanzanas*cantidaddemanzanas} pesos")