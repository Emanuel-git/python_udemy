from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = (
    ('Diego', '99765-4321'),
    ('Ana', '97765-4321'),
    ('Carlos', '95765-4321'),
    ('John', '90765-4321'),
    ('Ricardo', '92765-4321'),
    ('Caio', '91765-4321'),
    ('Matheus', '93765-4321')
    )

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')