


#!/bin/bash

REPORTE='reporte_incidente.txt'


echo "=====================================" > $REPORTE
echo "      REPORTE DE TRIAGE - INCIDENT" >> $REPORTE
echo "=====================================" >> $REPORTE
echo "Generado por: $0"                    >> $REPORTE
echo "" >> $REPORTE


echo "=== RETO 1: HUELLA DIGITAL - FECHA Y KERNEL ===" >> $REPORTE 
echo "Fecha y hora del análisis : $(date)"     >> $REPORTE
echo "Información completa Kernel : $(uname -a)"         >> $REPORTE
echo "Hostname del equipo         : $(hostname)"         >> $REPORTE
echo "" >> $REPORTE

echo "=== RETO 2: CONEXIONES DE RED ACTIVAS ===" >> $REPORTE
echo "t=TCP | u=UDP | l=ESCUCHA | n=IPs SIN RESOLVER | p=PROGRAMA/PID" >> $REPORTE
ss -tulnp >> $REPORTE


if [ $? -ne 0 ]; then
    echo "--- (usando netstat por compatibilidad) ---" >> $REPORTE
    netstat -tulnp >> $REPORTE
fi
echo "" >> $REPORTE



echo "=== RETO 3: USUARIOS CONECTADOS ACTUALMENTE ===" >> $REPORTE
echo "--- comando w (COMPLETO: qué están ejecutando) ---" >> $REPORTE
w >> $REPORTE
echo "" >> $REPORTE
echo "--- comando who (RESUMIDO: usuario + IP) ---" >> $REPORTE
who >> $REPORTE
echo "" >> $REPORTE


echo "=== RETO 4: LOGS AUTENTICACIÓN - ÚLTIMOS 15 EVENTOS ===" >> $REPORTE
echo " Busca estas palabras clave:" >> $REPORTE
echo "    Failed password  = INTENTO FALLIDO  → FUERZA BRUTA" >> $REPORTE
echo "    Accepted         = INICIO DE SESIÓN EXITOSO" >> $REPORTE
echo "    Invalid user     = USUARIO QUE NO EXISTE" >> $REPORTE
echo "" >> $REPORTE


if [ -f /var/log/auth.log ]; then
    tail -n 15 /var/log/auth.log >> $REPORTE
elif [ -f /var/log/secure ]; then
    tail -n 15 /var/log/secure   >> $REPORTE
else
    echo "  No se encontró archivo de auth" >> $REPORTE
fi
echo "" >> $REPORTE



echo "=====================================" >> $REPORTE
echo " REPORTE TERMINADO: $REPORTE"       >> $REPORTE
echo "=====================================" >> $REPORTE

# Mensaje en TU PANTALLA
echo ""
echo " LISTO! Reporte guardado en: $REPORTE"
echo " Para leerlo escribe:  cat $REPORTE"
echo ""
