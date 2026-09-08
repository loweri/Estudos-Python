### k1 - "O perfil de conexão com o data lake"
config_s3 = {
    "bucket": "raw-data-lake-financeiro", 
    "regiao": "sa-east-1",
    "timeout": 30,
    "criptografia": True,
    "prefixo": "telemetria/"
}
bucket = config_s3["bucket"]
regiao = config_s3["regiao"]
prefixo = config_s3["prefixo"]
criptografia = config_s3["criptografia"]
if criptografia == True:
    criptografia = str("Verdadeiro")
else:
    criptografia = str("Falso")
print(f"Conectado ao bucket {bucket} na região {regiao} com o prefixo {prefixo}")
print('-' * 25)
print(f"Criptografia habilitada: {criptografia}")
print("=" * 45)
### k2 - Schema Enforcement & Correção de Tipos
colunas_schema = {"id_transacao": "string", "valor": "string", "data_registro": "string"}
print(f"Original: \n{colunas_schema}")
print('-' * 25)
colunas_schema["valor"] = "float"
print(f"Alteração 01:\n{colunas_schema}")
print('-' * 25)
colunas_schema["score_fraude"] = "float"
print(f"Versão final:\n{colunas_schema}")
print('=' * 45)
### k3 - Blindagem de payload de webhook com fallbacks
evento_webhook = {"evento_id": "evt_9921", "cliente_id": 402, "valor": 890.50}
ip_origem_test = evento_webhook.get("ip_origem", "0.0.0.0")
tentativa_test = evento_webhook.get("tentativa", 1)
metodo_pgto_test = evento_webhook.get("metodo_pagamento","Desconhecido")
print(f"{tentativa_test} tentativas, ip de origem {ip_origem_test} e metodo de pagamento {metodo_pgto_test}")
print('=' * 45)
### k4 - Limpeza de cache de metadados
sessao_etl = {
    "job_name": "carga_diaria_vendas",
    "status": "running",
    "temp_file": "/tmp/stage_temp_9918.parquet",
    "retry_count": 0
}
print(f"Original:\n{sessao_etl}")
print('-' * 25)
arquivo_para_deletar = sessao_etl.pop("temp_file")
sessao_etl["status"] = "Completed"
sessao_etl["retry_count"] = 1
print(f"Novo:\n{sessao_etl}\nArquivo para deletar: {arquivo_para_deletar}")
print('=' * 45)
### k5 Inversor de dicionarios
rotas_iata = {"GRU": "São Paulo", "GIG": "Rio de Janeiro", "BSB": "Brasília", "SSA": "Salvador"}
rotas_por_cidade = {}
print(f"Antigo:\n{rotas_iata}")
print('-' * 25)
for rota, cidade in rotas_iata.items():
    rotas_por_cidade[cidade] = rota
print(f"Novo:\n{rotas_por_cidade}")
print('=' * 45)
### k6 Auditor de campos obrigatórios
# alternativa em comentario entre "===="
# == campos_faltantes = []
# == for campo in campos_obrigatorios:
# ==     if campo not in evento_iot:
# ==         campos_faltantes.append(campo)
# == print(f"Campos Faltantes pra auditoria: {campos_faltantes}")
evento_iot = {"dispositivo_id": "sensor_alpha_01", "temperatura": 36.8}
campos_obrigatorios = ["dispositivo_id", "timestamp", "temperatura", "bateria"]
ver_dispositivo = evento_iot.get("dispositivo_id", "Não há um evento chamado 'dispositivo_id'.")
ver_timestamp = evento_iot.get("timestamp", "Não há um evento chamado 'timestamp'.")
ver_temperatura = evento_iot.get("temperatura", "Não há um evento chamado 'temperatura'.")
ver_bateria = evento_iot.get("bateria", "Não há um evento chamado 'bateria'.")
print(
    f"Verificando se há os campos obrigatórios 'dispositivo_id', 'timestamp', 'temperatura', 'bateria'...\n"
    f"Dispositivo: {ver_dispositivo}\n"
    f"Timestamp: {ver_timestamp}\n"
    f"Temperatura: {ver_temperatura}\n"
    f"Bateria: {ver_bateria}\n"
    f"Campos faltantes: {ver_timestamp} e {ver_bateria}."
)
print('=' * 45)
### k7 Agrupador financeiro por moeda
transacoes = [
    {"id": 1, "moeda": "BRL", "valor": 120.0},
    {"id": 2, "moeda": "USD", "valor": 50.0},
    {"id": 3, "moeda": "BRL", "valor": 300.0},
    {"id": 4, "moeda": "EUR", "valor": 80.0},
    {"id": 5, "moeda": "USD", "valor": 150.0}
]
totais_por_moeda = {}
for item in transacoes:
    id_cpt = item["id"]
    moeda = item["moeda"]
    valor = item["valor"]
    if moeda in totais_por_moeda:
        totais_por_moeda[moeda] += valor
    else:
        totais_por_moeda[moeda] = valor
print(f"Total: {totais_por_moeda}")
print('=' * 45)
### k8 Mecanismo de upsert de config
config_padrao = {"threads": 4, "timeout": 60, "modo": "batch", "isolamento": True}
config_usuario = {"threads": 8, "modo": "streaming"}
config_final = {}
for chave8, valor8 in config_padrao.items():
    config_final[chave8] = valor8
for chave9, valor9 in config_usuario.items():
    config_final[chave9] = valor9
print(f"Config final: {config_final}")
print('=' * 45)
### k9 Alerta de Servidores Criticos
cluster_cpu = {
    "srv_prod_01": 45.2,
    "srv_prod_02": 88.5,
    "srv_prod_03": 92.0,
    "srv_prod_04": 61.3,
    "srv_prod_05": 82.1
}
servidores_criticos = {}
for chave10, valor10 in cluster_cpu.items():
    if valor10 > 80.0:
        servidores_criticos[chave10] = valor10
print(f"Servidores criticos: {servidores_criticos}")
print('=' * 45)
### k10 - Sanitização de payload
dados_cliente = {
    "id": 841,
    "nome": "Mariana Souza",
    "email": "mariana@email.com",
    "telefone": None,
    "empresa": "",
    "ativo": True,
    "observacoes": None
}
dados_limpos = {}
for chave11, valor11 in dados_cliente.items():
    if valor11 == None:
        continue
    elif valor11 == "":
        continue
    else:
        dados_limpos[chave11] = valor11
print(f"Dados limpos: {dados_limpos}")