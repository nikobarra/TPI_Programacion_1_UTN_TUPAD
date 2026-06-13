from config import *
from ui import (
    imprimir_titulo, 
    imprimir_cuadro_error, 
    imprimir_cuadro_exito, 
    imprimir_cuadro_info, 
    imprimir_cuadro_advertencia, 
    mostrar_tabla_paises
)
from archivos import guardar_csv

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
    """Busca países que contengan el texto ingresado"""
    if not paises:
        imprimir_cuadro_advertencia("No hay países cargados.")
        return

    imprimir_titulo("BUSCAR PAÍS")
    termino = (
        input(f"{BLANCO}Ingrese parte del nombre a buscar: {RESET}").strip().title()
    )

    resultados = []
    for p in paises:
        if termino in p["nombre"]:
            resultados.append(p)

    if resultados:
        imprimir_cuadro_info(f"Se encontraron {len(resultados)} coincidencias:")
        mostrar_tabla_paises(resultados)
    else:
        imprimir_cuadro_advertencia("No se encontraron países con ese nombre.")

def filtrar_paises(paises):
    """Submenú para aplicar distintos filtros a la lista"""
    if not paises:
        imprimir_cuadro_advertencia("No hay países para filtrar.")
        return

    imprimir_titulo("FILTRAR PAÍSES")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    print("0. Volver")

    opcion = input(f"\n{AMARILLO}Seleccione una opción: {RESET}")

    resultados = []
    if opcion == "1":
        continentes = []
        for p in paises:
            if p["continente"] not in continentes:
                continentes.append(p["continente"])

        print(f"\nContinentes disponibles: {', '.join(continentes)}")
        elegido = input(f"{BLANCO}Escriba el continente: {RESET}").strip().title()

        for p in paises:
            if p["continente"] == elegido:
                resultados.append(p)

    elif opcion == "2":
        try:
            min_pob = int(input(f"{BLANCO}Población mínima: {RESET}"))
            max_pob = int(input(f"{BLANCO}Población máxima: {RESET}"))
            for p in paises:
                if min_pob <= p["poblacion"] <= max_pob:
                    resultados.append(p)
        except ValueError:
            imprimir_cuadro_error("Debe ingresar números válidos.")
            return

    elif opcion == "3":
        try:
            min_sup = int(input(f"{BLANCO}Superficie mínima: {RESET}"))
            max_sup = int(input(f"{BLANCO}Superficie máxima: {RESET}"))
            for p in paises:
                if min_sup <= p["superficie"] <= max_sup:
                    resultados.append(p)
        except ValueError:
            imprimir_cuadro_error("Debe ingresar números válidos.")
            return
    elif opcion == "0":
        return
    else:
        imprimir_cuadro_advertencia("Opción no válida.")
        return

    if resultados:
        mostrar_tabla_paises(resultados)
    else:
        imprimir_cuadro_advertencia("Ningún país coincide con el filtro.")

def ordenar_paises(paises):
    """Ordena una copia de la lista mediante el algoritmo Bubble Sort (Método burbuja)"""
    if not paises:
        imprimir_cuadro_advertencia("No hay países para ordenar.")
        return

    copia = []
    for p in paises:
        copia.append(p.copy())

    imprimir_titulo("ORDENAR PAÍSES")
    print("1. Por nombre (A-Z)")
    print("2. Por población (Mayor a Menor)")
    print("3. Por superficie (Elegir Ascendente/Descendente)")

    opcion = input(f"\n{AMARILLO}Seleccione criterio: {RESET}")

    sentido = "2"
    if opcion == "3":
        print("\nSentido del ordenamiento:")
        print("1. Menor a Mayor (Ascendente)")
        print("2. Mayor a Menor (Descendente)")
        sentido = input(f"{AMARILLO}Seleccione sentido: {RESET}")

    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            intercambiar = False

            if opcion == "1":
                if copia[j]["nombre"] > copia[j + 1]["nombre"]:
                    intercambiar = True
            elif opcion == "2":
                if copia[j]["poblacion"] < copia[j + 1]["poblacion"]:
                    intercambiar = True
            elif opcion == "3":
                if sentido == "1":
                    if copia[j]["superficie"] > copia[j + 1]["superficie"]:
                        intercambiar = True
                else:
                    if copia[j]["superficie"] < copia[j + 1]["superficie"]:
                        intercambiar = True

            if intercambiar:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]

    if opcion in ["1", "2", "3"]:
        imprimir_cuadro_info(
            "Lista ordenada (estos cambios no afectan la base de datos principal)"
        )
        mostrar_tabla_paises(copia)
    else:
        imprimir_cuadro_advertencia("Opción de ordenado no válida.")

def mostrar_estadisticas(paises):
    """Calcula y muestra estadísticas básicas de los países cargados"""
    if not paises:
        imprimir_cuadro_advertencia("No hay datos para generar estadísticas.")
        return

    imprimir_titulo("ESTADÍSTICAS GENERALES")

    p_mayor_pob = paises[0]
    p_menor_pob = paises[0]
    suma_pob = 0
    suma_sup = 0
    conteo_continentes = {}

    for p in paises:
        if p["poblacion"] > p_mayor_pob["poblacion"]:
            p_mayor_pob = p
        if p["poblacion"] < p_menor_pob["poblacion"]:
            p_menor_pob = p

        suma_pob += p["poblacion"]
        suma_sup += p["superficie"]

        cont = p["continente"]
        if cont in conteo_continentes:
            conteo_continentes[cont] += 1
        else:
            conteo_continentes[cont] = 1

    prom_pob = suma_pob / len(paises)
    prom_sup = suma_sup / len(paises)

    print(f"\n{NEGRITA}📊 RESUMEN NUMÉRICO:{RESET}")
    print(
        f"{CIAN}• País con más población: {RESET}{p_mayor_pob['nombre']} ({p_mayor_pob['poblacion']:,} hab.)"
    )
    print(
        f"{CIAN}• País con menos población: {RESET}{p_menor_pob['nombre']} ({p_menor_pob['poblacion']:,} hab.)"
    )
    print(f"{CIAN}• Promedio de población: {RESET}{prom_pob:,.2f} hab.")
    print(f"{CIAN}• Promedio de superficie: {RESET}{prom_sup:,.2f} km²")

    print(f"\n{NEGRITA}🌍 PAÍSES POR CONTINENTE:{RESET}")
    for cont, cant in conteo_continentes.items():
        print(f" - {cont:<15}: {cant} países")
