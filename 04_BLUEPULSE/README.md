 BluePulse: Motor de Detección de Amenazas (SecOps)

Este proyecto es una herramienta de automatización diseñada para el análisis forense y la detección proactiva de amenazas. El motor procesa archivos de logs en tiempo real para identificar patrones de ataque comunes sin necesidad de herramientas externas.

 Capacidades del Motor

Análisis de Logs: Procesamiento eficiente de archivos de registros (access.log).

Detección de Fuzzing: Identificación automatizada de atacantes buscando directorios ocultos mediante el conteo de errores HTTP 404.

Correlación de Datos: Uso de diccionarios en Python para la agregación de datos por IP, optimizando el rendimiento de búsqueda.

Alertas Críticas: Generación de notificaciones en consola ante la superación de umbrales de seguridad definidos.

 Tecnologías Utilizadas

Lenguaje: Python 3.x

Conceptos SecOps: Análisis de logs, Threat Hunting, Detección de anomalías.

 Cómo utilizar

Asegúrate de tener los logs en la carpeta ./logs/.

Ejecuta el motor desde la raíz:

python3 bluepulse_engine.py


Desarrollado como parte de mi especialización en Operaciones de Seguridad.