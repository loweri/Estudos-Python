### k1 De-Para de Siglasa de estados
estados = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Minas Gerais"}
usuarios = [
    {"nome": "Ana", "uf": "SP"},
    {"nome": "Beto", "uf": "MG"},
    {"nome": "Caio", "uf": "RJ"}
]
usuarios_completos = []
for ufint in usuarios:
    nome_t1 = ufint["nome"]
    uf_t1 = ufint["uf"]
    novo_uf = estados[uf_t1]
    novo_reg_uf = {"nome": nome_t1, "uf":novo_uf}
    usuarios_completos.append(novo_reg_uf)
print(f"Teste1: {usuarios_completos}")
print("=" * 55)
### k2 De-Para Numérico de Prioridades
pesos = {"ALTA": 10, "MEDIA": 5, "BAIXA": 1}
chamados = [
    {"ticket": 101, "prioridade": "ALTA"},
    {"ticket": 102, "prioridade": "BAIXA"},
    {"ticket": 103, "prioridade": "MEDIA"}
]
chamados_pesados = []
for chamado in chamados:
    ticket_k2 = chamado["ticket"]
    prioridade_k2 = chamado["prioridade"]
    pesok2 = pesos[prioridade_k2]
    novo_chamado_completo = {"ticket": ticket_k2, "prioridade": prioridade_k2, "peso": pesok2}
    chamados_pesados.append((novo_chamado_completo))
print(chamados_pesados)
print("=" * 55)
### k3 Acesso profundo em dicionário aninhado
empresa = {
    "departamento": {
        "engenharia": {
            "lider": "Paula",
            "equipe": 12
        }
    }
}
novoacessoliderk3 = empresa["departamento"]["engenharia"]["lider"]
novoacessoequipek3 = empresa["departamento"]["engenharia"]["equipe"]
print(novoacessoliderk3, novoacessoequipek3)
print("=" * 55)
### k4 Atualização direta de dicionário aninhado
servidor = {
    "hardware": {
        "ram_gb": 16,
        "ssd_gb": 512
    }
}
servidor["hardware"]["ram_gb"] = 32
servidor["hardware"]["ssd_gb"] = 1024
servidor_att = servidor["hardware"]
servidor_att["ssd_gb"] = 2048
servidor_att["ram_gb"] = 64
print(servidor)
print("=" * 55)
### k5 Agrupador de pontor por time
partidas = [
    {"time": "Gryffindor", "pontos": 50},
    {"time": "Slytherin", "pontos": 30},
    {"time": "Gryffindor", "pontos": 100},
    {"time": "Ravenclaw", "pontos": 40},
    {"time": "Slytherin", "pontos": 70}
]
placar_total = {}
for placar in partidas:
    pontostotais = placar["pontos"]
    timetotal = placar["time"]
    if timetotal in placar_total:
        placar_total[timetotal] += pontostotais
    else:
        placar_total[timetotal] = pontostotais
print(placar_total)
print("=" * 55)
### k6 Agrupador de itens por categoria
produtos = [
    {"item": "Manga", "setor": "Hortifruti"},
    {"item": "Sabao", "setor": "Limpeza"},
    {"item": "Banana", "setor": "Hortifruti"},
    {"item": "Detergente", "setor": "Limpeza"}
]
itens_por_setor = {}
for produto in produtos:
    itemk6 = produto["item"]
    setork6 = produto["setor"]
    if setork6 in itens_por_setor:
        itens_por_setor[setork6].append(itemk6)
    else:
        itens_por_setor[setork6] = [itemk6]
print(itens_por_setor)
print("=" * 55)
### k7 Inversor de dicionário
moedas = {"USD": "Dolar", "BRL": "Real", "EUR": "Euro"}
moedas_invertidas = {}
for moeda, troca in moedas.items():
    moedas_invertidas[troca] = moeda
print(moedas_invertidas)
print("=" * 55)
### k8 Filtro duplo de status
inscricoes = {
    "user1": "Aprovado",
    "user2": "Pendente",
    "user3": "Reprovado",
    "user4": "Pendente",
    "user5": "Aprovado"
}
inscricoes_revisadas = {}
for inscricao, estado in inscricoes.items():
    if estado == "Pendente":
        continue
    elif estado == "Reprovado":
        continue
    else:
        inscricoes_revisadas[inscricao] = estado
print(inscricoes_revisadas)
print("=" * 55)
### k9 Extração de chaves com condicional
registros = [
    {"id": 1, "email": "a@test.com", "ativo": True},
    {"id": 2, "email": "b@test.com", "ativo": False},
    {"id": 3, "email": "c@test.com", "ativo": True}
]
emails_ativos = []
for registro in registros:
    idguardado = registro["id"]
    emailguardado = registro["email"]
    estadoguardado = registro["ativo"]
    if estadoguardado == False:
        continue
    else:
        emails_ativos.append(emailguardado)
print(emails_ativos)
print("=" * 55)
### k10 Contador de letras de uma palavra
palavra = "engenharia"
frequencia_letras = {}
for letra in palavra:
    if letra in frequencia_letras:
        frequencia_letras[letra] += 1
    else:
        frequencia_letras[letra] = 1
print(frequencia_letras)