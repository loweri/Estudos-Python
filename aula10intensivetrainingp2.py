### k11 contador de severidade de logs
logs_sistema = ["INFO", "ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO", "DEBUG"]
contagem_logs = {}
for logs11 in logs_sistema:
    if logs11 in contagem_logs:
        contagem_logs[logs11] += 1
    else:
        contagem_logs[logs11] = 1
print(f"Contagem: {contagem_logs}")
print("=" * 45)
### k12 Mapeamento de schema de banco
tabela_schema = [
    {"nome": "id", "tipo": "int", "obrigatorio": True},
    {"nome": "email", "tipo": "string", "obrigatorio": True},
    {"nome": "idade", "tipo": "int", "obrigatorio": False},
    {"nome": "cidade", "tipo": "string", "obrigatorio": False}
]
tipos_colunas = {}
for n_column in tabela_schema:
    n_nome = n_column["nome"]
    n_tipo = n_column["tipo"]
    tipos_colunas[n_nome] = n_tipo
print(f"Teste12: {tipos_colunas}")
print("=" * 45)
### k13 filtro de campos mandatorios
tabela_schema = [
    {"nome": "id", "tipo": "int", "obrigatorio": True},
    {"nome": "email", "tipo": "string", "obrigatorio": True},
    {"nome": "idade", "tipo": "int", "obrigatorio": False},
    {"nome": "cidade", "tipo": "string", "obrigatorio": False}
]
colunas_obrigatorias = []
for n_columns in tabela_schema:
    n_stat = n_columns["obrigatorio"]
    n_column2 = n_columns["nome"]
    if n_stat == True:
        colunas_obrigatorias.append(n_column2)
print(f"Teste13: {colunas_obrigatorias}")
print("=" * 45)
### k14 monitor de latência de microsserviços
latencias_ms = {
    "auth_service": 120,
    "payment_service": 850,
    "catalog_service": 95,
    "notification_service": 450,
    "search_service": 620
}
servicos_lentos = {}
for key1, value1 in latencias_ms.items():
    if value1 > 400:
        servicos_lentos[key1] = value1
print(f"Teste14: {servicos_lentos}")
print("=" * 45)
### k15 Sanitização de questionário
respostas_survey = {
    "q1": "Excelente",
    "q2": "N/A",
    "q3": "Regular",
    "q4": "",
    "q5": "Bom",
    "q6": "N/A"
}
respostas_validas = {}
for key2, value2 in respostas_survey.items():
    if value2 == "N/A":
        continue
    elif value2 == "":
        continue
    else:
        respostas_validas[key2] = value2
print(f"Teste15: {respostas_validas}")
print("=" * 45)
### k16 Catálogo de Preços por Item
itens_loja = [
    {"item": "Mouse", "preco": 80.0, "depto": "Informatica"},
    {"item": "Camisa", "preco": 50.0, "depto": "Vestuario"},
    {"item": "Teclado", "preco": 150.0, "depto": "Informatica"},
    {"item": "Tenis", "preco": 200.0, "depto": "Calcados"}
]
catalogo_precos = {}
for catalog16 in itens_loja:
    item16 = catalog16["item"]
    preco16 = catalog16["preco"]
    dpto16 = catalog16["depto"]
    catalogo_precos[item16] = preco16
print(f"Teste16: {catalogo_precos}")