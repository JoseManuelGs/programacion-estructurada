#proyecto 3
import calificaciones

# crear un proyecto que permita gestionar(administtar) calificaciones, colocar un menu de opciones para agregar
# ,mostrar y calcular el promedio de calificaciones 

#Notas
# 1.- utilizar funciones y mandar llamar desde otro archivo 
# 2.- utilizar listas para almacenar el nombre y 3 calificaciones de los alumnos

def main():
    opcion=True
    datos=[]
    while opcion:
        calificaciones.borrarPantalla()
        opcion = calificaciones.menu_principal()
        
        match opcion:
            case "1":
                
                calificaciones.agregarCalificacion(datos)
                calificaciones.esperarTecla()
            case "2":
                print(".:: MostrarPeliculas ::.") 
                calificaciones.mostrar_calificaciones(datos)
                input("Oprima cualquier tecla para continuar ...")  
            case "3":
                calificaciones.calcular_Promedio(datos)
            case "4":
                opcion=False    
                print("Terminaste la ejecucion del SW")
            case _:  
                opcion = True
                input("Opción invalida vuelva a intentarlo ... por favor")

if __name__ == "__main__":
    main()