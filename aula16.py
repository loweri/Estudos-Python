"""
MÓDULO 4.3: COMBINAÇÃO DE DADOS, JOINS E TRATAMENTO TEMPORAL COM PANDAS
Objetivo: Merges (Inner/Left Join), concatenação, conversão de tipos e manipulação de datas.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

import pandas as pd

print("=" * 65)

### Kata 1: Junção Interna (Inner Join)
# Cenário: Uma esteira de faturamento precisa combinar os pedidos realizados com o catálogo
# de produtos para obter o nome e o preço de cada item faturado.
# 1. Realize uma junção interna entre 'df_pedidos' e 'df_produtos' usando a coluna 'produto_id' como chave.
# 2. Armazene o DataFrame resultante em 'df_pedidos_completos'.
# 3. Armazene a quantidade total de linhas da tabela resultante na variável 'total_pedidos_completos' (int).
# Dados de entrada:
dados_pedidos = {
    "pedido_id": [1, 2, 3, 4],
    "produto_id": [101, 102, 101, 105],
    "quantidade": [2, 1, 5, 1]
}
dados_produtos = {
    "produto_id": [101, 102, 103],
    "nome_produto": ["Mouse", "Teclado", "Monitor"],
    "preco": [80.0, 250.0, 1200.0]
}
df_pedidos = pd.DataFrame(dados_pedidos)
df_produtos = pd.DataFrame(dados_produtos)
df_pedidos_completos = None
total_pedidos_completos = 0
df_pedidos_completos = pd.merge(df_pedidos, df_produtos, on="produto_id", how="inner")
total_pedidos_completos = len(df_pedidos_completos)

print("K1 - Total de Pedidos Completos:", total_pedidos_completos)
print("K1 - Colunas Resultantes:", list(df_pedidos_completos.columns) if df_pedidos_completos is not None else [])
# Saída esperada:
# Total de Pedidos Completos: 3
# Colunas Resultantes: ['pedido_id', 'produto_id', 'quantidade', 'nome_produto', 'preco']
print("=" * 65)


### Kata 2: Junção à Esquerda (Left Join)
# Cenário: O time de relacionamento precisa listar todos os clientes cadastrados e seus planos.
# Clientes que ainda não assinaram nenhum plano devem continuar no relatório (com valores ausentes).
# 1. Realize uma junção preservando TODOS os registros de 'df_clientes' associados a 'df_assinaturas' pela coluna 'cliente_id'.
# 2. Armazene o resultado em 'df_relatorio_clientes'.
# 3. Conte quantos clientes ficaram sem plano (valores ausentes na coluna 'plano') e guarde na variável 'clientes_sem_plano' (int).
# Dados de entrada:
dados_clientes = {
    "cliente_id": [10, 20, 30, 40],
    "nome": ["Alice", "Bob", "Carol", "Daniel"]
}
dados_assinaturas = {
    "cliente_id": [10, 30],
    "plano": ["Premium", "Básico"]
}
df_clientes = pd.DataFrame(dados_clientes)
df_assinaturas = pd.DataFrame(dados_assinaturas)
df_relatorio_clientes = None
clientes_sem_plano = 0
df_relatorio_clientes = pd.merge(df_clientes, df_assinaturas, on="cliente_id", how="left")
clientes_sem_plano = int(df_relatorio_clientes["plano"].isna().sum())

print("K2 - Total de Clientes no Relatório:", len(df_relatorio_clientes) if df_relatorio_clientes is not None else 0)
print("K2 - Clientes Sem Plano:", clientes_sem_plano)
# Saída esperada:
# Total de Clientes no Relatório: 4
# Clientes Sem Plano: 2
print("=" * 65)


### Kata 3: Concatenação Vertical (Empilhamento de Lotes)
# Cenário: Um data lake recebe dados de vendas em arquivos separados por região geográfica.
# 1. Empilhe verticalmente os DataFrames 'df_vendas_sul' e 'df_vendas_sudeste' em um único DataFrame chamado 'df_vendas_brasil'.
# 2. Garanta que o índice do DataFrame consolidado seja redefinido de forma contínua (de 0 a N-1).
# 3. Armazene o número total de linhas em 'total_vendas_brasil' (int).
# Dados de entrada:
dados_sul = {
    "venda_id": [1001, 1002],
    "filial": ["Curitiba", "Porto Alegre"],
    "total": [450.0, 780.0]
}
dados_sudeste = {
    "venda_id": [2001, 2002, 2003],
    "filial": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"],
    "total": [1200.0, 950.0, 600.0]
}
df_vendas_sul = pd.DataFrame(dados_sul)
df_vendas_sudeste = pd.DataFrame(dados_sudeste)
df_vendas_brasil = None
total_vendas_brasil = 0
df_vendas_brasil = pd.concat([df_vendas_sul, df_vendas_sudeste], ignore_index=True)
total_vendas_brasil = len(df_vendas_brasil)

print("K3 - Total de Vendas Brasil:", total_vendas_brasil)
print("K3 - Índice Final:", list(df_vendas_brasil.index) if df_vendas_brasil is not None else [])
# Saída esperada:
# Total de Vendas Brasil: 5
# Índice Final: [0, 1, 2, 3, 4]
print("=" * 65)


### Kata 4: Conversão de Tipos de Dados
# Cenário: Na ingestão de um sistema legado, códigos de departamento vieram como números inteiros
# e tarifas adicionais vieram como strings de texto.
# 1. No DataFrame 'df_funcionarios', converta a coluna 'depto_codigo' para o tipo texto (string / 'str').
# 2. Converta a coluna 'tarifa_adicional' para número decimal ('float').
# 3. Armazene os tipos resultantes dessas colunas nas variáveis 'tipo_depto' e 'tipo_tarifa'.
# Dados de entrada:
dados_funcionarios = {
    "func_id": [1, 2, 3],
    "depto_codigo": [10, 20, 10],
    "tarifa_adicional": ["15.50", "22.00", "0.00"]
}
df_funcionarios = pd.DataFrame(dados_funcionarios)
tipo_depto = None
tipo_tarifa = None
df_funcionarios["depto_codigo"] = df_funcionarios["depto_codigo"].astype(str)
df_funcionarios["tarifa_adicional"] = df_funcionarios["tarifa_adicional"].astype(float)
tipo_depto = df_funcionarios["depto_codigo"].dtype
tipo_tarifa = df_funcionarios["tarifa_adicional"].dtype

print(f"K4 - Tipo Depto: {tipo_depto} | Tipo Tarifa: {tipo_tarifa}")
# Saída esperada: Tipo Depto: object (ou string) | Tipo Tarifa: float64
print("=" * 65)


### Kata 5: Tratamento Temporal e Extração de Atributos
# Cenário: Uma esteira de auditoria precisa analisar datas de transações financeiras.
# 1. Converta a coluna 'data_registro' do DataFrame 'df_auditoria' (atualmente texto) para o tipo data/hora do Pandas.
# 2. Crie uma nova coluna chamada 'ano' contendo exclusivamente o ano de cada registro.
# 3. Calcule quantas transações ocorreram no ano de 2026 e guarde na variável 'transacoes_2026' (int).
# Dados de entrada:
dados_auditoria = {
    "log_id": [501, 502, 503, 504, 505],
    "data_registro": ["2025-11-20", "2026-01-15", "2026-03-10", "2025-12-31", "2026-04-05"],
    "valor": [100.0, 250.0, 310.0, 80.0, 420.0]
}
df_auditoria = pd.DataFrame(dados_auditoria)
transacoes_2026 = 0
df_auditoria["data_registro"] = pd.to_datetime(df_auditoria["data_registro"])
df_auditoria["ano_registro"] = df_auditoria["data_registro"].dt.year
transacoes_2026 = int((df_auditoria["ano_registro"] == 2026).sum())

print("K5 - Transações em 2026:", transacoes_2026)
# Saída esperada: 3
print("=" * 65)
