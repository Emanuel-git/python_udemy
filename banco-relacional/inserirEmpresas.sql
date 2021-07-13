ALTER TABLE empresas MODIFY cnpj VARCHAR(14)

INSERT INTO empresas
    (nome, cnpj)
VALUES
    ('Bradesco', '24306217000192'),
    ('Vale', '25279658000105'),
    ('Cielo', '84614144000128');


DESC empresas;
DESC prefeitos;
SELECT * FROM empresas;
SELECT * FROM cidades;

INSERT INTO empresas_unidades
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0),
    (2, 2, 1);