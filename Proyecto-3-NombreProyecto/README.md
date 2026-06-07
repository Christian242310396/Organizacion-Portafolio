# 📈 Proyecto 3: Sales Analytics - Motor Analítico, Persistencia en CSV y Dashboard Interactivo Híbrido

## 1. Descripción del Sistema
Este entorno de software funciona como una solución avanzada de Inteligencia de Negocios (*Business Intelligence*) diseñada para automatizar la auditoría, análisis estadístico y visualización de registros transaccionales de tecnología. El sistema implementa una arquitectura híbrida distribuida en dos capas funcionales: un potente motor matemático estructurado en **Python 3** que procesa grandes volúmenes de datos transaccionales empleando bibliotecas científicas de alto rendimiento, y una interfaz de control web desarrollada en **PHP, HTML5 y CSS3** que actúa como puente operativo ejecutando los scripts backend mediante llamadas de sistema seguras para renderizar tableros informativos en tiempo real.

---

## 2. Arquitectura de Archivos y Flujo de Datos
Siguiendo los estándares institucionales de diseño limpio y ordenamiento de componentes, todos los recursos del proyecto se concentran estrictamente dentro de la carpeta contenedora del entorno técnico. El ciclo de vida y procesamiento de la información se ejecuta bajo el siguiente flujo secuencial:

1. **`ventas_tecnologia.csv`**: Almacén de datos estructurado que aloja el histórico completo de transacciones comerciales con campos dedicados a meses, productos, cantidades y costes unitarios.
2. **`Reportes.py`**: Motor lógico principal encargado de la ingesta de datos, cálculos métricos vectorizados en memoria RAM y generación de indicadores clave para la toma de decisiones corporativas.
3. **`Graficas.py`**: Script analítico secundario enfocado en la generación automatizada de componentes visuales de alto nivel (barras, líneas continuas y sectores circulares) exportados directamente como recursos PNG independientes.
4. **`reporte_resultado.txt`**: Archivo plano de persistencia intermedia que guarda de forma estructurada el texto plano con los balances numéricos resultantes de la ejecución del motor analítico.
5. **`verReporte.php` / `verReporteSeparado.php`**: Controladores de servidor web encargados de invocar el binario de Python local (`shell_exec`), capturar las salidas de datos dinámicas, escribir las bitácoras y renderizar la interfaz HTML final integrando gráficos de rendimiento.

---

## 3. Sustentación Técnica de Formatos y Modos de Acceso

### Persistencia de Datos Estructurada (`ventas_tecnologia.csv`)
* **Criterio de Selección:** Se implementó el formato **CSV (Comma-Separated Values)** para el histórico transaccional comercial debido a su naturaleza ligera basada en texto delimitado por caracteres estructurados. Científicamente, esto garantiza interoperabilidad absoluta entre sistemas e hilos de procesamiento híbridos, erradicando metadatos pesados o propietarios de suites ofimáticas tradicionales, reduciendo la latencia de procesamiento (*overhead*) y optimizando las lecturas concurrentes masivas.
* **Estrategias de Acceso y Manipulación:** El escaneo y carga del recurso se administra mediante la librería científica de alta velocidad **Pandas** a través de la función nativa `pd.read_csv()` bajo codificación robusta. Este proceso mapea las transacciones directamente en matrices indexadas en memoria RAM (*DataFrames*), acelerando las operaciones matemáticas concurrentes como agrupaciones matriciales vectorizadas (`.groupby()`) para calcular sumatorias físicas y monetarias al instante.

### Jerarquía de Información y Abstracción Visual (`Matplotlib`)
* **Justificación de Gráficos Estadísticos:** El cerebro humano procesa estímulos gráficos geométricos con una velocidad exponencialmente mayor que los bloques lineales de texto plano. Por lo tanto, el sistema implementa un motor de visualización estructurado en tres componentes jerárquicos independientes extraídos con `plt.savefig()`:
  * **Gráfica de Barras (`ventas_producto.png`):** Diseñada para la auditoría y análisis comparativo inmediato del volumen físico de unidades desplazadas entre los diferentes artículos comerciales.
  * **Gráfica de Líneas Nodales (`ventas_mes.png`):** Implementada con marcadores secuenciales continuos sobre series temporales para monitorizar de manera inmediata la evolución mensual de ventas, detectando valles operativos o picos de demanda estacional.
  * **Gráfica de Composición Circular (`porcentaje_producto.png`):** Configurada mediante proyecciones proporcionales automatizadas para ilustrar con precisión la participación porcentual de los ingresos totales en el mercado, optimizando la toma de decisiones en el inventariado prioritario.

---

## 4. Desacoplamiento Dinámico y Control de Inyección (Anti-Hardcoded)
Con el objetivo de adherirse a los principios estrictos de código limpio y asegurar la escalabilidad del sistema, las operaciones matemáticas no contienen valores estáticos, strings quemados ni parámetros de negocio fijos de forma rígida dentro de las funciones de cómputo. Métricas gerenciales como la identificación del "Producto con mayores ingresos" mediante `.idxmax()`, "Mes más rentable" o "Producto prioritario para inventario" se autoevalúan de forma completamente dinámica y en tiempo de ejecución. Esto garantiza que el dataset base de transacciones pueda expandir su volumen de filas indefinidamente sin necesidad de reescribir o modificar una sola instrucción de programación en el core del software.
