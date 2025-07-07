import peliculas

opcion=True
while opcion:
    peliculas.borrarpantalla()
    print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()

    match opcion:
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperartecla()
        case "2":
            print(".:: Eliminar Peliculas ::.") 
            peliculas.borrarPeliculas()
            input("Oprima cualquier tecla para continuar ...") 
        case "3":
            print(".:: MostrarPeliculas ::.") 
            peliculas.mostrarPeliculas()
            input("Oprima cualquier tecla para continuar ...")    
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperartecla()
        case "5": 
            peliculas.modificarCaracteristicas()
            peliculas.esperartecla()
        case "6": 
            peliculas.borrarcaracteristicas()
            peliculas.esperartecla()
        case "7":
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _: 
            opcion = True
            input("Opción invalida vuelva a intentarlo ... por favor")