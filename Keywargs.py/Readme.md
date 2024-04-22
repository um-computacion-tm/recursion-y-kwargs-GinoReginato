# Búsqueda de Datos en una Base de Datos

Este código implementa una función llamada `buscar_datos(*args, **kwargs)` en Python que realiza una búsqueda de datos en una base de datos proporcionada como argumento. La función acepta una lista de argumentos posicionales `args` que representan los datos que se desean buscar, y un argumento de palabra clave `database` que representa la base de datos en la que se realizará la búsqueda.

La función itera sobre cada uno de los datos proporcionados en `args` y verifica si están presentes en la base de datos. Si un dato está presente en la base de datos, se agrega a una lista llamada `datos_encontrados`. Si un dato no está presente en la base de datos, se imprime un mensaje indicando que no se encontró el dato.

Al finalizar la búsqueda, se imprime una lista de los datos encontrados en la base de datos.
