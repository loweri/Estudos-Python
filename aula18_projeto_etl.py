"""
PROJETO FINAL (NÍVEL 5): PIPELINE ETL END-TO-END DE FATURAMENTO
Objetivo: Construção de uma esteira completa de extração, transformação, enriquecimento e carga.
Regra: Resolva cada fase no espaço reservado sem alterar os arquivos de origem.
"""

import sqlite3
import pandas as pd
from datetime import datetime

print("=" * 65)
print("INICIANDO ESTEIRA DE DADOS (ETL PIPELINE)")
print("=" * 65)


### Fase 1: Extração de Múltiplas Fontes (Extract)
# Cenário: O pipeline precisa ingerir dados de duas fontes diferentes no disco:
# um arquivo CSV com as vendas brutas e um arquivo JSON com o cadastro de clientes.
# 1. Carregue o arquivo "vendas_brutas.csv" em um DataFrame chamado 'df_vendas_raw'.
# 2. Carregue o arquivo "clientes_cadastrados.json" em um DataFrame chamado 'df_clientes_raw'.
# 3. Guarde o número de linhas de cada um nas variáveis 'total_linhas_vendas' e 'total_linhas_clientes' (int).
df_vendas_raw = None
df_clientes_raw = None
total_linhas_vendas = 0
total_linhas_clientes = 0

# Espaço para resolução da Fase 1:


print(f"Fase 1 - Vendas Brutas Lidas: {total_linhas_vendas} linhas")
print(f"Fase 1 - Clientes Lidos: {total_linhas_clientes} linhas")
# Saída esperada:
# Vendas Brutas Lidas: 7 linhas
# Clientes Lidos: 4 linhas
print("=" * 65)


### Fase 2: Higienização e Padronização (Transform - Parte 1)
# Cenário: A esteira identificou duplicatas de rede, cupons vazios e datas em formato texto.
# A partir de 'df_vendas_raw':
# 1. Remova as duplicatas baseando-se na coluna 'transacao_id', mantendo a primeira ocorrência.
# 2. Substitua os valores nulos da coluna 'cupom' pelo texto "SEM_CUPOM".
# 3. Converta a coluna 'data_compra' para o formato de data (datetime).
# 4. Armazene o DataFrame resultante em 'df_vendas_limpas' e o total de linhas em 'total_vendas_limpas' (int).
df_vendas_limpas = None
total_vendas_limpas = 0

# Espaço para resolução da Fase 2:


print(f"Fase 2 - Vendas Limpas Restantes: {total_vendas_limpas} linhas")
print("Fase 2 - Tipo da Data Compra:", str(df_vendas_limpas["data_compra"].dtype) if df_vendas_limpas is not None else "")
# Saída esperada:
# Vendas Limpas Restantes: 5 linhas
# Tipo da Data Compra: datetime64[ns] (ou similar contendo datetime)
print("=" * 65)


### Fase 3: Enriquecimento e Cruzamento (Transform - Parte 2)
# Cenário: Para gerar inteligência de negócio, precisamos cruzar os dados de vendas com os clientes.
# 1. Realize uma junção à esquerda (Left Join) entre 'df_vendas_limpas' e 'df_clientes_raw'
#    usando a chave comum 'cliente_id'.
# 2. Crie uma nova coluna chamada 'ano_compra' contendo o ano extraído da coluna 'data_compra'.
# 3. Armazene o DataFrame final consolidado em 'df_consolidado'.
df_consolidado = None

# Espaço para resolução da Fase 3:


print("Fase 3 - Colunas Consolidadas:", list(df_consolidado.columns) if df_consolidado is not None else [])
print("Fase 3 - Total de Linhas Consolidadas:", len(df_consolidado) if df_consolidado is not None else 0)
# Saída esperada:
# Colunas Consolidadas: ['transacao_id', 'cliente_id', 'valor', 'data_compra', 'cupom', 'nome_cliente', 'estado', 'ano_compra']
# Total de Linhas Consolidadas: 5
print("=" * 65)


### Fase 4: Carga no Banco e Log de Auditoria (Load)
# Cenário: Os dados tratados devem ser persistidos no banco de dados analítico e a operação registrada em log.
# 1. Crie uma conexão SQLite apontando para o arquivo "armazem_dados.db" na variável 'conexao_dw'.
# 2. Salve 'df_consolidado' dentro da tabela 'faturamento_analitico' usando o método '.to_sql()'
#    do próprio Pandas (com if_exists="replace" e index=False).
# 3. Confirme que a tabela foi gravada consultando o total de linhas com SQL
#    armazenando o resultado na variável 'total_gravado_banco' (int).
# 4. Registre uma linha de auditoria no arquivo "etl_execucao.log" contendo a mensagem:
#    "SUCESSO: Pipeline executado com X registros carregados." (substituindo X pelo total de registros).
conexao_dw = None
total_gravado_banco = 0

# Espaço para resolução da Fase 4:


print(f"Fase 4 - Registros Gravados no Banco SQLite: {total_gravado_banco}")
# Saída esperada:
# Registros Gravados no Banco SQLite: 5
print("=" * 65)

# Fechamento seguro
if conexao_dw is not None:
    conexao_dw.close()
