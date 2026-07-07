

# El problema: 
# ¿Cómo saber si un atacante modificó un archivo de configuración clave (como /etc/passwd)?
# Objetivo: 
# Crea un script que calcule el hash (MD5 o SHA256) de un archivo específico
# y lo compare con un hash previamente guardado. Si el hash cambia, el script
# debe imprimir una alerta crítica: "¡INTEGRIDAD COMPROMETIDA!".



import hashlib
from datetime import datetime
import os

carpeta_actual = os.path.dirname(os.path.abspath(__file__))

# hash_para_vigilar = os.path.join(carpeta_actual, 'hash_para_vigilar.txt')
# referencia_de_hash = os.path.join(carpeta_actual, 'referencia_de_hash.txt')

# algoritmo = hashlib.sha256()

# with open(hash_para_vigilar, 'rb') as archivo:
#     while True:
#         datos = archivo.read(4096)
        
#         if not datos:
#             break
        
#         algoritmo.update(datos)
        
        
# hash_generado = algoritmo.hexdigest()

# print("Hash creado por primera vez:")
# print(hash_generado)



# with open(referencia_de_hash, 'w') as ref:
#     ref.write(hash_generado)
    




archivo_objetivo = os.path.join(carpeta_actual, 'hash_para_vigilar.txt')

archivo_referencia = os.path.join(carpeta_actual, 'referencia_de_hash.txt')
    
archivo_registro = os.path.join(carpeta_actual, 'registro_verificaciones.txt')



def calcular_hash(ruta):    
    algoritmo = hashlib.sha256()
    with open(ruta, 'rb') as archivo:
        while True:
            datos = archivo.read(4096)
            if not datos:
                break
            algoritmo.update(datos)
    return algoritmo.hexdigest()    


with open(archivo_referencia, 'r') as ref:
    hash_guardado = ref.read().strip()
    
hash_actual = calcular_hash(archivo_objetivo)

fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("=== VERIFICACIÓN DE INTEGRIDAD ===")
print(f"Fecha: {fecha}")
print(f"Hash de referencia: {hash_guardado}")
print(f"Hash actual:        {hash_actual}")

if hash_actual == hash_guardado:
    estado = "ARCHIVO ÍNTEGRO - Sin cambios detectados"
else:
    estado = "¡INTEGRIDAD COMPROMETIDA! El archivo fue modificado"

print(f"\nResultado: {estado}")

with open(archivo_registro, 'a', encoding="utf-8") as log:
    log.write(f"[{fecha}] | {estado} | Referencia: {hash_guardado} | Actual: {hash_actual}\n")

print(f"\nRegistro guardado en: {archivo_registro}")