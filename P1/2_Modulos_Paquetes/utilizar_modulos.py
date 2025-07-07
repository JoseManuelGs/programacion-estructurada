# 1er forma de utilizar los modulos 
# import modulos

# modulos.borrarPantalla()
# print(modulos.saludar("Roberto Figeroa Paez"))

#2da forma de utilizar modulos

from modulos import saludar,borrarPantalla, solicitarDatos4

borrarPantalla()
print(saludar("Daniel Contreras Renecio"))


nombre=input("Ingresa el nombre del contacto: ")
telefono=input("Ingresa su numero de telefono con clave lada: ")
nom,tel=solicitarDatos4(nombre,telefono)
print(f"\tNombre Completo: {nom}\n\tTelefono:{tel}")

