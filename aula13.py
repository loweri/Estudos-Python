"""
MÓDULO 3.2: MANIPULAÇÃO DE ARQUIVOS E FORMATOS REAIS DE DADOS (I/O, CSV, JSON)
Objetivo: Leitura, escrita e serialização resiliente de dados em disco.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

import os
import csv
import json

print("=" * 65)

### Kata 1: Escrita e Leitura de Arquivo Texto (TXT)
# Cenário: Uma rotina de infraestrutura precisa salvar a lista de 'servidores_iniciais'
# no arquivo 'servidores.txt' (um servidor por linha).
# Em seguida, abra o mesmo arquivo em modo leitura, leia todas as linhas e guarde
# cada nome (removendo a quebra de linha '\n') na lista 'servidores_lidos'.
# Dados de entrada:
servidores_iniciais = ["srv-prod-01", "srv-prod-02", "srv-db-master", "srv-cache-01"]
arquivo_k1 = "servidores.txt"
servidores_lidos = []

# Espaço para resolução:


print("K1 - Servidores Lidos:", servidores_lidos)
# Saída esperada: ['srv-prod-01', 'srv-prod-02', 'srv-db-master', 'srv-cache-01']
print("=" * 65)


### Kata 2: Persistência Cumulativa / Modo Anexação (Append)
# Cenário: Um arquivo de log 'acessos.log' já existe com registros prévios.
# 1. Crie o arquivo 'acessos.log' escrevendo os itens de 'logs_iniciais' (um por linha).
# 2. Em uma segunda operação, abra o mesmo arquivo em modo de anexação e adicione os itens de 'novos_logs'.
# 3. Por fim, leia todas as linhas do arquivo e armazene na lista 'todos_logs' (sem quebras de linha '\n').
# Dados de entrada:
arquivo_k2 = "acessos.log"
logs_iniciais = ["USER_LOGIN:1001", "QUERY_RUN:1001"]
novos_logs = ["EXPORT_DATA:1001", "USER_LOGOUT:1001"]
todos_logs = []

# Espaço para resolução:


print("K2 - Todos os Logs:", todos_logs)
# Saída esperada: ['USER_LOGIN:1001', 'QUERY_RUN:1001', 'EXPORT_DATA:1001', 'USER_LOGOUT:1001']
print("=" * 65)


### Kata 3: Ingestão de Dados Tabulares (CSV)
# Cenário: Um arquivo tabular 'sensores_estacao.csv' foi gerado por medidores climáticos.
# O arquivo deve conter cabeçalho: "sensor_id,temperatura,status"
# e as linhas de dados fornecidas em 'dados_sensores'.
# 1. Grave o arquivo 'sensores_estacao.csv' com o cabeçalho e os dados.
# 2. Em seguida, leia o arquivo e armazene em 'sensores_validos' apenas os dicionários ou registros
# cuja temperatura numérica seja superior a 25.0.
# Dados de entrada:
arquivo_k3 = "sensores_estacao.csv"
dados_sensores = [
    ["S01", "24.5", "ATIVO"],
    ["S02", "28.1", "ATIVO"],
    ["S03", "31.4", "ALERTA"],
    ["S04", "21.0", "STANDBY"]
]
sensores_validos = []

# Espaço para resolução:


print("K3 - Sensores Válidos (> 25.0):", sensores_validos)
# Saída esperada (lista de ids dos sensores válidos ou registros):
# ['S02', 'S03']
print("=" * 65)


### Kata 4: Serialização e Desserialização de Configurações (JSON)
# Cenário: Uma esteira de ingestão consome parâmetros de conexão em formato JSON.
# 1. Salve o dicionário 'pipeline_config' no arquivo 'config_pipeline.json' de forma legível (com indentação).
# 2. Leia o arquivo 'config_pipeline.json' de volta para a variável 'config_carregada'.
# 3. Verifique se o valor da chave 'database' na seção 'parametros' corresponde a "dw_production".
# Guarde esse valor na variável 'banco_conectado'.
# Dados de entrada:
arquivo_k4 = "config_pipeline.json"
pipeline_config = {
    "versao": "2.1.0",
    "esteira": "ingestao_financeira",
    "parametros": {
        "database": "dw_production",
        "porta": 5432,
        "ssl": True
    }
}
config_carregada = {}
banco_conectado = ""

# Espaço para resolução:


print("K4 - Banco Conectado:", banco_conectado)
# Saída esperada: "dw_production"
print("=" * 65)


### Kata 5: Ingestão Resiliente de Arquivo Inexistente (FileNotFoundError)
# Cenário: Uma função 'carregar_tabela_segura(caminho_arquivo)' tenta ler o conteúdo de um arquivo.
# - Se o arquivo existir, leia todas as linhas e retorne a lista de linhas.
# - Se o arquivo NÃO existir (FileNotFoundError), capture a exceção e retorne a lista vazia [].
# Fora da função, teste chamando carregar_tabela_segura('arquivo_fantasma.txt') e armazene
# o resultado na variável 'resultado_carga'.
arquivo_k5_teste = "arquivo_fantasma.txt"
resultado_carga = None

def carregar_tabela_segura(caminho_arquivo):
    pass

# Espaço para chamada da função:


print("K5 - Resultado Carga Segura:", resultado_carga)
# Saída esperada: []
print("=" * 65)
