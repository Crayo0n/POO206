while True:
    
    try: 
        print("Introduce 1 para finalizar\n")
        num= int(input("Introduce un número entero positivo mayor de 10: "))
        if num == 1:
            print("\nFin del programa")
            break
        else:
            if num>10:
                impares = [str(i) for i in range(3, num+1, 2)]  
                print("\nNúmeros impares desde 2 hasta ", num, ":", ", ".join(impares))
            else:
                print("Se debe ingresar un número mayor a 10")
    except (ValueError): 
        print("Error: Se ingreso algo diferente a un número")