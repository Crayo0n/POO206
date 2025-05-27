while True:
    
    try: 
        print("Introduce 1 para finalizar\n")
        num= int(input("Introduce un número entero positivo: "))
        if num == 1:
            print("\nFin del programa")
            break
        else:
            if num>0:
                cuentaA = [str(i) for i in range(num, -1, -1)]  
                print("\nCuenta atras de", num, ":", ", ".join(cuentaA))
            else:
                print("Se debe ingresar un número positivo")
    except (ValueError): 
        print("Error: Se ingreso algo diferente a un número")