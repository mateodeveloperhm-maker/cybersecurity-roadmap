

# El problema: 
# Necesitas saber rapidamente si los servicios criticos estan activos en una red interna.
# Objetivo:
# Crea un script que reciba una lista de IPs (de un archivo .txt) y un puerto 
# (ej. 22). El script debe intentar conectarse a esos puertos y reportar cuales estan "ABIERTO" y cuales "CERRADO".

# Libreria sugerida: socket (es una libreria nativa de Python, no necesitas instalar nada).



import socket
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))

archivo = os.path.join(carpeta_actual, 'archivo.txt')

with open(archivo, 'r') as archivo:
    
    ips = archivo.readlines()
    
    archivo.close()
    
    lista_ips = []
    
    for linea in ips:
        ip_limpia = linea.strip()
        if ip_limpia:
            lista_ips.append(ip_limpia)
            
    for ip in lista_ips:
        
        s = socket.socket()
        s.settimeout(1)
        
        puerto = 22
        resultado = s.connect_ex((ip, puerto))
        
        if resultado == 0:
            print(f'Se conecto correctamente {ip}:{puerto}')
        else:
            print(f'No se conecto {ip}:{puerto}')
         
        s.close()  
            
    

    



     
    
    
    
    