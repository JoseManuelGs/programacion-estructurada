# main.py
import calificaciones

# Menú principal
def menu_principal():
    print("\n\t..::: Sistema De Calificación :::...\n 1.- Agregar  \n 2.- Mostrar \n 3.- Calcular Promedios \n 4.- Salir")
    opcion = input("\t Elige una opción: ").upper()
    return opcion

# Función principal para administrar el menú
def main():
    opcion = True
    while opcion:
        calificaciones.borrarPantalla()
        opcion = menu_principal()
        
        if opcion == "1":
            calificaciones.agregarCalificacion()
            calificaciones.esperarTecla()
        elif opcion == "2":
            calificaciones.mostrar_calificaciones()
            calificaciones.esperarTecla()
        elif opcion == "3":
            calificaciones.calcular_Promedio()
            calificaciones.esperarTecla()
        elif opcion == "4":
            opcion = False
            print("Terminaste la ejecución del sistema.")
        else:
            input("Opción inválida. Vuelve a intentarlo...")

if __name__ == "__main__":
    main()
