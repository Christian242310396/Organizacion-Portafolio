# 🏭 Proyecto 2: Gateway Security - Motor de Autenticación y Monitor de Auditoría para Planta

## 1. Descripción del Sistema
Este entorno de software funciona como un sistema de control perimetral diseñado para administrar y validar el acceso del personal en las instalaciones de una planta industrial. La solución se distribuye en dos componentes operativos: un núcleo local de validación programado en **Python** que simula un lector de terminales físicas, y una consola web de supervisión en tiempo real desarrollada con **PHP, HTML5 y CSS3**. El software procesa cada petición de entrada, verifica las credenciales operativas del usuario y escribe registros inmutables de auditoría para mitigar brechas de seguridad.

---

## 2. Arquitectura de Archivos y Flujo de Datos
El proyecto adopta un diseño modular estricto, aislando los recursos del motor y la interfaz gráfica dentro del directorio `src/`. El ciclo de procesamiento de la información sigue el siguiente orden secuencial:

1. **`src/usuarios.json`**: Repositorio de datos estructurado que centraliza los tokens de tarjetas, identidades del personal, áreas de trabajo y rangos de permisos.
2. **`src/control.py`**: Script backend (Python) encargado de gobernar el lector de accesos. Carga el esquema JSON, itera sobre las lecturas y despacha las autorizaciones.
3. **`src/auditoria.txt`**: Almacén plano de persistencia incremental que actúa como un libro de actas inalterable para los eventos del sistema.
4. **`src/index.php`**: Panel de control web que interpreta y renderiza los renglones de la bitácora, inyectando alertas visuales automáticas cuando se detectan infracciones.
5. **`src/style.css`**: Hoja de estilos encargada de la maquetación responsiva, la consistencia tipográfica y la codificación cromática de los estados de seguridad.

---

## 3. Sustentación Técnica de Formatos y Modos de Acceso

### Estructura de Datos en Formato Organizado (`usuarios.json`)
* **Criterio de Selección:** Se implementó el estándar **JSON (JavaScript Object Notation)** para el catálogo de usuarios autorizados debido a su capacidad innata de jerarquizar datos mediante colecciones de pares clave-valor. Esto permite moldear atributos complejos de los empleados (como subobjetos de departamentos y privilegios) omitiendo la sobrecarga analítica de un sistema gestor de bases de datos relacionales, lo que garantiza portabilidad y una sintaxis unificada para Python y PHP.
* **Estrategias de Acceso:** En el script de Python se invoca el modo de lectura exclusiva `r` (`open("usuarios.json", "r")`), volcando el contenido directamente en la memoria caché mediante `json.load()` para agilizar los ciclos lógicos de emparejamiento.

### Registro de Eventos Secuenciales (`auditoria.txt`)
* **Criterio de Selección:** Se seleccionó un archivo de texto plano para el histórico de accesos debido a que las operaciones de auditoría demandan un registro estrictamente cronológico adjuntando estampas de tiempo exactas por cada suceso.
* **Estrategias de Acceso:** * En la capa de Python se utiliza el modificador de apertura `a` (`open("auditoria.txt", "a")`), una técnica esencial en el manejo de flujos de datos que posiciona de forma automática el puntero al término del documento, asegurando que las nuevas transacciones se concatenen limpiamente sin comprometer los registros históricos previos.
  * En la capa de PHP se aplica el modo de lectura lineal continua `r` (`fopen("auditoria.txt", "r")`) en conjunto con un bucle iterativo controlado por `fgets()`, extrayendo las cadenas línea por línea para mitigar la saturación de memoria en el servidor al renderizar archivos masivos.

---

## 4. Desacoplamiento de Datos Dinámicos (Anti-Hardcoded)
Con el objetivo de garantizar la escalabilidad y adherirse a los principios de código limpio, el sistema prescinde por completo de almacenar identificadores de tarjetas o registros personales de forma estática (*hardcoded*) en los scripts funcionales. Toda validación de acceso se resuelve dinámicamente consultando el archivo de configuración externo `usuarios.json`, facilitando la administración de altas y bajas de personal sin necesidad de alterar la lógica del programa.
