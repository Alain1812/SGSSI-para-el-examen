#!/bin/bash

# Ruta a la carpeta
carpeta="/ruta/a/la/carpeta"

# Hash proporcionado como argumento
hash_proporcionado="$1"

# Recorre todos los archivos en la carpeta
for archivo in "$carpeta"/*
do
    if [[ -f "$archivo" ]]; then
        # Calcula el hash del archivo
        hash_archivo=$(md5sum "$archivo" | cut -d ' ' -f 1)

        # Compara el hash con el proporcionado
        if [[ "$hash_archivo" == "$hash_proporcionado" ]]; then
            echo "El hash coincide para el archivo: $archivo"
            exit 0
        fi
    fi
done

echo "No se encontró ningún archivo con el hash proporcionado."
exit 1
