

-- BRUTE FORCE 

-- Objetivo: 
-- Encuentra las IPs (ip_origen) en la tabla vpn_logs
-- que tengan más de 50 intentos con estado 'FALLO'.
-- Requisito:
-- Tu consulta debe devolver la IP y el total de fallos
-- (puedes llamarlo total_fallos), ordenado de mayor a menor.



SELECT ip_origen, COUNT(*) AS total_fallos
FROM vpn_logs 
WHERE estado = 'FALLO'
GROUP BY ip_origen
HAVING COUNT(*) > 50
ORDER BY total_fallos DESC;



-- EXFILTRATION

-- Objetivo: 
-- En la tabla firewall_logs, encuentra a los equipos internos que 
-- podrían estar robando información cifrada.
-- Requisito:
--  Suma los bytes_enviados por cada ip_origen, filtrando solo el tráfico
--  cuyo puerto_destino sea 443 (HTTPS) y la accion sea 'PERMITIDO'. 
-- Muestra el Top 3 de IPs que más datos enviaron.


SELECT ip_origen, SUM(bytes_enviados) AS total_bytes_enviados
FROM firewall_logs
WHERE puerto_destino = 443 AND accion = 'PERMITIDO'
GROUP BY ip_origen
ORDER BY total_bytes_enviados DESC
LIMIT 3;



-- impossible_travel

-- Objetivo: 
-- Un usuario malicioso podría haber robado la contraseña de un empleado
--  e iniciado sesión desde Rusia, mientras el empleado real está en México.
-- Requisito:
--  Encuentra a los usuarios (usuario) en vpn_logs que hayan iniciado sesión 
-- con 'EXITO' desde más de 1 país diferente.
-- Tip de Analista: Vas a necesitar usar la función COUNT(DISTINCT pais) en tu cláusula HAVING.


