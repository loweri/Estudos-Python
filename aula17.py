"""
MÓDULO 4.4: SQL RELACIONAL COM PYTHON (SQLITE3 & PANDAS)
Objetivo: Conexão com banco relacional, criação de tabelas, inserção, consultas analíticas e integração com Pandas.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

import sqlite3
import pandas as pd

print("=" * 65)

### Kata 1: Conexão e Criação de Tabela Relacional
# Cenário: Uma esteira de ingestão precisa inicializar um banco relacional em memória e estruturar
# a tabela 'dispositivos' para armazenar ativos de tecnologia.
# 1. Crie uma conexão SQLite em memória (usando ":memory:") armazenada em 'conexao'.
# 2. Obtenha o cursor dessa conexão na variável 'cursor'.
# 3. Crie a tabela 'dispositivos' contendo as colunas:
#    - 'id': número inteiro e chave primária
#    - 'hostname': texto
#    - 'ip': texto
#    - 'memoria_gb': número inteiro
# 4. Guarde o nome da tabela criada na variável 'nome_tabela_criada' (string).
conexao = None
cursor = None
nome_tabela_criada = ""
conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()
cursor.execute("""
    CREATE TABLE dispositivos (
    id INTEGER PRIMARY KEY,
    hostname TEXT,
    ip TEXT,
    memoria_gb INTEGER
    );
""")
# Verificação de integridade no catálogo do banco:
if cursor is not None:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='dispositivos';")
    res = cursor.fetchone()
    nome_tabela_criada = res[0] if res else ""

print("K1 - Tabela Criada no Banco:", nome_tabela_criada)
# Saída esperada: dispositivos
print("=" * 65)


### Kata 2: Inserção de Registros e Confirmação de Volumetria
# Cenário: O inventário precisa carregar os dados de dispositivos na tabela relacional recém-criada.
# 1. Insira todos os registros da lista 'lote_dispositivos' na tabela 'dispositivos'.
# 2. Confirme a transação na conexão.
# 3. Consulte a quantidade total de linhas presentes na tabela 'dispositivos' e armazene na variável 'total_registros_inseridos' (int).
# Dados de entrada:
lote_dispositivos = [
    (1, "srv-app-01", "192.168.1.10", 32),
    (2, "srv-app-02", "192.168.1.11", 32),
    (3, "srv-db-01", "192.168.1.20", 128),
    (4, "srv-cache-01", "192.168.1.30", 64),
    (5, "srv-db-02", "192.168.1.21", 128)
]
total_registros_inseridos = 0
cursor.executemany("""
    INSERT INTO dispositivos (id, hostname, ip, memoria_gb)
    VALUES (?, ?, ?, ?);
""",lote_dispositivos)
conexao.commit()
cursor.execute("SELECT COUNT(*) FROM dispositivos;")
total_registros_inseridos = cursor.fetchone()[0]

print("K2 - Total de Registros no Banco:", total_registros_inseridos)
# Saída esperada: 5
print("=" * 65)


### Kata 3: Consulta com Filtragem Condicional
# Cenário: A equipe de segurança precisa listar os servidores com alta capacidade de memória (maior ou igual a 64 GB).
# 1. Execute uma consulta SQL que selecione 'hostname' e 'memoria_gb' da tabela 'dispositivos'
#    onde 'memoria_gb' seja maior ou igual a 64.
# 2. Recupere todas as linhas retornadas e armazene na lista 'servidores_alta_memoria'.
servidores_alta_memoria = []
cursor.execute("""
    SELECT hostname, memoria_gb
    FROM dispositivos
    WHERE memoria_gb >= 64;
""")
servidores_alta_memoria = cursor.fetchall()

print("K3 - Servidores Filtrados:", servidores_alta_memoria)
# Saída esperada: [('srv-db-01', 128), ('srv-cache-01', 64), ('srv-db-02', 128)]
print("=" * 65)


### Kata 4: Agregação Relacional com Agrupamento
# Cenário: A gestão de infraestrutura precisa de um relatório com a quantidade de servidores agrupada por capacidade de memória.
# 1. Execute uma consulta SQL que retorne a 'memoria_gb' e a contagem total de servidores para cada faixa de memória.
# 2. Ordene o resultado pela 'memoria_gb' de forma crescente.
# 3. Recupere os registros na lista 'resumo_por_memoria'.
resumo_por_memoria = []
cursor.execute("""
    SELECT memoria_gb, COUNT(*)
    FROM dispositivos
    GROUP BY memoria_gb
    ORDER BY memoria_gb ASC;
""")
resumo_por_memoria = cursor.fetchall()

print("K4 - Resumo por Memória:", resumo_por_memoria)
# Saída esperada: [(32, 2), (64, 1), (128, 2)]
print("=" * 65)


### Kata 5: Integração SQL + Pandas (Bridge de Dados)
# Cenário: Engenheiros de dados frequentemente carregam consultas SQL diretamente em DataFrames para análises avançadas.
# 1. Execute a consulta "SELECT hostname, ip, memoria_gb FROM dispositivos WHERE memoria_gb > 32"
#    carregando o resultado diretamente em um DataFrame do Pandas chamado 'df_servidores_pesados'
#    através da própria conexão do banco.
# 2. Armazene a quantidade de linhas desse DataFrame na variável 'total_pesados' (int).
df_servidores_pesados = None
total_pesados = 0
query = "SELECT hostname, ip, memoria_gb FROM dispositivos WHERE memoria_gb > 32"
df_servidores_pesados = pd.read_sql_query(query, conexao)
total_pesados = len(df_servidores_pesados)

print("K5 - Total de Servidores no DataFrame:", total_pesados)
print("K5 - Colunas do DataFrame:", list(df_servidores_pesados.columns) if df_servidores_pesados is not None else [])
# Saída esperada:
# Total de Servidores no DataFrame: 3
# Colunas do DataFrame: ['hostname', 'ip', 'memoria_gb']
print("=" * 65)

# Fechamento seguro da conexão
if conexao is not None:
    conexao.close()
