import os
import mutagen
from mutagen.mp3 import MP3

def obtener_canciones(carpeta):
    canciones = {}
    
    # Iterar sobre los archivos en la carpeta especificada
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.mp3'):
            try:
                # Extraer el número de ID y el nombre de la canción del nombre del archivo
                partes = archivo.split('_', 1)
                id_cancion = partes[0]
                nombre_cancion = partes[1].rsplit('.', 1)[0]

                # Obtener la duración de la canción usando mutagen
                ruta_archivo = os.path.join(carpeta, archivo)
                audio = MP3(ruta_archivo)
                duracion = audio.info.length

                # Añadir la información al diccionario
                canciones[id_cancion] = {
                    'id': id_cancion,
                    'nombre': nombre_cancion,
                    'duracion': round(duracion, 2)  # Duración en segundos, redondeada a 2 decimales
                }

            except Exception as e:
                print(f'Error procesando {archivo}: {e}')

    return canciones

audios = {}

import os
for subdir, dirs, files in os.walk("archivos_de_audio"):
    if '\\' in subdir: 
        carpeta = subdir[subdir.find('\\')+1:].split('_', 1)
        print(subdir)
        audios[carpeta[1]] = {'id': int(carpeta[0]), 'canciones':[]}
        for file in files:
            partes = file.split('_', 1)
            id_cancion = partes[0]
            nombre_cancion = partes[1].rsplit('.', 1)[0]
            ruta_archivo = os.path.join(subdir, file)
            audio = MP3(ruta_archivo)
            duracion = audio.info.length
            audios[carpeta[1]]['canciones'].append({'id':int(id_cancion), 'nombre':nombre_cancion, 'duracion': round(duracion, 2)})

print(audios)
import json
with open('audios.json', 'w') as fp:
    json.dump(audios, fp, indent=4)