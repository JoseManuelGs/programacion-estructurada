import os 
os.system("cls")

# Ejemplo 1: Crear una lista de numeros e imprimir su contenido

numeros_lista = [10, 20, 30, 40, 50]
print("Lista de números enteros:")
print(numeros_lista)

# Ejemplo 2: Crear una lista de palabras y buscar si una fruta está presente
frutas = ["pera", "naranja", "sandía", "melón"]
buscar = "naranja"
if buscar in frutas:
    print(f"Se encontró la fruta: '{buscar}' en la lista.")
else:
    print(f"La fruta '{buscar}' no está en la lista.")

# Ejemplo 3: Agregar un nuevo elemento a la lista
frutas.append("mango")
print("Lista de frutas actualizada:")
print(frutas)

# Ejemplo 4: Crear una lista compuesta con nombres y números telefónicos (agenda)
contactos = [
    ["Carlos", "618-1122-334"],
    ["María", "618-3344-556"],
    ["Elena", "618-7788-990"]
]

print("Lista de contactos telefónicos:")
for persona in contactos:
    print(f"Contacto: {persona[0]} | Tel: {persona[1]}")
