import os
import csv
import sys

# Constantes de colores ANSI para la interfaz
ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIAN = "\033[96m"
BLANCO = "\033[97m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_cuadro_error(mensaje):
    """Muestra un mensaje de error en un cuadro rojo"""
    linea = "═" * (len(mensaje) + 6)
    print(f"\n{ROJO}╔{linea}╗")
    print(f"║   ❌ {mensaje}   ║")
    print(f"╚{linea}╝{RESET}")

def imprimir_cuadro_exito(mensaje):
    """Muestra un mensaje de éxito en un cuadro verde"""
    linea = "═" * (len(mensaje) + 6)
    print(f"\n{VERDE}╔{linea}╗")
    print(f"║   ✓  {mensaje}   ║")
    print(f"╚{linea}╝{RESET}")

def imprimir_cuadro_info(mensaje):
    """Muestra un mensaje informativo en un cuadro cian"""
    linea = "═" * (len(mensaje) + 6)
    print(f"\n{CIAN}╔{linea}╗")
    print(f"║   ℹ  {mensaje}   ║")
    print(f"╚{linea}╝{RESET}")

def imprimir_cuadro_advertencia(mensaje):
    """Muestra un mensaje de advertencia en un cuadro amarillo"""
    linea = "═" * (len(mensaje) + 6)
    print(f"\n{AMARILLO}╔{linea}╗")
    print(f"║   ⚠  {mensaje}   ║")
    print(f"╚{linea}╝{RESET}")