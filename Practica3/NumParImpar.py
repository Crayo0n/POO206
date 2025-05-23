while True:
    
    try: 
        print("Introduce 100 para finalizar\n")
        num= int(input("Introduce un número: "))
        if num == 100:
            print("\nFin del programa")
            break
        else:
            if num>0:
                if (num%2==0):
                    print("Tu numero ingresado es par\n")
                else:
                    print("Tu numero ingresado es impar \n")
            else:
                print("No se puede ingresar números negativos o 0")
    except (ValueError): 
        print("Error: Se ingreso algo diferente a un número")
        
       

