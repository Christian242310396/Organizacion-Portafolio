# Proyecto 4: HealthData Engine - Plataforma de Procesamiento de Big Data y Evaluación de Arquitecturas Clínicas

## 1. Descripción del Sistema
Este entorno de software funciona como un motor analítico de alto rendimiento diseñado para la ingesta, manipulación, localización y agregación estadística de volúmenes masivos de información (Big Data) en el sector médico. La solución está configurada para procesar de forma nativa sets de **1, 10 y 20 millones de expedientes** clínicos. El core del sistema evalúa empíricamente la eficiencia de los algoritmos y la velocidad de los formatos de almacenamiento, trazando un análisis comparativo de tiempos de ejecución y consumo de memoria RAM entre esquemas de bases de datos planos y estructuras de datos jerárquicas.

---

## 2. Arquitectura de Archivos y Flujo de Datos
El proyecto adopta un diseño estrictamente modular basado en el principio de responsabilidad única, aislando el código fuente dentro del directorio `src/`. El ciclo de vida de los datos se distribuye a través de los siguientes componentes lógicos:

1. **`src/menu.py`**: Interfaz de control principal en terminal que orquesta la ejecución global del sistema y captura los requerimientos del operador.
2. **`src/datos.py`**: Capa lógica de acceso a datos que encapsula las rutinas de lectura de bajo nivel y el parsing optimizado de datasets masivos.
3. **`src/pacientes.py`**: Módulo transaccional encargado de gobernar los hilos de inserción y búsquedas indexadas, manteniendo paridad simétrica entre los formatos.
4. **`src/estadisticas.py`**: Motor analítico de agregación numérica dedicado al cálculo dinámico de métricas (promedios, máximos y mínimos) en memoria.
5. **`src/graficas.py`**: Componente visual que abstrae las matrices de rendimiento para exportar cuadros comparativos de velocidad y latencia.

---

## 3. Sustentación Técnica de Formatos y Mecanismos de Carga

### Carga Fraccionada de Archivos Planos Masivos (`Pandas Chunking`)
* **Criterio de Selección:** Al interactuar con almacenes de texto plano de escala multimillonaria, la carga simultánea del archivo completo colapsaría la memoria de cualquier servidor estándar. Para solucionar este cuello de botella técnico, el motor integra el parámetro de lectura por bloques `chunksize=100000` nativo de **Pandas**. 
* **Mecanismo Operativo:** El script extrae la información en flujos secuenciales fragmentados de manera iterativa. Esto mantiene el consumo de memoria RAM en una tasa fija y controlada, permitiendo al sistema procesar archivos masivos sin degradar el rendimiento del hardware.

### Ingesta de Datos Jerárquicos mediante Flujo Continuo (*JSON Streaming*)
* **Criterio de Selección:** A diferencia de las estructuras JSON estándar organizadas como una única matriz global que exige ser leída en su totalidad antes del mapeo, este software emplea una arquitectura híbrida donde cada línea del documento representa una entidad JSON independiente separada por un salto de línea (`\n`).
* **Mecanismo Operativo:** El canal de datos inicializa el documento en el modo nativo de lectura de texto `r` y ejecuta un recorrido lineal continuo que deserializa los registros fila por fila empleando `json.loads(linea)`. El objeto se descarta de la memoria RAM inmediatamente después de consolidar sus métricas acumuladas, evitando la acumulación innecesaria de caché.

---

## 4. Desacoplamiento de Variables de Entorno (Anti-Hardcoded)
Con el fin de asegurar el cumplimiento de las buenas prácticas institucionales de ingeniería de software, el sistema prescinde de cadenas de texto fijas o rutas estáticas (*hardcoded*) inyectadas en la lógica del código. Las direcciones físicas y los nombres de los recursos de datos se estructuran dinámicamente en tiempo de ejecución basándose en la escala seleccionada por el usuario (por ejemplo, `f"datos_{nuevo_tamano}.csv"`). Todas las funciones matemáticas y analíticas operan de forma paramétrica, permitiendo que el volumen del dataset clínico incremente exponencialmente sin requerir cambios en el código fuente básico del sistema.
