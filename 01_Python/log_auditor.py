

# El problema: Tienes un archivo de logs masivo y necesitas detectar ataques de fuerza bruta.
# Objetivo: 
#   Escribe un script que lea un archivo /var/log/auth.log, 
#   cuente cuantos intentos fallidos por IP existen, y genere 
#   una alerta (print) para todas las IPs que superen los 10 intentos fallidos.


contador_404 = 0
cuentas_ips = {}
umbral_ataque = 10

with open('/var/log/auth.log') as archivo:
    
    for linea in archivo:
        
        partes = linea.split()
        extraer_codigo = partes[8]
        ip = partes[0]
        
        if extraer_codigo == '404':
            contador_404 += 1
            
            if ip not in cuentas_ips:
                cuentas_ips[ip] = 1
            else:
                cuentas_ips[ip] += 1
                

for ip, cantidad in cuentas_ips.items(): 

	if cantidad > umbral_ataque: 
		print(f'ALERTA ESTA IP {ip} ESTA ATACANDO | CANTIDAD DE ERRORES: {cantidad}') 
