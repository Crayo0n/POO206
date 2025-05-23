while True:
    
    try: 
        num= int(input("Introduce un número: "))
        if num>0:
            if (num%2==0):
                print("Tu numero ingresado es par")
            else:
                print("Tu numero ingresado es impar ")
        else:
            print("No se puede ingresar números negativos o 0")
    except (ValueError): 
        print("Error: Se ingreso algo diferente a un número")
        
        break

