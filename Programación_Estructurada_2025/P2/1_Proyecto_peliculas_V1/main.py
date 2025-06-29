"""Proyecto 1
Crear un proyecto que permita gestionar (administrar peliculas;colocar un menu de opciones para agregar,eliminar,modificar,consultar,buscar y vaciar peliculas.)
Notas:
1-Utilizar funciones y mandar llamar desde otro archivo
2-Utilizar listas para almacenar los nombres de las peliculas"""
import peliculas
import os
os.system("cls")

opcion=True
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n\t 1.- Agregar  \n\t 2.- Eliminar \n\t 3.- Actualizar \n\t 4.- Consultar \n\t 5.- Buscar \n\t 6.- Vaciar \n\t 7.- SALIR ")
    opcion=input("\t\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPelicula()
            peliculas.esperarTecla()
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False    
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case "": 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")
            opcion=True
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")
            "Agregar funcion de buscar y que diga cual es la pelicula que se esta buscando y con que numero se registro"