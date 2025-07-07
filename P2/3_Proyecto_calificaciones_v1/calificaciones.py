def esperarTecla():
    input("Pulsa para continuar")

# lista = [
#     ["Ruben",10.0,8.9,9.2],
#     ["Andres",10.0,10.0,10.0],
#     ["Maria",10.0,10.0,10.0]
# ]

def borrarPantalla():
    import os
    os.system("cls")

def menu_principal():
    print("\n\t..::: Sistema De Calificación :::...\n 1.- Agregar  \n 2.- mostrar \n 3.- Calcular Promedios \n 4.- Salir")
    opcion=input("\t Elige una opción: ").upper()
    return opcion 

def agregarCalificacion(lista):
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre = input("Ingrese el nombre del alumno: ").upper().strip()
    calificaciones = []  # <-- Moverla fuera del for
    for i in range(1, 4):
        continua = True
        while continua:
            try:
                cal = float(input(f"Ingrese calificación {i}: "))
                if 0 <= cal <= 10:
                    calificaciones.append(cal)
                    continua = False
                else:
                    print("Ingrese un valor comprendido entre 0 y 10")
            except ValueError:
                print("Ingrese un valor numérico")
    lista.append([nombre] + calificaciones)
    print("Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar Calificaciones")
    if len(lista)>0:
        print(f"{"Nombre":<15}{"calif.1":<10}{"calif.2":<10}{"calif.3":<10}")
        print("-"*60)
        for fila in lista:
            print(f"{fila[0]}   {fila[1]}   {fila[2]}   {fila[3]}")
            print(f"son {len(lista)} alumnos ")
        print("-"*60)
    else:
        print("No hay calificaciones")

def calcular_Promedio(lista):
    borrarPantalla()
    print("Promedios")
    promedio_clase=0
    alumnos=0
    if len(lista)>0:
        print(f"{"Nombre" :<15}{"Promedio":<10}")
        print("-"*30)
        for fila in lista:
            promedio=((fila[1])+(fila[2])+(fila[3]))/3
            print(f"{fila[0]:<15}{promedio:<10}")
            promedio_clase+=promedio
            alumnos+=1
        print("-"*30)
        print(f"Son {len(lista)} alumnos y tienen el promedio de {promedio_clase/alumnos}")
    else:
        print("No hay calificaiones en el sistema")
    
    esperarTecla()