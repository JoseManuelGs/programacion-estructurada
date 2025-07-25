# agenda.py
import mysql.connector
from mysql.connector import Error

# Función para borrar la pantalla
def borrarPantalla():
    import os
    os.system("cls")

# Función para esperar una tecla
def esperarTecla():
    input("Presione una tecla para continuar...")

# Conexión a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(
        host="127.0.0.1",  # IP local, asegúrate que sea correcta
        user="root",        # Usuario de la base de datos
        password="",        # Contraseña (vacía en tu caso)
        database="agenda_contactos",  # Nombre de la base de datos
        port=4306           # Puerto configurado en tu my.cnf
    )
        return conexion
    except Error as e:
        print(f"El error que ocurrió es: {e}")
        return None

# Función para agregar un contacto
def agregar_contacto():
    borrarPantalla()
    print("\t\t\t.::: Agregar Contacto :::. 📱")
    print("=" * 60)
    nombre = input("\t\tIngrese el nombre del contacto: ").upper().strip()

    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (nombre,))
        if cursor.fetchone():
            print("Ya existe 😕")
        else:
            tel = input("Telefono 📞: ").upper().strip()
            email = input("Email 📧: ").upper().strip()
            sql = "INSERT INTO contactos (nombre, telefono, email) VALUES (%s, %s, %s)"
            valores = (nombre, tel, email)
            cursor.execute(sql, valores)
            conexionBD.commit()
            print("=" * 60)
            print("Accion realizada con Exito ✅")
        conexionBD.close()

# Función para mostrar todos los contactos
def mostrar_contactos():
    borrarPantalla()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT id, nombre, telefono, email FROM contactos"
        cursor.execute(sql)
        registros = cursor.fetchall()

        if registros:
            print("\t\t\t.::: Agenda :::. 📚")
            print(f"{'ID':<5}{'Nombre':<15}{'Telefono':<15}{'Email':<15}")
            print("=" * 60)
            for fila in registros:
                print(f"{fila[0]:<5}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}")
            print("=" * 60)
        else:
            print("=" * 90)
            print(f"\t\tNo hay contactos 😔")
            print("=" * 90)
        conexionBD.close()

# Función para buscar un contacto por nombre
def buscar_contacto():
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto a buscar 🔍: ").upper().strip()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT nombre, telefono, email FROM contactos WHERE nombre = %s", (buscar,))
        persona = cursor.fetchone()
        if persona:
            print("=" * 60)
            print(f"{"Nombre":<15} {"Telefono":<15} {"Email":<15}")
            print("=" * 60)
            print(f"{persona[0]:<15} {persona[1]:<15} {persona[2]:<15}")
            print("=" * 60)
        else:
            print("=" * 60)
            print("No existe el contacto... Vuelva a intentarlo por favor 😔")
        conexionBD.close()

# Función para modificar un contacto
def modificar_contacto():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de un contacto ::. ✏️\n")
    buscar = input("Ingrese el nombre de la persona que quiere modificar 🖊️: ").upper().strip()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT telefono, email FROM contactos WHERE nombre = %s", (buscar,))
        persona = cursor.fetchone()

        if persona:
            print(f"\n\t.:: Los datos de {buscar} son: ::.\n")
            print(f"\n\t\tTelefono: {persona[0]}")
            print(f"\n\t\tEmail: {persona[1]}")
            
            dato = input("\nIngresa el nombre de la característica que deseas modificar (Telefono/Email): ").upper().strip()
            
            if dato == "TELEFONO":
                nuevo_valor = input("Ingresa el nuevo numero telefonico 📱: ").upper().strip()
                sql_update = "UPDATE contactos SET telefono = %s WHERE nombre = %s"
                cursor.execute(sql_update, (nuevo_valor, buscar))
                conexionBD.commit()
                print("La operacion se realizo con exito ✅")
            elif dato == "EMAIL":
                nuevo_valor = input("Ingresa el nuevo email 📧: ").upper().strip()
                sql_update = "UPDATE contactos SET email = %s WHERE nombre = %s"
                cursor.execute(sql_update, (nuevo_valor, buscar))
                conexionBD.commit()
                print("=" * 60)
                print("La operacion se realizo con exito ✅")
            else:
                print("\n\t\t::: La característica no existe ::: ❌")
        else:
            print("=" * 60)
            print("\t..:: No esta esa persona en la agenda ::.. 😕")
        conexionBD.close()

# Función para borrar un contacto
def borrar_contacto():
    borrarPantalla()
    buscar = input("Ingrese el nombre del contacto que desea borrar 🗑️: ").upper().strip()
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        cursor.execute("SELECT * FROM contactos WHERE nombre = %s", (buscar,))
        if cursor.fetchone():
            resp = input(f"Se encontro a {buscar}, deseas eliminarla de la agenda (Si/No)? 🗑️: ").upper().strip()
            if resp == "SI":
                sql = "DELETE FROM contactos WHERE nombre = %s"
                cursor.execute(sql, (buscar,))
                conexionBD.commit()
                print("=" * 60)
                print("La operacion se realizo con Exito ✅")
        else:
            print("=" * 60)
            print("No existe el contacto... Vuelva a intentarlo por favor 😔")
        conexionBD.close()
