#ejercicio calcular el promedio de una clase de 10 alumnos 
#usando funciones y lista

def calcular_promedio(lista):   
    suma = sum(lista)
    promedio = suma / len(lista)
    return promedio
lista= [10,9,10,8,7,10,9,8,9,10]
promedio = calcular_promedio(lista)
print(f"El promedio es: {promedio}")

#verifique si una palabra es palindromo

def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    reverso = palabra[::-1] 
    return palabra == reverso
palabra = "anita lava la tina"
palindromo(palabra)
if palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
    
#verifique si una palabra es pangram

import string
def es_pangrama(frase):
    alfabeto = set(string.ascii_lowercase)
    letras_frase = set(frase.lower()) 
    return alfabeto.issubset(letras_frase)
frase = "Pack my box with five dozen liquor jugs. - Mark Dunn"
if es_pangrama(frase):
    print("La frase es un pangrama.")
else:
    print("La frase no es un pangrama.")