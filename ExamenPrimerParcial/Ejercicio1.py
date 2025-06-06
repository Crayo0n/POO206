while True:
    try:
        print("Ejercicio de palabra más larga")
        a=input("Ingresa 1 para terminar el programa, o algo más para continuar:")
        if a=='1':
            print("Fin del programa")
            break
        elif not a.strip():
            print("No puede estar vacio")
            continue
        
        else:
            primeraP=input("Ingresa la primera palabra:")
            segundaP=input("Ingresa la segunda palabra:")
            L1=len(primeraP)
            L2=len(segundaP)
            LT= L1-L2
            
            if primeraP.isdigit() or segundaP.isdigit():
                print("Los números no son palabras")
                continue
            
            elif not primeraP.strip() or not segundaP.strip():
                print("Las palabras no pueden estar vacias")
                continue
            
            else:
                
                if L1>L2:
                    print("La palabra '", primeraP, "' es más grande que '", segundaP,"' con ", LT ," letras")
                
                elif L2>L1:
                    print("La palabra '", segundaP, "' es más grande que '", primeraP,"' con ", (-1)*LT ," letras")
            
                else:
                    print("Las palabras son del mismo tamaño")
                
    except Exception as error:
        print("Error: ", error)