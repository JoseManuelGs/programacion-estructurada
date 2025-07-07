

#dict u objeto para almacenar los atributos (nombre,categoria,clasificacion,genero, idioma)

# pelicula={
#     "Nombre":"",
#     "Categoria":"",
#     "Genero":"",
#     "idioma":""
# }

pelicula={}

def borrarpantalla():
    import os
    os.system("cls")

def esperartecla():
    input(".::oprima cualquier tecla para continuar::. ")

def crearPeliculas():
    borrarpantalla()
    print("crear peliculas")
    pelicula.update({"nombre":input("Ingresa el nombre").upper().strip()})
    # pelicula["Nombre"]=input("Ingrese el nombre").upper().strip()
    pelicula.update({"Categoria":input("Ingresa la Categoria").upper().strip()})
    pelicula.update({"Clasificacion":input("Ingresa la Clasificacion").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma").upper().strip()})

def mostrarPeliculas():
    borrarpantalla()
    print("Mostrar Peliculas")
    if len(pelicula)> 0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
    else:
        print("\t .::no hay peliculas en el sistema::.")

def agregarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t.:: Agregar Característica a Películas ::.\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor = input("Ingresa el valor de la característica de la película: ").upper().strip()
    # pelicula.update({atributo:valor})
    pelicula[atributo]=valor
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def borrarCaracteristicaPeliculas():
    borrarpantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for clave in pelicula:
            print(f"\t{clave}: {pelicula[clave]}")
        atributo = input("\nIngresa el nombre de la característica que deseas borrar: ").lower().strip()
        if atributo in pelicula:
            del pelicula[atributo]
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        else:
            print("\n\t\t::: La característica no existe :::")
    else:
        print("\t..:: No hay películas en el sistema ::..")

def borrarPeliculas():
    borrarpantalla()
    if len(pelicula)>0:
        resp=input("¿desea borrar todas las caracteristicas").upper().strip()
        if resp=="si":
            pelicula.clear()
            print("Operacion con exito")

    else:
        print("No hay Peliculas")

def modificarCaracteristicas():
    borrarpantalla()
    print(".:: Modificar Caracteristicas ::.")
    if len(pelicula)>0:
     for i in pelicula:
        print(f"{i} : {pelicula[i]}")
        resp=input(f"deseas modificar el valor de la caracteristica de {i}? (si/no): ").lower().strip()
        if resp=="si":
            pelicula[i]=input(f"Ingresa el nuevo valor de la caracteristica {i}; ").lower().strip()
            print("Operacion se realizo con exito")
    else:
        print("No hay pelicula")

def borrarcaracteristicas():
    borrarpantalla()
    print(".:: Borrar Caracteristicas a Peliculas ::.")
    print("\n Valores actuales: ")
    if len(pelicula)>0:
        start = True
    else: start= False
    while start:
        if len(pelicula)> 0:
            
            for i in pelicula:
                print(f"{i} : {pelicula[i]}")
        else:
            print("\t .::no hay peliculas en el sistema::.")
        resp=input(f"que caracteristica te gustaria borrar: ").lower().strip()
        if resp in pelicula:
            if resp in pelicula:
                    pelicula.pop(resp)
                    print("LA OPERACIÓN SE REALIZO CON EXITO")
                    decision = input("¿Desea borrar otra caracteristica? SI/NO: ").upper().strip()
                    if decision == "SI":
                        start= True
                    elif decision == "NO":
                        start = False
                    else:
                        print("Elija una de las opciones validas (SI/NO)")
                        start= True
        else:
            "no hay ninguna pelicula con ese nombre"
        
    

# def agregarpeliculas():
#     peliculas.append(input("Ingresa el nombre de la pelicula: ").upper().strip())
#     input("!!!LA OPERACIÓN SE REALIZO CON EXITO!!!")

# def consultarpeliculas():
#     borrarpantalla()
#     print("consultar o mostrar peliculas")
   
#     if len(peliculas)>0:
#          for i in range(0,len(peliculas)):
#             print(f"{i+1} : {peliculas }[i] ")
#     else:
#         print("No hay peliculas en el sistema")

# def vaciarpeliculas():
#     print("Vaciar o borrar todas las peliculas")
#     resp=input("¿desea borrar todas las peliculas? SI/NO: ").upper()
#     if resp == "SI":
#         peliculas.clear()
#         print("!!!LA OPERACIÓN SE REALIZO CON EXITO!!!")
    

# def buscarPelicula():
#     borrarpantalla()
#     pelicula_buscar = input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
#     if not (pelicula_buscar in peliculas):
#         print("No hay ninguna pelicula con este nombre")

#     else: 
#         encontro = 0
#         for i in range(0,len(peliculas)):
#             if pelicula_buscar == peliculas [i]:
#                 print( f"La pelicula {pelicula_buscar} si la tenemos, y esta en el casillero {i+1}")
#                 encontro+=1
#                 print(f"Tenemos {encontro} pelicula(s) con este titulo")
                    
# def modificarPeliculas():
#     pelicula_buscar = input("Ingresa el nombre de la pelicula a buscar: ").upper().strip()
#     if not (pelicula_buscar in peliculas):
#         print("No hay ninguna pelicula con este nombre")

#     else: 
#         encontro = 0
#         for i in range(0,len(peliculas)):
#             if pelicula_buscar == peliculas [i]:
#                 resp=input("¿deseas modificar ña pelicula (SI/NO)").upper().strip()
#                 if resp=="SI":
#                     peliculas[i] = input("introduzca el nuevo valor de la pelicula").upper().strip()
#                     encontro+=1
#         print(f"se actualizaron {encontro} pelicula(s) con este titulo")
            
# def borrarPeliculas():
#     pelicula_borrar = input("Ingresa el nombre de la pelicula a borrar: ").upper().strip()
#     if not (pelicula_borrar in peliculas):
#         print("No hay ninguna pelicula con este nombre")
#     else: 
#         borradas = 0
#         for i in range(0,len(peliculas)):
#             if pelicula_borrar == peliculas [i]:
                
#                 while pelicula_borrar in peliculas:
#                     resp=input("¿deseas eliminar o borrar la pelicula del sistema (SI/NO): ").upper().strip()
#                     if resp=="SI":
                        
#                         peliculas.remove(pelicula_borrar)
#                         borradas+=1
                
#             print(f"se borraron {borradas} pelicula(s) con este titulo")
                    


    
#pedir pelicula a buscar despues asesiore si existe que diga donde se encontro o categoria 1 si se repite
#se repita el mensaje al final "se encontrarion tantas peliculas con el mismo nombr