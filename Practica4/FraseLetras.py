while True:
    
    try: 
        print("Introduce 1 para finalizar\n")
        frase= input("Introduce una frase: ")
        letra= input("\nIntroduce una letra para buscar en la frase: ")
        if frase == '1':
            print("\nFin del programa")
            break
        else:
            if len(frase)>0:
                contador=0
                for i in range(len(frase)):
                    elemento=frase[i]
                    if letra==elemento:
                        contador=contador+1
                print("La letra ", letra , " aparece ", contador ,"veces")
    except Exception as Error: 
        print("Error: ", Error)