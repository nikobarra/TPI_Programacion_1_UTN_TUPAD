import sys
from config import AMARILLO, BLANCO, RESET
from ui import limpiar_pantalla, imprimir_titulo, imprimir_menu, imprimir_cuadro_info, imprimir_cuadro_advertencia, mostrar_tabla_paises
from archivos import cargar_csv
from acciones import (
    agregar_pais, 
    actualizar_pais, 
    buscar_pais, 
    filtrar_paises, 
    ordenar_paises, 
    mostrar_estadisticas
)

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
            mostrar_tabla_paises(lista_paises)
        elif opcion == "0":
            imprimir_cuadro_info("Gracias por utilizar el sistema. ¡Hasta pronto!")
            sys.exit()
        else:
            imprimir_cuadro_advertencia("Opción no válida. Intente nuevamente.")

        input(f"\n{BLANCO}Presione Enter para volver al menú...{RESET}")

if __name__ == "__main__":
    main()
