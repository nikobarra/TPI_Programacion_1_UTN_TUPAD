import os
from config import *

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")

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

def imprimir_titulo(texto):
    """Muestra un título decorado en magenta"""
    print(f"\n{MAGENTA}{NEGRITA}{'═' * 50}")
    print(f"{texto.center(50)}")
    print(f"{'═' * 50}{RESET}")

def imprimir_menu():
    """Muestra el menú principal con bordes decorativos"""
    print(f"{AZUL}{NEGRITA}╔══════════════════════════════════════════════╗")
    print(f"║         🌍  {BLANCO}GESTIÓN DE PAÍSES{AZUL}  🌍           ║")
    print(f"╠══════════════════════════════════════════════╣")
    print(f"║  {AMARILLO}[1]{AZUL}  Agregar país                           ║")
    print(f"║  {AMARILLO}[2]{AZUL}  Actualizar datos de un país            ║")
    print(f"║  {AMARILLO}[3]{AZUL}  Buscar país por nombre                 ║")
    print(f"║  {AMARILLO}[4]{AZUL}  Filtrar países                         ║")
    print(f"║  {AMARILLO}[5]{AZUL}  Ordenar países                         ║")
    print(f"║  {AMARILLO}[6]{AZUL}  Ver estadísticas                       ║")
    print(f"║  {AMARILLO}[7]{AZUL}  Mostrar todos los países               ║")
    print(f"║  {AMARILLO}[0]{AZUL}  Salir                                  ║")
    print(f"╚══════════════════════════════════════════════╝{RESET}")

def mostrar_tabla_paises(paises):
    """Muestra todos los países en una tabla formateada"""
    if not paises:
        imprimir_cuadro_advertencia("No hay países para mostrar.")
        return

    # Encabezado de la tabla
    header = f"{NEGRITA}{AZUL}{'NOMBRE':<20} {'POBLACIÓN':<15} {'SUPERFICIE (km2)':<20} {'CONTINENTE':<15}{RESET}"
    print("\n" + header)
    print("─" * 70)

    for p in paises:
        print(
            f"{p['nombre']:<20} {p['poblacion']:<15,} {p['superficie']:<20,} {p['continente']:<15}"
        )
    print("─" * 70)
