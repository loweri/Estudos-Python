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
print("=" * 45)
### K17 Faturamento acumulado por departamento
itens_loja = [
    {"item": "Mouse", "preco": 80.0, "depto": "Informatica"},
    {"item": "Camisa", "preco": 50.0, "depto": "Vestuario"},
    {"item": "Teclado", "preco": 150.0, "depto": "Informatica"},
    {"item": "Tenis", "preco": 200.0, "depto": "Calcados"}
]
faturamento_dpto = {}
for ft_dpto in itens_loja:
    item17 = ft_dpto["item"]
    preco17 = ft_dpto["preco"]
    depto17 = ft_dpto["depto"]
    if depto17 in faturamento_dpto:
        faturamento_dpto[depto17] += preco17
    else:
        faturamento_dpto[depto17] = preco17
print(f"Teste17: {faturamento_dpto}")
print("=" * 45)
### K18 Inspeção de Cluster Aninhado
cluster_spark = {
    "cluster_id": "c-9914",
    "especificacoes": {
        "nos": 8,
        "memoria_gb": 64,
        "disco_tb": 2
    },
    "ambiente": "producao"
}
temp_espec = cluster_spark["especificacoes"]
temp_nos = temp_espec["nos"]
temp_memoriagb = temp_espec["memoria_gb"]
print(f"Teste18: Cluster c-9914 configurado com {temp_nos} nós e {temp_memoriagb}GB de memória no ambiente producao")
print("=" * 45)
### k19 Escalonamento de recursos
cluster_spark = {
    "cluster_id": "c-9914",
    "especificacoes": {
        "nos": 8,
        "memoria_gb": 64,
        "disco_tb": 2
    },
    "ambiente": "producao"
}
temp_espec19 = cluster_spark["especificacoes"]
temp_espec19["nos"] = 12
temp_espec19["memoria_gb"] = 128
print(f"{cluster_spark}")
print("=" * 45)
### k20 Pipeline De-Para
mapa_cargos = {
    "Estagiario": "NIVEL_1",
    "Junior": "NIVEL_2",
    "Pleno": "NIVEL_3",
    "Senior": "NIVEL_4"
}

colaboradores = [
    {"nome": "Lucas", "cargo": "Junior"},
    {"nome": "Beatriz", "cargo": "Senior"},
    {"nome": "Rodrigo", "cargo": "Pleno"},
    {"nome": "Camila", "cargo": "Junior"}
]
colaboradores_mascarados = []
for colab in colaboradores:
    nome_temp = colab["nome"]
    cargo_temp = colab["cargo"]
    novo_cargo = mapa_cargos[cargo_temp]
    novo_reg = {"nome": colab["nome"], "cargo": novo_cargo}
    colaboradores_mascarados.append(novo_reg)
print(f"Teste20: {colaboradores_mascarados}")