import os
import time

def clear():
    if os.name=="posix":
        os.system ("clear")
    elif os.name=="ce" or os.name== "nt" or os.name=="dos":
        os.system ("cls")
    print("".center(40,"x"))

def saludo():
    print("Hola mundo")

def suma(number1, number2):
    number1 *= numerber1
    number2 *= number2 
    total=number1+number2
    return total
    
nombre="Jose"
numero1=2
numero2=2
total=3
clear()
saludo()
total=suma(numero1,numero2)
print(total)
time.sleep(3)
print("Salio")