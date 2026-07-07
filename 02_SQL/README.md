Threat Hunting & SOC Analysis con SQL

Este proyecto demuestra la aplicación de SQL para el análisis de operaciones de seguridad (SOC) y la detección proactiva de amenazas (Threat Hunting). A través de la agregación de logs, se mapean comportamientos anómalos para identificar técnicas de ataques informáticos.

Casos de Uso y Funcionalidades Destacadas

Detección de Account Takeover (Viaje Imposible):
Uso de COUNT(DISTINCT pais) en cláusulas HAVING para identificar sesiones concurrentes desde ubicaciones geográficas anómalas, previniendo el secuestro de sesiones.

Rastreo de Exfiltración de Datos:
Uso de SUM(bytes_enviados) y filtrado estricto de puertos de salida (ej. 443 HTTPS) para detectar fugas masivas de información hacia servidores externos.

Identificación de Fuerza Bruta Distribuida:
Implementación de GROUP BY y agregaciones para aislar IPs atacantes en los registros de acceso remoto (VPN Logs) que superan el umbral de fallos permitidos.

Dimensionamiento de Brechas (Scoping):
Inclusión de recuentos totales de conexión para calcular el Dwell Time (tiempo de permanencia) del adversario y facilitar la investigación forense.

Tecnologías y Conceptos

Lenguaje: SQL (Lógica aplicable a PostgreSQL, MySQL, SQL Server).

Conceptos SecOps: Análisis de logs de Firewall y VPN, Mapeo MITRE ATT&CK, User Behavior Analytics (UBA).

Archivos del Proyecto

SQL_exercises.sql: Contiene el código fuente con las consultas de agregación, filtrado y ordenamiento utilizadas para la detección de las amenazas descritas.