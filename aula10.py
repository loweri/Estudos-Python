### K1
servidor = {"ip": "192.168.2.50", "porta": 8080, "ativo": True, "requisicoes": 300}
ip_rqst = servidor["ip"]
print(f"Imprimindo o IP ...\nIP: {ip_rqst}")
print("-" * 25)
print(f"Ativo, antes: {servidor["ativo"]}")
servidor["ativo"] = False
print(f"Ativo, depois: {servidor["ativo"]}")
print("-" * 25)
print(f"Número atual de requisições: {servidor["requisicoes"]}\nCarregando nova requisição ...")
servidor["requisicoes"] += 150
print(f"Novo número de requisições: {servidor["requisicoes"]}")
print("-" * 25)
print(f"Carregando dicionário...\n{servidor}\nRequisição concluida com sucesso.")
print("=" * 45)
### k2
# Acesso DEfensivo em APIs
payload_api = {"transacao_id": 9841, "moeda": "BRL"}
if "valor" in payload_api:
    print(f"O valor da API é: {payload_api["valor"]}")
else:
    print(f"Alerta: campo ausente")
print("-" * 25)
taxa_aplicada = payload_api.get("taxa", 0.0)
print(f"Taxa aplicada: {taxa_aplicada}")
print("=" * 45)
### k3
# Metadados dee Tabela (CRUD: Inserção, Atualização e Deleção /// Creat, Read, Update, Delete)
# Criar um dicionário chamado tabela_dw
tabela_dw = {"nome": "fator_vendas", "linhas": 250000, "formato": "csv"}
print(f"Tabela atual: {tabela_dw}")
print("-" * 25)
tabela_dw["particionada"] = True
print(f"Teste de particionamento adicionado:\n{tabela_dw}")
print("-" * 25)
tabela_dw["formato"] = "parquet"
print(f"Alteração de formato:\n{tabela_dw}")
print("-" * 25)
linhas_antigas = tabela_dw.pop("linhas")
print(f"Remoção de 'linhas':\n{tabela_dw}")
print("-" * 25)
print(f"Removidos:\n{linhas_antigas}")
print("=" * 45)
### k4
# A Triade de Inspeção (".keys(), .values(), .items()")
config_bd = {"host": "db.datacenter.internal", "porta": 5432, "banco": "analytics", "usuario": "etl_service"}
print(f"Lista nomeando as chaves:")
for key_names in config_bd.keys():
    print(f"{key_names}")
print("-" * 25)
print(f"Somente os valores:")
for values in config_bd.values():
    print(f"{values}")
print("-" * 25)
print(f"Completo em dicionário:")
for chave, valor in config_bd.items():
    print(f"Chave/Valor: {chave}:{valor} ")
print("=" * 45)
#### k5
# O contador de ocorrências
logs_http = ["200", "404", "200", "500", "200", "404", "200", "301", "500", "200"]
def analisar_frequencia(lista_logs):
    contagem = {}
    for status in lista_logs:
        if status in contagem:
            contagem[status] += 1
        else:
            contagem[status] = 1
    return contagem
resultado = analisar_frequencia(logs_http)
print(f"Resultado:\n{resultado}")