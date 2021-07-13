SELECT * FROM estados

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Campinas', 795, 29);

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Niterói', 133.9, 23);

INSERT INTO cidades
    (nome, area, estado_id)
VALUES (
    'Carauaru',
    920.6,
    (SELECT id FROM estados WHERE sigla = 'PE')
);

INSERT INTO cidades
    (nome, area, estado_id)
VALUES (
    'Juazeiro do Norte',
    248.2,
    (SELECT id FROM estados WHERE sigla = 'CE')
);

SELECT * FROM cidades