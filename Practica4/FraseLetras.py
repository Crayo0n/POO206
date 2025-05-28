while True:
    
    try: 
        print("Introduce 1 para finalizar\n")
        frase= input("Introduce una frase: ")
        
        if frase == '1':
            print("\nFin del programa")
            break
    
        elif frase.isdigit():
            print("Los números no son frases para analizar\n")
            continue
        
        elif not frase.strip():
            print("La frase no puede estar vacia\n")
            continue
                
        letra= input("\nIntroduce una letra para buscar en la frase: ")
        if not letra.strip():
            print("La letra no puede estar vacia")
            continue
        
        elif len(letra)!=1:
            print("\nSolo debes introducir una letra")
            continue
        
        elif letra.isdigit():
            print("No se puede introducir números")
            continue
        
        contador=0
        for i in range(len(frase)):
            elemento=frase[i]
            if letra==elemento:
                contador=contador+1
        print("La letra '", letra , "' aparece ", contador ,"veces\n")
        
    except Exception as Error: 
        print("Error: ", Error)