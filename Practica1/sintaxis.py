
#1.- Comentarios

# comentarios de una sola linea
"""
Aqui va un comentario
de varias lineas 
en python
"""

#2.- Strings 
print("Hola soy una cadena") 
print('Yo soy otra')
variable1="hola soy una cadena"
print(len(variable1))
print(variable1[2:5])
print(variable1[2:])
print(variable1[:5])

#3.- Variables

x="Mauricio Rodriguez"
x= 4
x=5.76

print(x)

x= int(3)
y= float(3)
z=str(3)

print (x,y,z)
print(type(x))
print(type(y))
print(type(z))

#4.- Solicitud de datos
a=input("introduce cualquier dato: ")
b=int(input("introduce un numero entero: "))
c=float(input("introduce un numero decimal: "))
print (a,b,c)

#5.- boolean, comparaciones y operadores logicos
print(10>9) 
print(10<9)
print(10==9)
print(10<=9)
print(10>=9)
print(10!=9)

x=1
print(x<5 and x<10)
print(x<5 or x<10) 
print(not(x<5 and x<10))