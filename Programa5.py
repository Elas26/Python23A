##########################FUNCION WHILE############################
contador = 0   
while contador < 5 :
    #print ("contador %d" % contador ) 
    print("Hola")
    #contador= contador + 1 
    contador +=1 #Otra opcion de hacer el contador + 1
    
tabla= 5
numero = 1
while tabla < 51 :
    print(f"5 x {numero} = {tabla}")
    tabla = tabla + 5
    numero = numero + 1

tabla= int(input("Ingresa el numero de tabla a multiplicar: "))
numero_multiplicado = 1
while numero_multiplicado <= 100:
    print(f"{tabla} x {numero_multiplicado} = {tabla * numero_multiplicado} ")
    numero_multiplicado= numero_multiplicado + 1
    
valida = 1
while valida != 0 :
        print("Hola")
        valida = int(input("si quieres salir presiona 0"))

########################## FUNCION FOR ##########################
nombre= "Elizabeth"
for letter in nombre :
    print(letter)

week=["lunes","martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for day in week:
    print(day)  
    
for count, day in enumerate (week) :
    print(count)
    print(day) 
    
######################## RANGO ##################################
rango = range(0,10)
for i in rango:
    print(i)
    
Lista= input("Ingresa una frase: ")
comprobacionA = comprobacionE = comprobacionI= comprobacionO=comprobacionU = False
for Vocals in Lista :
    if "a" in Vocals.lower() and comprobacionA == False :
        print("a")
        comprobacionA=True
    if "e" in Vocals.lower() and comprobacionA == False :
        print("e")
        comprobacionE=True
    if "i" in Vocals.lower() and comprobacionI == False :
        print("i")
        comprobacionI=True
    if "o" in Vocals.lower() and comprobacionO == False :
        print("o")
        comprobacionO=True
    if "u" in Vocals.lower() and comprobacionU == False :
        print("u")
        comprobacionU=True
      