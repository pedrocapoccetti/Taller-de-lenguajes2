import csv
import os

def mostrar_primeras_filas(path, delimiter="\t", n=10):
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        for i, row in enumerate(reader):
            if i < n:
                print(f"Fila {i+1}: {row}")
            else:
                break


def contar_filas(path, delimiter="\t"):
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        total = sum(1 for _ in reader)
    print(f"Total de registros: {total - 1}")  # -1 para no contar el encabezado

def contar_columnas(path, delimiter="\t"):
    with open(path, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delimiter)
        encabezado = next(reader)
    print(f"Total de columnas: {len(encabezado)}")

# Definir la carpeta base relativa al archivo .py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# IADIZA
print("="*50)
print("IADIZA")
print("="*50)
iadiza_path = os.path.join(BASE_DIR, "raw_datasets", "Iadiza", "occurrence.iadiza.txt")
mostrar_primeras_filas(iadiza_path, delimiter="\t")
contar_filas(iadiza_path, delimiter=",")
contar_columnas(iadiza_path, delimiter="\t")

# iNaturalist
print("="*50)
print("INATURALIST")
print("="*50)
inaturalist_path = os.path.join(BASE_DIR, "raw_datasets", "Inaturalist", "observations.inaturalist.csv")
mostrar_primeras_filas(inaturalist_path, delimiter=",")
contar_filas(inaturalist_path, delimiter=",")
contar_columnas(inaturalist_path, delimiter=",")

# Xeno-canto
print("="*50)
print("XENO-CANTO")
print("="*50)
xenocanto_path = os.path.join(BASE_DIR, "raw_datasets", "xenocanto", "occurrence.xeno-canto.txt")
mostrar_primeras_filas(xenocanto_path, delimiter="\t")
contar_filas(xenocanto_path, delimiter="\t")
contar_columnas(xenocanto_path, delimiter="\t")
