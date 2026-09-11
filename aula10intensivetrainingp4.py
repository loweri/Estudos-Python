### k1 Agrupador de valores por tipo
transacoes = [
    {"id": 1, "tipo": "PIX", "valor": 100.0},
    {"id": 2, "tipo": "CREDITO", "valor": 250.0},
    {"id": 3, "tipo": "PIX", "valor": 40.0},
    {"id": 4, "tipo": "BOLETO", "valor": 80.0},
    {"id": 5, "tipo": "CREDITO", "valor": 120.0}
]
valores_por_tipo = {}
for transacao in transacoes:
    idkeep = transacao["id"]
    tipokeep = transacao["tipo"]
    valorkeep = transacao["valor"]
    if tipokeep in valores_por_tipo:
        valores_por_tipo[tipokeep].append(valorkeep)
    else:
        valores_por_tipo[tipokeep] = [valorkeep]
print(valores_por_tipo)
print("=" * 65)
### k2 Agrupador de Cidades por Estado
cadastros = [
    {"cidade": "Campinas", "uf": "SP"},
    {"cidade": "Niteroi", "uf": "RJ"},
    {"cidade": "Santos", "uf": "SP"},
    {"cidade": "Belo Horizonte", "uf": "MG"},
    {"cidade": "Petropolis", "uf": "RJ"}
]
cidadesporuf = {}
for cadastro in cadastros:
    cidadekeep = cadastro["cidade"]
    ufkeep = cadastro["uf"]
    if ufkeep in cidadesporuf:
        cidadesporuf[ufkeep].append(cidadekeep)
    else:
        cidadesporuf[ufkeep] = [cidadekeep]
print(cidadesporuf)
print("=" * 65)
### k3 Mutação direta de 3 niveis
infra = {
    "banco": {
        "conexao": {
            "pool_max": 10,
            "timeout_sec": 30
        }
    }
}
infra["banco"]["conexao"]["pool_max"] = 20
infra["banco"]["conexao"]["timeout_sec"] = 60
print((infra))
print("=" * 65)
### k4 Inserção de enova chave em dicionário aninhado
usuario = {
    "id": 99,
    "preferencias": {
        "tema": "dark",
        "notificacoes": True
    }
}
usuario["preferencias"]["idioma"] = "pt-BR"
print(usuario)
print("=" * 65)
### k5 Incremento de Métrica Aninhada
servico = {
    "nome": "auth_api",
    "metricas": {
        "requisicoes_total": 1500,
        "erros_500": 12
    }
}
servico["metricas"]["requisicoes_total"] += 500
servico["metricas"]["erros_500"] += 3
print(servico)
print("=" * 65)
### k6 De-Para com Tratamento de código inexistente
mapa_status = {"A": "Aprovado", "R": "Rejeitado", "P": "Pendente"}
pedidos = [
    {"id": 101, "status_cod": "A"},
    {"id": 102, "status_cod": "X"},
    {"id": 103, "status_cod": "R"}
]
pedidos_revisados = []
for pedido in pedidos:
    id6 = pedido["id"]
    status6 = pedido["status_cod"]
    novostatus = mapa_status.get(status6, "Desconhecido")
    pedidos_revisados.append({"id": id6, "status_cod": novostatus})
print(pedidos_revisados)
print("=" * 65)
### k7 Agrupador com Dupla Métrica (Soma e Quantidade)
vendas = [
    {"vendedor": "Carla", "valor": 100.0},
    {"vendedor": "Bruno", "valor": 200.0},
    {"vendedor": "Carla", "valor": 150.0}
]
resumo_vendedores = {}
for venda in vendas:
    vendedork7 = venda["vendedor"]
    valork7 = venda["valor"]
    if vendedork7 in resumo_vendedores:
        resumo_vendedores[vendedork7]["total"] += valork7
        resumo_vendedores[vendedork7]["qtd"] += 1
    else:
        resumo_vendedores[vendedork7] = {"total": valork7, "qtd": 1}
print(resumo_vendedores)
print("=" * 65)

### k8 Agrupador Financeiro Acumulado
# Cenário: Consolidar o total gasto por categoria financeira.
# Saída esperada: {'Limpeza': 200.0, 'Alimentos': 500.0, 'Bebidas': 95.0}
despesas = [
    {"categoria": "Limpeza", "valor": 120.0},
    {"categoria": "Alimentos", "valor": 350.0},
    {"categoria": "Limpeza", "valor": 80.0},
    {"categoria": "Bebidas", "valor": 95.0},
    {"categoria": "Alimentos", "valor": 150.0}
]
gastos_por_categoria = {}
for despesa in despesas:
    categoriak8 = despesa["categoria"]
    valork8 = despesa["valor"]
    if categoriak8 in gastos_por_categoria:
        gastos_por_categoria[categoriak8] += valork8
    else:
        gastos_por_categoria[categoriak8] = valork8
print(gastos_por_categoria)

print("=" * 65)

### k9 Filtro e Extração em Lista de Dicionários
# Cenário: Filtrar apenas os nomes dos sensores cujo status 'valido' seja True.
# Saída esperada: ['s1', 's3', 's5']
sensores = [
    {"sensor": "s1", "valido": True},
    {"sensor": "s2", "valido": False},
    {"sensor": "s3", "valido": True},
    {"sensor": "s4", "valido": False},
    {"sensor": "s5", "valido": True}
]
sensores_ativos = []
for sensor in sensores:
    sensork9 = sensor["sensor"]
    validok9 = sensor["valido"]
    if validok9 == True:
        sensores_ativos.append(sensork9)
print(sensores_ativos)

print("=" * 65)

### k10 Inversor de Dicionário Agrupando em Lista
# Cenário: Inverter o mapeamento pessoa -> departamento para departamento -> lista de pessoas.
# Saída esperada: {'TI': ['Alice', 'Carlos'], 'RH': ['Bob', 'Diana']}
equipes = {
    "Alice": "TI",
    "Bob": "RH",
    "Carlos": "TI",
    "Diana": "RH"
}
pessoas_por_depto = {}
for chavek10, valork10 in equipes.items():
    if valork10 in pessoas_por_depto:
        pessoas_por_depto[valork10].append(chavek10)
    else:
        pessoas_por_depto[valork10] = [chavek10]
print(pessoas_por_depto)