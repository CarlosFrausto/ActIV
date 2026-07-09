import csv
import os

CARPETA = "datos"


def crear_directorio():
    """
    Crea la carpeta datos si no existe.
    """
    if not os.path.exists(CARPETA):
        os.makedirs(CARPETA)


def cargar(nombre_archivo):
    """
    Carga un archivo CSV y devuelve una lista de diccionarios.
    Si el archivo no existe, devuelve una lista vacía.
    """

    crear_directorio()

    if not os.path.exists(nombre_archivo):
        return []

    with open(
        nombre_archivo,
        mode="r",
        encoding="utf-8",
        newline=""
    ) as archivo:

        lector = csv.DictReader(archivo)

        return list(lector)


def guardar(nombre_archivo, datos, encabezados):
    """
    Guarda una lista de diccionarios en un archivo CSV.
    """

    crear_directorio()

    with open(
        nombre_archivo,
        mode="w",
        encoding="utf-8",
        newline=""
    ) as archivo:

        escritor = csv.DictWriter(
            archivo,
            fieldnames=encabezados
        )

        escritor.writeheader()

        for fila in datos:
            escritor.writerow(fila)
