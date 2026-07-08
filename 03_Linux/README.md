 Incident Response: Triage Collector (Bash)

Script de automatización desarrollado en Bash para la recolección rápida de evidencia forense (Triage) en sistemas Linux comprometidos. Este proyecto está diseñado para ser ejecutado en entornos de Respuesta a Incidentes (IR), donde el tiempo de recolección es crítico.

 El Problema

Durante un incidente de seguridad, los analistas de Blue Team no pueden permitirse revisar manualmente cada comando. Existe el riesgo de contaminar la evidencia, omitir archivos críticos o perder tiempo valioso. Este script automatiza la captura de un "snapshot" del estado del servidor en segundos.

 Capacidades Principales

El script recolecta automáticamente:

Huella del Sistema: Fecha, kernel y hostname para correlación de eventos.

Red: Estado de conexiones activas (usando ss o netstat como fallback de compatibilidad).

Sesiones: Auditoría de usuarios conectados actualmente.

Threat Hunting: Extracción de las últimas 15 líneas de logs de autenticación (auth.log o secure).

 Características Técnicas (Diseño Senior)

Portabilidad: Escrito en Bash puro, sin dependencias externas, ideal para servidores con acceso limitado.

Robustez: Implementación de lógica fallback para comandos de red. Si ss no está disponible, el script cambia automáticamente a netstat.

Seguridad: El reporte se genera mediante redirecciones seguras (>>), asegurando la integridad de los datos recolectados.

 Instrucciones de Uso

Dar permisos de ejecución:

chmod +x triage_collector.sh


Ejecutar como root (o sudo):

sudo ./triage_collector.sh


Analizar el reporte:
El resultado se guardará en reporte_incidente.txt. Puedes visualizarlo con:

cat reporte_incidente.txt


Desarrollado como parte de mi especialización en Operaciones de Seguridad (SecOps).