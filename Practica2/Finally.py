try:
    archivo = open("mi_archivo.txt", "w")
    archivo.write("Hola mundo")
except IOError:
    print("Error al escribir en el archivo")
finally:
    archivo.close()
    print("El archivo ha sido cerrado")
