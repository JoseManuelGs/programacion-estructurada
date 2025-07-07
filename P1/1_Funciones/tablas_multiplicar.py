"""""
crear un programa que calcule e imprima cualquier tabla de multiplicar 

restricciones
sin estructuras de control
sin funcions
"""
#version 1
uno = int(2)
uno1 = uno * 1
uno2 = uno * 2
uno3 = uno * 3
uno4 = uno * 4
uno5 = uno * 5
uno6 = uno * 6
uno7 = uno * 7
uno8 = uno * 8
uno9 = uno * 9
uno10 = uno * 10

print(uno1,uno2,uno3,uno4,uno5,uno6,uno7,uno8,uno9,uno10)

#version 2
uno = int(input("Numero; "))
uno1 = uno * 1
uno2 = uno * 2
uno3 = uno * 3
uno4 = uno * 4
uno5 = uno * 5
uno6 = uno * 6
uno7 = uno * 7
uno8 = uno * 8
uno9 = uno * 9
uno10 = uno * 10

print(uno1,uno2,uno3,uno4,uno5,uno6,uno7,uno8,uno9,uno10)

#version 3
numero = int(input("Numero: "))
for i in range (1,10+1):
    multi = numero * i
    print(multi)

#version 4
num1=int(input("Numero: "))
def tablamultiplicacion(num1):
    numero=num1
    for i in range(1,10+1):
       multi = numero * i
       print(multi)

    return(multi)

print(tablamultiplicacion(num1))