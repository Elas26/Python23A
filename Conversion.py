#EJERCICIO 1  Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.
numero_1:int=float(input("Ingrese numero: "))
numero_2:int=float(input("Ingrese numero: "))
if numero_1 == numero_2 :
    print(f"{numero_1} y {numero_2} son iguales")
elif numero_1 > numero_2 :
    print (f"{numero_1} es mayor a {numero_2}")
elif numero_1 < numero_2 :
    print (f"{numero_1} es menor a {numero_2}")
    
#EJERCICIO 2 Solicitar al usuario un número de cliente. Si el número es el 1000, imprimir "Ganaste un premio". 
cliente:int= float(input("Ingresar numero de cliente: "))
if cliente == 1000 :
    print("¡Ganaste un premio!")
elif cliente < 1000 :
    print("Suerte para la proxima")
elif cliente >1000 :
    print("Suerte para la proxima")

#EJERCICIO 3 Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. No considerar el caso en que ambos números son iguales.
numero1:int=float(input("Ingrese primer numero: "))
numero1_1:int=float(input("Ingrese segundo numero: "))
if numero < numero1_1 :
    print(f"{numero1} es menor")
else : 
    numero1_1 < numero1 
    print(f"{numero1_1} es menor")

#EJERCICIO 5 Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.
Numero1:int=float(input("Ingrese primer numero: "))
Numero2:int=float(input("Ingrese segundo numero: "))
Numero3:int=float(input("Ingrese tercer numero: "))
if (Numero1 == Numero2 and  Numero1 == Numero3 and Numero2 == Numero3) :
    print("Los tres numero son iguales")
elif (Numero1 == Numero2 and Numero1 > Numero3 and Numero2 > Numero3):
    print("Solo Numero 1 y Numero 2 son iguales, Numero 3 es menor")
elif (Numero1==Numero2 and Numero1<Numero3 and Numero2<Numero3) :
    print("Solo Numero 1 y Numero 2 son iguales, Numero 3 es mayor")
elif (Numero1==Numero3 and Numero1>Numero2 and Numero3>Numero2) :
    print("Solo Numero 1 y Numero 3 son iguales, Numero 2 es menor")
elif (Numero1==Numero3 and Numero1<Numero2 and Numero3<Numero2) :
    print("Solo Numero 1 y Numero 3 son iguales, Numero 2 es mayor")
elif (Numero2==Numero3 and Numero2<Numero1 and Numero3<Numero1) :
    print("Solo Numero 2 y Numero 3 son iguales, Numero 1 es mayor")
elif (Numero2==Numero3 and Numero2>Numero1 and Numero3>Numero1):
    print("Solo Numero 2 y Numero 3 son igules, Numero 1 es menor")
else :
    print("Ningun numero es igual")
