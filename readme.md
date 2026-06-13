# Trabajo Práctico Integrador: Gestión de Países 🌍

## Enlace a Youtube

[link] https://www.youtube.com/watch?v=ZYIG-8ayQik

Este proyecto es una aplicación de consola desarrollada en Python 3 para la gestión de datos de países. Ha sido diseñado siguiendo los requerimientos de un Trabajo Práctico de primer cuatrimestre de programación, priorizando la simplicidad, la modularidad y una interfaz visual atractiva mediante el uso de códigos ANSI.

## 📋 Descripción

La aplicación permite administrar una lista de países cargada inicialmente desde un archivo CSV. Todas las operaciones se realizan en memoria para garantizar rapidez, sin necesidad de bases de datos externas.

### Modalidad de trabajo

El equipo opto luego de una pequeña investigacion por abordar el proyecto bajo la modalidad pair programming, lo que nos permitió colaborar estrechamente en el diseño y desarrollo del código, asegurando una mayor calidad y coherencia en la implementación, ademas de fomentar el aprendizaje mutuo y la resolución conjunta de problemas.
Este metodo consiste en que ambos integrantes del equipo trabajan juntos en la misma computadora, compartiendo el teclado y la pantalla, lo que facilita la comunicación y la toma de decisiones en tiempo real, en este caso trabajamos de forma remota compartiendo pantalla a través de una videollamada, lo que nos permitió mantener una colaboración efectiva a pesar de la distancia física.

### Funcionalidades principales:

- **Carga inicial:** Lectura automática de `paises.csv` al arrancar.
- **Gestión:** Agregar nuevos países y actualizar datos de población y superficie de los existentes.
- **Búsqueda y Filtrado:** Búsqueda por nombre (parcial o exacta) y filtros por continente, rango de población o superficie.
- **Ordenamiento:** Clasificación de la lista por diferentes criterios (A-Z, población, superficie) usando algoritmos manuales.
- **Estadísticas:** Cálculo de máximos, mínimos, promedios y distribución por continente.
- **Visualización:** Listado completo formateado en tablas de consola.

## 🚀 Requisitos y Ejecución

### Requisitos

- **Python 3.x** instalado.
- No requiere la instalación de librerías externas (solo utiliza la biblioteca estándar de Python: `os`, `csv`, `sys`).

### Instalación y Ejecución

1.  Asegúrese de tener todos los archivos `.py` y `paises.csv` en la misma carpeta.
2.  Abra una terminal o consola en dicha carpeta.
3.  Ejecute el programa con el siguiente comando:
    ```bash
    python main.py
    ```

## 🛠️ Estructura del Proyecto (Arquitectura Modular)

El proyecto ha sido modularizado para seguir buenas prácticas de programación, separando las responsabilidades en distintos archivos:

- **`main.py`**: El punto de entrada del programa. Contiene el bucle principal y la gestión del menú.
- **`config.py`**: Contiene las constantes de configuración, principalmente los códigos de colores ANSI.
- **`ui.py`**: Se encarga de la interfaz de usuario: limpieza de pantalla, impresión de cuadros decorativos, títulos y tablas.
- **`archivos.py`**: Gestiona la persistencia de datos (lectura y escritura del archivo CSV).
- **`acciones.py`**: Contiene la lógica de negocio interactiva (agregar, actualizar, buscar, filtrar, ordenar y estadísticas).

## 🛠️ Estructura de Datos

Cada país se representa internamente como un diccionario con la siguiente estructura:

```python
{
    "nombre": str,
    "poblacion": int,
    "superficie": int,
    "continente": str
}
```

## 🎨 Aspectos Visuales

El programa utiliza códigos de escape ANSI para ofrecer una experiencia de usuario más intuitiva y agradable, incluyendo:

- **Títulos resaltados** en magenta y negrita.
- **Cuadros de diálogo:**
    - 🟢 Verde para éxitos.
    - 🔴 Rojo para errores de validación.
    - 🟡 Amarillo para advertencias.
    - 🔵 Cian para información neutral.
- **Menú interactivo** con bordes decorativos.

## 📂 Archivos del Proyecto

- **`main.py`**: Punto de entrada.
- **`config.py`**: Configuración y constantes.
- **`ui.py`**: Interfaz y visualización.
- **`archivos.py`**: Manejo de CSV.
- **`acciones.py`**: Lógica de gestión de países.
- `paises.csv`: Archivo de datos de ejemplo.
- `README.md`: Documentación del proyecto.

---

**Nota:** Este proyecto fue desarrollado con fines educativos para la materia Programación 1.
