import argparse

# Crear un analizador de argumentos
parser = argparse.ArgumentParser(description='Reemplazar una letra por otra en un archivo de texto')
parser.add_argument('archivo', help='Nombre del archivo de texto')
parser.add_argument('letra_a_cambiar', help='Letra a cambiar')
parser.add_argument('letra_a_reemplazar', help='Letra a reemplazar')
args = parser.parse_args()

# Leer el contenido actual del archivo de texto
try:
    with open(args.archivo, 'r') as archivo:
        texto = archivo.read()
except FileNotFoundError:
    print(f"El archivo '{args.archivo}' no fue encontrado.")
    exit()

# Realizar el reemplazo de la letra
texto_modificado = texto.replace(args.letra_a_cambiar, args.letra_a_reemplazar)

# Escribir el texto modificado de nuevo en el archivo
with open(args.archivo, 'w') as archivo:
    archivo.write(texto_modificado)

print(f'Se ha cambiado la letra "{args.letra_a_cambiar}" por "{args.letra_a_reemplazar}" en el archivo "{args.archivo}".')
