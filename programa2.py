cantidadDeManzanas:int=int(input("Cuantas manaznas compro: "))
precioDeLasManzanas:int=float(input("Las manzanas cuestan:  pelucholares"))
nombre=input("Nombre del comprador: ")
if cantidadDeManzanas==18:
    descuento=(precioDeLasManzanas*cantidadDeManzanas)*.20
    print(f"Tienes descuento secreto de: {descuento}%")
    print(f"Pagaras:{(precioDeLasManzanas*cantidadDeManzanas)-descuento} pelucholares")
elif nombre=="Elizabeth":
    descuento=((precioDeLasManzanas*cantidadDeManzanas)*.20)
    print(f"Descuento Especial: {descuento}%")
    print(f"Pagaras:{(precioDeLasManzanas*cantidadDeManzanas)-descuento} pelucholares")
elif cantidadDeManzanas>=10:
    descuento=(precioDeLasManzanas*cantidadDeManzanas)*.10
    print(f"Descuento: {descuento}%")
    print(f"Pagaras:{(precioDeLasManzanas*cantidadDeManzanas)-descuento} pelucholares")

else:
    descuento=0 
    print(f"pagaras {precioDeLasManzanas*cantidadDeManzanas} pelucholares")
  
    
