"""
MÓDULO 4.1: ENGENHARIA DE DADOS TABULARES COM PANDAS
Objetivo: Fundamentos de Series, DataFrames, Inspeção e Operações Vetorizadas.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

import pandas as pd

print("=" * 65)

### Kata 1: Criação de Series e Inspeção Unidimensional
# Cenário: Uma esteira de sensores recebe uma lista de medições de pressão em bar.
# Crie uma Series do Pandas chamada 'serie_pressao' a partir de 'medicoes_raw'.
# Extraia o número total de elementos para a variável 'tamanho_serie' (int)
# e o tipo de dado da Series para 'tipo_serie' (string ou dtype).
# Dados de entrada:
medicoes_raw = [101.3, 102.1, 99.8, 100.5, 103.2]
serie_pressao = None
tamanho_serie = 0
tipo_serie = None
serie_pressao = pd.Series(medicoes_raw)
tamanho_serie = serie_pressao.size
tipo_serie = serie_pressao.dtype

print(f"K1 - Tamanho: {tamanho_serie} | Tipo: {tipo_serie}")
# Saída esperada: Tamanho: 5 | Tipo: float64
print("=" * 65)


### Kata 2: Construção de DataFrame via Dicionário de Colunas
# Cenário: Um sistema de inventário precisa estruturar os dados de servidores em uma tabela.
# 1. Crie o DataFrame 'df_servidores' a partir do dicionário 'dados_infra'.
# 2. Extraia a tupla de dimensões (linhas, colunas) para a variável 'dimensoes_tabela'.
# 3. Extraia a lista com o nome de todas as colunas para 'nomes_colunas'.
# Dados de entrada:
dados_infra = {
    "hostname": ["srv-app-01", "srv-app-02", "srv-db-01", "srv-cache-01"],
    "cpu_cores": [8, 8, 32, 16],
    "memoria_gb": [16, 16, 128, 64],
    "status": ["ATIVO", "ATIVO", "ATIVO", "MANUTENCAO"]
}
df_servidores = None
dimensoes_tabela = ()
nomes_colunas = []
df_servidores = pd.DataFrame(dados_infra)
dimensoes_tabela = df_servidores.shape
nomes_colunas = list(df_servidores.columns)

print("K2 - Dimensões:", dimensoes_tabela)
print("K2 - Colunas:", nomes_colunas)
# Saída esperada:
# Dimensões: (4, 4)
# Colunas: ['hostname', 'cpu_cores', 'memoria_gb', 'status']
print("=" * 65)


### Kata 3: Projeção de Colunas Selecionadas
# Cenário: Em pipelines analíticos, selecionamos apenas as colunas necessárias para economizar memória.
# A partir do DataFrame 'df_clientes', crie um novo DataFrame 'df_projecao' contendo
# EXCLUSIVAMENTE as colunas 'nome' e 'saldo_conta' (nessa ordem).
# Dados de entrada:
dados_clientes = {
    "cliente_id": [1001, 1002, 1003],
    "nome": ["Alice Silva", "Bruno Santos", "Carla Dias"],
    "cidade": ["São Paulo", "Curitiba", "Recife"],
    "saldo_conta": [15400.50, 8200.00, 23150.75],
    "score_credito": [780, 690, 810]
}
df_clientes = pd.DataFrame(dados_clientes)
df_projecao = None
df_projecao = df_clientes[["nome","saldo_conta"]]
# Espaço para resolução:


print("K3 - Colunas da Projeção:", list(df_projecao.columns) if df_projecao is not None else [])
print("K3 - Quantidade de Linhas:", len(df_projecao) if df_projecao is not None else 0)
# Saída esperada:
# Colunas da Projeção: ['nome', 'saldo_conta']
# Quantidade de Linhas: 3
print("=" * 65)


### Kata 4: Criação de Coluna Derivada Vetorizada
# Cenário: Uma esteira de faturamento precisa calcular o valor total de cada item vendido.
# 1. No DataFrame 'df_vendas', crie uma nova coluna chamada 'valor_total'
# multiplicando a coluna 'quantidade' pela coluna 'preco_unitario'.
# 2. Em seguida, calcule a soma total da coluna 'valor_total' e armazene na variável 'faturamento_total'.
# Dados de entrada:
dados_vendas = {
    "item": ["Teclado Mecânico", "Monitor 27", "Mouse Sem Fio"],
    "quantidade": [5, 2, 10],
    "preco_unitario": [250.0, 1200.0, 80.0]
}
df_vendas = pd.DataFrame(dados_vendas)
faturamento_total = 0.0
df_vendas["Valor_total"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]
faturamento_total = df_vendas["Valor_total"].sum()

print("K4 - Faturamento Total:", faturamento_total)
# Saída esperada: 4450.0
print("=" * 65)


### Kata 5: Construção via Lista de Registros e Filtragem Booleana
# Cenário: Eventos de telemetria chegam como uma lista de dicionários individuais.
# 1. Crie o DataFrame 'df_eventos' a partir de 'eventos_brutos'.
# 2. Crie um novo DataFrame 'df_erros' filtrando apenas as linhas onde a coluna 'nivel' é igual a "ERROR".
# 3. Guarde o número total de linhas com erro na variável 'total_erros' (int).
# Dados de entrada:
eventos_brutos = [
    {"timestamp": "2026-10-01 10:00:01", "nivel": "INFO", "modulo": "auth", "latencia_ms": 45},
    {"timestamp": "2026-10-01 10:00:03", "nivel": "ERROR", "modulo": "database", "latencia_ms": 1200},
    {"timestamp": "2026-10-01 10:00:05", "nivel": "WARN", "modulo": "cache", "latencia_ms": 180},
    {"timestamp": "2026-10-01 10:00:08", "nivel": "ERROR", "modulo": "payment", "latencia_ms": 3400},
    {"timestamp": "2026-10-01 10:00:10", "nivel": "INFO", "modulo": "auth", "latencia_ms": 50}
]
df_eventos = None
df_erros = None
total_erros = 0
df_eventos = pd.DataFrame(eventos_brutos)
df_erros = df_eventos[df_eventos["nivel"] == "ERROR"]
total_erros = len(df_erros)

print("K5 - Total de Erros Filtrados:", total_erros)
# Saída esperada: 2
print("=" * 65)
