import os
import csv
from ui import imprimir_cuadro_error, imprimir_cuadro_exito, imprimir_cuadro_advertencia

def cargar_csv(nombre_archivo):
    """Carga los datos del CSV a una lista de diccionarios"""
    lista_paises = []
    if not os.path.exists(nombre_archivo):
        imprimir_cuadro_advertencia(
            f"El archivo {nombre_archivo} no existe. Iniciando lista vacía."
        )
        return lista_paises

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                try:
                    # Validamos que los datos numéricos sean correctos
                    pais = {
                        "nombre": fila["nombre"].strip().title(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip().title(),
                    }
                    if pais["poblacion"] > 0 and pais["superficie"] > 0:
                        lista_paises.append(pais)
                except (ValueError, KeyError):
                    continue  # Si hay error en una fila, la salteamos

        if lista_paises:
            imprimir_cuadro_exito(
                f"Se cargaron {len(lista_paises)} países correctamente."
            )
        else:
            imprimir_cuadro_advertencia(
                "El archivo CSV estaba vacío o no tenía datos válidos."
            )
    except Exception as e:
        imprimir_cuadro_error(f"Error al leer el archivo: {e}")

    return lista_paises

def guardar_csv(nombre_archivo, lista_paises):
    """Guarda la lista de países completa en el archivo CSV"""
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            for pais in lista_paises:
                escritor.writerow(pais)
        return True
    except Exception as e:
        imprimir_cuadro_error(f"No se pudo guardar en el archivo: {e}")
        return False
