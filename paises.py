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


def mostrar_todos(paises):
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


def agregar_pais(paises):
    """Permite al usuario ingresar un nuevo país con validaciones"""
    imprimir_titulo("AGREGAR NUEVO PAÍS")

    nombre = input(f"{BLANCO}Nombre del país: {RESET}").strip().title()

    # Validación de duplicados
    for p in paises:
        if p["nombre"] == nombre:
            imprimir_cuadro_error("Este país ya existe en la lista.")
            return

    if nombre == "":
        imprimir_cuadro_error("El nombre no puede estar vacío.")
        return

    try:
        poblacion = int(input(f"{BLANCO}Población (habitantes): {RESET}"))
        superficie = int(input(f"{BLANCO}Superficie (km²): {RESET}"))
        if poblacion <= 0 or superficie <= 0:
            imprimir_cuadro_error(
                "La población y superficie deben ser números positivos."
            )
            return
    except ValueError:
        imprimir_cuadro_error(
            "Debe ingresar números enteros para población y superficie."
        )
        return

    continente = input(f"{BLANCO}Continente: {RESET}").strip().title()
    if continente == "":
        imprimir_cuadro_error("El continente no puede estar vacío.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(nuevo_pais)

    if guardar_csv("paises.csv", paises):
        imprimir_cuadro_exito(f"¡País '{nombre}' agregado y guardado con éxito!")
    else:
        imprimir_cuadro_advertencia(
            "El país se agregó en memoria pero hubo un error al guardar el archivo."
        )


def actualizar_pais(paises):
    """Busca un país por nombre y permite editar población y superficie"""
    if not paises:
        imprimir_cuadro_advertencia("La lista está vacía.")
        return

    imprimir_titulo("ACTUALIZAR DATOS")
    buscar = (
        input(f"{BLANCO}Ingrese el nombre exacto del país a actualizar: {RESET}")
        .strip()
        .title()
    )

    encontrado = None
    for p in paises:
        if p["nombre"] == buscar:
            encontrado = p
            break

    if encontrado:
        print(f"\n{CIAN}Datos actuales de {encontrado['nombre']}:{RESET}")
        print(f"- Población: {encontrado['poblacion']:,}")
        print(f"- Superficie: {encontrado['superficie']:,}")

        try:
            nueva_pob = int(input(f"\n{BLANCO}Nueva población: {RESET}"))
            nueva_sup = int(input(f"{BLANCO}Nueva superficie: {RESET}"))

            if nueva_pob > 0 and nueva_sup > 0:
                encontrado["poblacion"] = nueva_pob
                encontrado["superficie"] = nueva_sup

                if guardar_csv("paises.csv", paises):
                    imprimir_cuadro_exito(
                        "Datos actualizados y guardados correctamente."
                    )
                else:
                    imprimir_cuadro_advertencia(
                        "Datos actualizados en memoria, pero error al guardar en archivo."
                    )
            else:
                imprimir_cuadro_error("Los valores deben ser mayores a cero.")
        except ValueError:
            imprimir_cuadro_error("Ingreso inválido. No se realizaron cambios.")
    else:
        imprimir_cuadro_error("País no encontrado.")


def buscar_pais(paises):
    pass


def filtrar_paises(paises):
    pass


def ordenar_paises(paises):
    pass


def mostrar_estadisticas(paises):
    pass


def main():
    limpiar_pantalla()
    imprimir_titulo("BIENVENIDO AL SISTEMA DE GESTIÓN MUNDIAL")

    lista_paises = cargar_csv("paises.csv")

    if not lista_paises:
        input(
            f"\n{AMARILLO}Presione Enter para continuar con el programa vacío...{RESET}"
        )

    while True:
        limpiar_pantalla()
        imprimir_menu()

        opcion = input(f"\n{AMARILLO}Seleccione una opción (0-7): {RESET}")

        if opcion == "1":
            agregar_pais(lista_paises)
        elif opcion == "2":
            actualizar_pais(lista_paises)
        elif opcion == "3":
            buscar_pais(lista_paises)
        elif opcion == "4":
            filtrar_paises(lista_paises)
        elif opcion == "5":
            ordenar_paises(lista_paises)
        elif opcion == "6":
            mostrar_estadisticas(lista_paises)
        elif opcion == "7":
            imprimir_titulo("LISTADO COMPLETO DE PAÍSES")
            mostrar_todos(lista_paises)
        elif opcion == "0":
            imprimir_cuadro_info("Gracias por utilizar el sistema. ¡Hasta pronto!")
            sys.exit()
        else:
            imprimir_cuadro_advertencia("Opción no válida. Intente nuevamente.")

        input(f"\n{BLANCO}Presione Enter para volver al menú...{RESET}")


if __name__ == "__main__":
    main()
