# Ordenador de Bloques de Números en un Arreglo

## Descripción

Este proyecto implementa una solución en Python para procesar un arreglo (lista o tupla) que contiene bloques de números. Los bloques pueden ser de cualquier longitud, y los números contenidos están en el rango de 1 a 9. Los bloques se separan por un cero (0).

El programa ordena los números dentro de cada bloque individualmente de menor a mayor e imprime las secuencias resultantes, separando los bloques por un espacio.

## Características Principales

* Procesa arreglos con un número variable de bloques.
* Maneja bloques de longitud variable.
* Los números dentro de los bloques están en el rango de 1 a 9.
* Un cero (0) marca el final de un bloque y el inicio de otro.
* El inicio y el final del arreglo se consideran límites de bloque.
* Un bloque puede no contener elementos (por ejemplo, debido a ceros consecutivos o un cero al inicio/final del arreglo). En tal caso, se representa con una "X".

## Requisitos

* Python 3.x

## Estructura de Archivos

El proyecto consta de los siguientes archivos:

* `procesador_bloques.py`: Contiene la lógica principal para el procesamiento y ordenamiento de los bloques.
    * `ordenar_bloques_arreglo(myArray)`: La función principal que toma el arreglo y devuelve la cadena formateada.
    * `procesar(bloque_actual)`: Una función auxiliar que formatea un bloque individual (ya ordenado o vacío) a su representación en cadena ("X" o los números unidos).
* `test_bloques.py`: Contiene las pruebas unitarias para verificar el correcto funcionamiento de `procesador_bloques.py`.
* `README.md`: Este archivo de documentación.

## Cómo Usar el Código Principal

La función `ordenar_bloques_arreglo` está diseñada para ser importada y utilizada en otros scripts de Python.

1.  Asegúrate de tener el archivo `procesador_bloques.py` en tu directorio de trabajo o en una ruta accesible por Python.
2.  En tu script de Python, importa la función:
    ```python
    from procesador_bloques import ordenar_bloques_arreglo
    ```
3.  Llama a la función con tu arreglo de entrada:
    ```python
    mi_arreglo = (1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1)
    resultado = ordenar_bloques_arreglo(mi_arreglo)
    print(resultado)
    # Salida esperada: 123 1378 167

    otro_arreglo = (2, 1, 0, 0, 3, 4)
    resultado_otro = ordenar_bloques_arreglo(otro_arreglo)
    print(resultado_otro)
    # Salida esperada: 12 X 34
    ```

Si deseas ejecutar un ejemplo directamente desde `procesador_bloques.py`, puedes añadir un bloque de ejecución al final de dicho archivo:
```python
# Al final de procesador_bloques.py (opcional, para pruebas rápidas)
if __name__ == '__main__':
    ejemplo_arr_1 = (1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1)
    print(f"Entrada: {ejemplo_arr_1}")
    print(f"Salida: {ordenar_bloques_arreglo(ejemplo_arr_1)}")

    ejemplo_arr_2 = (2, 1, 0, 0, 3, 4)
    print(f"Entrada: {ejemplo_arr_2}")
    print(f"Salida: {ordenar_bloques_arreglo(ejemplo_arr_2)}")
```

## Cómo Ejecutar las Pruebas Unitarias
Las pruebas unitarias se encuentran en test_bloques.py y utilizan el módulo unittest de Python. Para ejecutarlas:

1.  Abre una terminal o línea de comandos.

2.  Navega al directorio donde se encuentran los archivos procesador_bloques.py y test_bloques.py.

3.  Ejecuta el siguiente comando:
```
python -m unittest test_bloques.py
```
Si todas las pruebas pasan, verás un mensaje indicando "OK". Si alguna falla, se mostrarán los detalles del error.