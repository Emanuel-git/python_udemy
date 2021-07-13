SELECT 
    e.nome AS estado,
    c.nome AS cidade,
    regiao AS região
FROM estados e, cidades c
WHERE e.id = c.estado_id;

SELECT 
    c.nome AS cidade,
    e.nome AS estado,
    regiao AS Região
FROM estados e
INNER JOIN cidades c ON e.id = c.estado_id