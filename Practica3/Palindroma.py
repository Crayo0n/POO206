while True:
        def Numeros(frase):
            if frase.isdigit():
                raise ValueError("No se puede analizar números")
            return frase
        
        try: 
            print("Introduce 'a' para finalizar \n")
            frase= input("Ingresa una frase para analizar: ").lower()
            Numeros(frase)
            if frase == "a":
                print("\nFin del programa")
                break
            
            else:
                if frase==frase[::-1] :
                    print("La frase ingresada es un palíndromo\n")
                else:
                    print("La frase ingresada no es un palíndromo\n")
                    
        except (ValueError) as Error:
            print("Error ocurido :", Error)