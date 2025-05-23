while True:
    
    try: 
        print("Introduce 1 para finalizar\n")
        año= int(input("Introduce un año a analizar: "))
        if año == 1:
            print("\nFin del programa")
            break
        else:
            if año>0:
                if (año%4==0):
                    print("Tu año ingresado es un año bisiesto\n")
                else:
                    print("Tu año ingresado no es un año bisiesto\n")
            else:
                print("No se puede ingresar años negativos o 0")
    except (ValueError): 
        print("Error: Se ingreso algo diferente a un número")