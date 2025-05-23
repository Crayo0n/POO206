while True:
    try: 
        print("Introduce 'a' para finalizar\n")
        contraseña= input("Introduce una contraseña: ")
        especiales = "!@#$%^&*()-_=+{}[]:;\"'<>.,?/\\|`~"

        caracterEspecial = False
        for char in contraseña:
            if char in especiales:
                caracterEspecial = True
                break
        
        if contraseña == 'a':
            print("\nFin del programa")
            break
        
        else:
            if not contraseña.strip():
                print("La contraseña no puede estar vacía")
            elif " " in contraseña:
                print("La contraseña no puede tener espacios")
            elif len(contraseña)<=10:
                print("La contraseña es demasiado corta")
            elif not any(char.isdigit() for char in contraseña):
                print("La contraseña debe tener un número")
            elif not caracterEspecial:
                print ("La contraseña debe contener un carácter especial")
            else:
                print("\nLa contraseña es válida\n")
                
    except Exception as Error: 
        print("Error: ", Error)