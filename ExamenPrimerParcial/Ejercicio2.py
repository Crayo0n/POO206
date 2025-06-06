while True:
    try:
        print("Programa descomponedor de palabras")
        a=input("Ingresa 1 para salir del programa o algo más para continuar:")
        
        if a=='1':
            print("Fin del programa")
            break
        elif not a.strip():
            print("No puede estar vacío")
            continue
        
        else:
            palabra=input("Ingresa una palabra para descomponer:")
            
            if not palabra.strip():
                print("No puede estar vacío")
                continue
        
            elif palabra.isdigit():
                print("Los números no son palabras")
                continue
            
            else:
                contador=0
                for i in range(len(palabra)):
                    print("Letra ", contador , " : ", palabra[i])
                    contador=contador+1 
                
    except Exception as error:
        print("Error: ", error)