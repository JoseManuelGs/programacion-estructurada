# main.py
import agenda

def main():
    opcion = True

    while opcion:
        agenda.borrarPantalla()
        print(
        "\n\t\t📓.:: Sistema de Gestion de Agenda de Contactos ::.📓"
        "\n\n\t\t 1️⃣  Agregar Contacto"
        "\n\t\t 2️⃣  Mostrar todos los contactos"
        "\n\t\t 3️⃣  Buscar Contacto por nombre"
        "\n\t\t 4️⃣  Modificar"
        "\n\t\t 5️⃣  Eliminar"
        "\n\t\t 6️⃣  SALIR")
        
        opcion = input("\n\t\t 👉 Elija una opcion (1-6): ")

        match opcion:
            case "1":
                agenda.agregar_contacto()
                agenda.esperarTecla()
            
            case "2":
                agenda.mostrar_contactos()
                agenda.esperarTecla()

            case "3":
                agenda.buscar_contacto()
                agenda.esperarTecla()
            
            case "4":
                agenda.modificar_contacto()
                agenda.esperarTecla()
                
            case "5":
                agenda.borrar_contacto()
                agenda.esperarTecla()
                
            case "6":
                opcion = False
                agenda.borrarPantalla()
                print("\t👋Terminaste la ejecución del SW")
                
            case _:
                opcion = True
                input("Opción invalida vuelva a intentarlo... por favor")

                
if __name__ == "__main__":
    main()
