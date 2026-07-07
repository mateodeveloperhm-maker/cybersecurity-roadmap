🛡️ Python for Cybersecurity & SecOps

Este repositorio contiene una colección de scripts de automatización desarrollados en Python, enfocados en Operaciones de Seguridad (SecOps), Análisis de Tráfico y Respuesta a Incidentes.

El objetivo de estas herramientas es demostrar la capacidad de extraer, transformar y alertar sobre datos críticos utilizando únicamente la biblioteca estándar de Python (sin dependencias externas), garantizando alta portabilidad en entornos de servidores.

🛠️ Herramientas Desarrolladas

1. Vigilante de Logs (Log Auditor)

Analiza archivos masivos de autenticación (auth.log) para detectar ataques de fuerza bruta.

Técnica: Parseo de cadenas, manipulación de diccionarios en memoria (O(1) lookup).

Uso en la vida real: Detección de intrusiones y enumeración de directorios (Fuzzing).

2. Escáner de Puertos Ligero (Port Scanner)

Verifica la disponibilidad de servicios críticos a través de una red interna leyendo IPs desde un archivo de texto.

Técnica: Uso de la librería nativa socket, manejo de conexiones TCP y control de timeouts.

Uso en la vida real: Auditoría de superficie de ataque y validación de reglas de Firewall.

3. Detector de Integridad (Hacker Hunter)

Calcula y compara firmas criptográficas de archivos críticos de configuración (ej. /etc/passwd) para alertar sobre modificaciones no autorizadas.

Técnica: Uso de hashlib (SHA-256) y lectura de archivos por bloques (Chunks de 4096 bytes) para prevenir desbordamientos de memoria (Memory Leaks).

Uso en la vida real: Prevención de persistencia de atacantes y detección de Rootkits.

4. Reporteador de Exfiltración (Exfiltration Tracker)

Analiza registros CSV de tráfico de red para identificar el equipo interno con mayor volumen de transferencia hacia internet.

Técnica: Uso de csv.DictReader, cálculos de porcentajes y formateo matemático.

Uso en la vida real: Detección de movimiento lateral y exfiltración de datos confidenciales hacia servidores C2.

⚙️ Tecnologías Utilizadas

Lenguaje: Python 3.x

Librerías (Built-in): os, csv, socket, hashlib, datetime

Entorno: Linux / Windows

🚀 Cómo Ejecutar

Clona este repositorio y asegúrate de mantener los archivos de datos (.txt, .csv) en el mismo directorio que los scripts. Las rutas están configuradas de manera relativa utilizando os.path.abspath para máxima compatibilidad.

git clone https://github.com/TuUsuario/python-cybersecurity.git
cd python-cybersecurity
python exfiltration_tracker.py
