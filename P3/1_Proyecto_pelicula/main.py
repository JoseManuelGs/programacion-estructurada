import peliculas

def menu_principal():
    opcion = True
    while opcion:
        peliculas.borrarPantalla()
        print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\n\t\t 1.- Crear  \n\t\t 2.- Borrar \n\t\t 3.- Mostrar \n\t\t 4.- Buscar \n\t\t 5.- Modificar \n\t\t 6.- SALIR ")
        opcion = input("\n\t\t Elige una opción: ").upper()

        if opcion == "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        elif opcion == "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla()
        elif opcion == "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        elif opcion == "4":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        elif opcion == "5":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        elif opcion == "6":
            opcion = False
            peliculas.borrarPantalla()
            print("\n\t\tTerminaste la ejecución del SW")
        else:
            input("\n\t\tOpción inválida. Vuelve a intentarlo... por favor")
            
if __name__ == "__main__":
    menu_principal()
