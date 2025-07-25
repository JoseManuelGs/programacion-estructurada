# conexionBD.py
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host="127.0.0.1",  # IP local, asegúrate que sea correcta
        user="root",        # Usuario de la base de datos
        password="",        # Contraseña (vacía en tu caso)
        database="bd_notas",# Nombre de la base de datos
        port=4306           # Puerto configurado en tu my.cnf
    )
    cursor = conexion.cursor(buffered=True)  # Crear cursor
except mysql.connector.Error as err:
    print(f"En este momento no es posible comunicarse con el sistema. Error: {err}")
    conexion = None
    cursor = None
