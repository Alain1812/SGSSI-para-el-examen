# Solicitar al usuario que ingrese el nombre del archivo de texto
nombre_archivo = input("Ingrese el nombre del archivo de texto (incluyendo la extensión, por ejemplo 'texto.txt'): ")

# Intentar abrir el archivo y leer su contenido
try:
    with open(nombre_archivo, 'r') as archivo:
        texto = archivo.read()
except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    exit()

# Crear un diccionario para contar las apariciones de cada letra
apariciones = {}

# Recorrer el texto y contar las apariciones de cada letra
for letra in texto:
    if letra.isalpha():
        letra = letra.lower()  # Convertir la letra a minúscula
        if letra in apariciones:
            apariciones[letra] += 1
        else:
            apariciones[letra] = 1

# Convertir el diccionario en una lista de tuplas (letra, apariciones)
lista_apariciones = [(letra, contador) for letra, contador in apariciones.items()]

# Ordenar la lista por apariciones en orden descendente
lista_apariciones.sort(key=lambda x: x[1], reverse=True)

# Imprimir las apariciones de cada letra
for letra, contador in lista_apariciones:
    print(f'{letra}: {contador}')
