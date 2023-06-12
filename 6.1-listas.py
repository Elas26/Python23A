milista=[4,5,7,2,87,54,32]
print(milista)
print(milista[5]) #extraer un valor de la lista
print(len(milista)) #cuantos valores tiene
milista.append(13) #Apilar valores al final de la lista
print(milista)
milista.sort()
for count, element in enumerate(milista) :
    print(f"contador {count} element {element}")
    
if 7 in milista :
    print("si esta el siete")

print(milista.index(7))
