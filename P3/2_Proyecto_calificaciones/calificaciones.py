# calificaciones.py
import mysql.connector
from mysql.connector import Error

# Función para borrar la pantalla
def borrarPantalla():
    import os
    os.system("cls")

# Función para esperar una tecla
def esperarTecla():
    input("Pulsa para continuar...")

# Conexión a la base de datos
def conectar():
    try:
        conexion = mysql.connector.connect(
        host="127.0.0.1",  # IP local, asegúrate que sea correcta
        user="root",        # Usuario de la base de datos
        password="",        # Contraseña (vacía en tu caso)
        database="calificaciones",# Nombre de la base de datos
        port=4306           # Puerto configurado en tu my.cnf
    )
        return conexion
    except Error as e:
        print(f"El error que ocurrió es: {e}")
        return None

# Función para agregar calificación
def agregarCalificacion():
    borrarPantalla()
    print("Agregar Calificaciones")
    nombre = input("Ingrese el nombre del alumno: ").upper().strip()
    calificaciones = []

    # Obtener las calificaciones
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
                print("Ingrese un valor numérico válido")

    # Conectar a la base de datos
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "INSERT INTO calificaciones (nombre, calificacion1, calificacion2, calificacion3) VALUES (%s, %s, %s, %s)"
        valores = (nombre, calificaciones[0], calificaciones[1], calificaciones[2])
        cursor.execute(sql, valores)
        conexionBD.commit()
        print("Acción realizada con éxito")
        conexionBD.close()

# Función para mostrar las calificaciones
def mostrar_calificaciones():
    borrarPantalla()
    print("Mostrar Calificaciones")
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        # Consulta SQL incluyendo el campo 'promedio'
        sql = "SELECT id, nombre, calificacion1, calificacion2, calificacion3, promedio FROM calificaciones"
        cursor.execute(sql)
        registros = cursor.fetchall()

        if registros:
            print(f"{'ID':<5}{'Nombre':<15}{'Calif.1':<10}{'Calif.2':<10}{'Calif.3':<10}{'Promedio':<10}")
            print("-" * 70)
            for fila in registros:
                # Si el promedio es None, asignamos un valor por defecto o vacío
                promedio = fila[5] if fila[5] is not None else "N/A"
                print(f"{fila[0]:<5}{fila[1]:<15}{fila[2]:<10}{fila[3]:<10}{fila[4]:<10}{promedio:<10}")
            print("-" * 70)
        else:
            print("No hay calificaciones registradas.")
        conexionBD.close()

# Función para calcular y actualizar los promedios
def calcular_Promedio():
    borrarPantalla()
    print("Calcular Promedios")
    conexionBD = conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT id, nombre, calificacion1, calificacion2, calificacion3 FROM calificaciones"
        cursor.execute(sql)
        registros = cursor.fetchall()

        if registros:
            for fila in registros:
                promedio = (fila[2] + fila[3] + fila[4]) / 3
                sql_update = "UPDATE calificaciones SET promedio = %s WHERE id = %s"
                cursor.execute(sql_update, (promedio, fila[0]))
                conexionBD.commit()

            print("Promedios actualizados con éxito.")

            # Mostrar los promedios actualizados de todos los estudiantes
            print("\nListado de Promedios Actualizados:")
            print(f"{'Nombre':<15}{'Promedio':<10}")
            print("-" * 30)
            for fila in registros:
                # Volver a obtener el nombre y el promedio actualizado
                cursor.execute("SELECT nombre, promedio FROM calificaciones WHERE id = %s", (fila[0],))
                resultado = cursor.fetchone()
                print(f"{resultado[0]:<15}{resultado[1]:<10.2f}")
            print("-" * 30)

        else:
            print("No hay calificaciones para calcular el promedio.")
        conexionBD.close()
