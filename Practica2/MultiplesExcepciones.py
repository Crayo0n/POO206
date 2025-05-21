try: 
    lista=[1,2,3]
    indice=int(input("Ingrese al indice de la lista que quiere acceder: "))
    print(lista[indice])
except(ValueError, IndexError) as Error:
    print("Error:", Error)