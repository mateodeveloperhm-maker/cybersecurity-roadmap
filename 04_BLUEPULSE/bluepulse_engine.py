

import os

log_path = './logs/access.log'
umbral_404 = 2



def analizar_logs():
    print(f'=== Iniciando analisis de sitema- Analizando: {log_path}')
    
    conteo_ips = {}
    
    if not os.path.exists(log_path):
        print(f'Error: No encontre el archivo en {log_path}')
        return 
    
    
    with open(log_path, 'r') as archivo:
        for linea in archivo:
            
            partes = linea.split()
            
            if len(partes) < 9: continue
            
            ip = partes[0]
            codigo_estado = partes[7]
            
            if codigo_estado == '404':
                conteo_ips[ip] = conteo_ips.get(ip, 0) +1
                
                
    alertas = False
    for ip, cantidad in conteo_ips.items():
        if cantidad > umbral_404:
            print(f'[!] ALERTA CRITICA: Posible ataque de fuzzing detectado desde: {ip}')
            print(f'Total de errores: {cantidad}')
            alertas = True
            
    if not alertas:
        print('[-] Estado del sistema: Limpio. No se detectaron anomalias.')
    else:
        print('--- Analisis finalizado. Se han detectado amenazas. ---')
    
if __name__ == "__main__":
    analizar_logs()    




