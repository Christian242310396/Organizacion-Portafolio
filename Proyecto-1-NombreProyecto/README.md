
# Proyecto 1
Descripcion Del Problema
Esta plataforma opera como un núcleo central de gestión de datos distribuido en dos etapas funcionales bien definidas: Módulo de Inyección de Datos (Python) Consiste en un script de automatización estructurado para la creación e inserción masiva de registros simulados bajo un estándar homogéneo y controlado.Entorno de Consulta Web (PHP, HTML5 y CSS3)Una interfaz dinámica que ejecuta tareas de búsqueda y filtrado secuencial en tiempo real, aislando y extrayendo de forma precisa los elementos almacenados a partir de los criterios o palabras clave que ingrese el usuario.
---

## 2. Arquitectura de Archivos y Flujo de Datos
El sistema implementa una distribución modular rígida, concentrando la lógica operativa y las vistas dentro de la carpeta `src/`. El ciclo de vida de los datos se ejecuta a través del siguiente orden secuencial:

1. **`src/generacion.py`**: Script automatizado encargado de la construcción e inserción masiva de registros simulados en el almacén de datos.
2. **`src/maestro.txt`**: Base de datos plana principal que aloja el histórico completo de inventario separado por caracteres de control (`|`).
3. **`src/formulario.html`**: Front-end interactivo que captura los criterios de búsqueda enviados por el usuario mediante peticiones HTTP `POST`.
4. **`src/procesar.php`**: Controladora backend que ejecuta el ciclo de lectura lineal para localizar coincidencias directas.
5. **`src/filtrado.txt`**: Repositorio temporal que almacena de manera exclusiva las filas resultantes de la última consulta.
6. **`src/visualizar.php`**: Módulo de presentación que analiza sintácticamente el archivo temporal para desplegar los datos en una malla web estructurada con los estilos de **`src/estilos.css`**.

---

## 3. Sustentación Técnica de Formatos y Modos de Acceso

### Persistencia en Archivos Planos con Delimitadores (`maestro.txt` y `filtrado.txt`)
* **Criterio de Selección:** Se optó por el uso de archivos de texto plano bajo codificación estándar `UTF-8` empleando tuberías (`|`) como separadores de campos debido a su bajísimo sobrecosto de almacenamiento (*overhead*). Al descartar metadatos redundantes y etiquetas repetitivas por cada registro, se maximiza la eficiencia de almacenamiento de cada elemento guardado.
* **Estrategias de Acceso:** * En el entorno de Python se implementa el modo de apertura `w` (`open(ARCHIVO_MAESTRO, "w")`), garantizando un vaciado e inicialización limpia del inventario masivo de pruebas.
  * En el entorno de PHP se aprovechan las rutinas internas `file()` y `file_put_contents()`, las cuales transfieren las líneas a vectores de memoria indexados para agilizar los ciclos iterativos de lectura y escritura secuencial.

### Arquitectura y Desacoplamiento Web
* **Hojas de Estilo Centralizadas (`estilos.css`):** El diseño visual se mantiene aislado de los archivos funcionales para respetar la modularidad de la arquitectura de software. Al evitar la inyección de estilos embebidos (*hardcoded*) dentro del marcado lógico de PHP, se asegura la mantenibilidad y un crecimiento escalable del front-end.

---

## 4. Aseguramiento de Código Limpio y Control de Excepciones
Todas las operaciones de manipulación del sistema de archivos están blindadas mediante el uso de manejadores de contexto nativos con cierre automatizado de punteros (`with open` en Python) y condicionales lógicos de verificación de entorno (`file_exists` en PHP). Esto previene fugas de memoria y caídas críticas ante fallos de concurrencia o archivos ausentes en tiempo de ejecución.
