
# El problema: 
# Necesitas identificar qué equipo interno envió más bytes hacia internet.
# Objetivo: 
# Lee un archivo CSV que contenga: ip_interna, bytes_enviados. El script 
# debe devolver la IP que más datos transfirió y calcular el porcentaje 
# de esos datos respecto al total de la red.

import csv 
import os


carpeta_actual = os.path.dirname(os.path.abspath(__file__))

archivo_csv = os.path.join(carpeta_actual, 'datos_trafico.csv')

lista_datos = []
total_bytes = 0


with open(archivo_csv, 'r', encoding='utf-8') as archivo:
    
    lector = csv.DictReader(archivo)
    lector.fieldnames = [col.strip() for col in lector.fieldnames]
    
    for fila in lector:
        ip = fila['ip_interna']
        bytes_enviados = int(fila['bytes_enviados'])   
        
        lista_datos.append((ip, bytes_enviados))
        total_bytes += bytes_enviados
        
        

ip_mayor = ''
cantidad_mayor = 0


for ip, cantidad in lista_datos:
    if cantidad > cantidad_mayor:
        cantidad_mayor = cantidad
        ip_mayor = ip
        
        
if total_bytes > 0:
    porcentaje = (cantidad_mayor / total_bytes) * 100
else:
    porcentaje = 0 
    

print("=== ANALISIS DE TRAFICO ===")
print(f"Total de bytes enviados en la red: {total_bytes:,} bytes")
print(f"Equipo con mayor transferencia:\n IP: {ip_mayor}")
print(f"Bytes enviados: {cantidad_mayor:,} bytes")
print(f"Porcentaje sobre el total: {porcentaje:.2f} %")