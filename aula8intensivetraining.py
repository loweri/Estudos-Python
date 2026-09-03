#Bateria de Katas
# 1.8.1:
# Rastreador de Histórico de navegação
sitesacessados = ["google.com","github.com","stackoverflow.com","linkedin.com"]
paginafechada = sitesacessados.pop()
print(f"Última página fechada: {paginafechada}.\nHistórico de navegação: {sitesacessados}")
print("-" * 50)
###
# 1.8.2:
# Controle de Estoque
deposito = ["Parafuso","Prego","Porca","Arruela","Prego"]
compra1 = deposito.remove("Prego")
print(f"Lista atualizada: {deposito}")
print("-" * 50)
###
# 1.8.3
# Fatiamento de Turnos de Trabalho
turnos = ["T1","T2","T3","T4","T5","T6"]
turnomanha = turnos[0:3]
turnonoite = turnos[3:6]
print(f"Turno Matinal: {turnomanha}\nTurno Noturno: {turnonoite}")
print("-" * 50)
###
# 1.8.4
# Pódio de corrida
pilotos = ["Hamilton","Verstappen","Leclerc","Norris","Alonso"]
podio = pilotos[0] +",  "+ pilotos[1] +", "+ pilotos[-1]
print(f"Pódio atual + último: {podio}")
print("-" * 50)
###
# 1.8.5
# Cancelamento de Compra
itens_compra = ["Notebook","Mochila","Mousepad"]
qtd_itens = len(itens_compra)
print(f"Quantos itens há no carrinho: {qtd_itens}")
itens_compra.clear()
novaqtd_itens = len(itens_compra)
print(f"Carrinho vazio, itens no carrinho: {novaqtd_itens}")
print("-" * 50)
###
# 1.8.6
# Filtro de Alunos Aprovados
notas = [8.5,4.0,7.0,5.5,9.0,3.2,6.0]
aprovados = []
for n in notas:
    if n >= 6.0:
        aprovados.append(n)
        aprovados.sort()
print(f"Alunos aprovados: {aprovados}")
print("-" * 50)
###
# sessão extra pra treinar listas e adicionar em listas: 
# extra 1: Filtro de palavras curtas
palavras = ["sol","lua","computador","mar","elefante","pão"]
palavras_curtas = []
for p in palavras:
    if len(p) < 5:
        palavras_curtas.append(p)
print(f"Nova lista com as palavras curtas:\n{palavras_curtas}")
print("-" * 50)
###
# extra 2: Extrator de Saldos Positivos (Bancário)
movimentacoes = [150.0, -50.0, 300.0, -120.0, 90.0, -10.0]
entradas_positivas = []
for m in movimentacoes:
    if m > 0:
        entradas_positivas.append(m)
        entradas_positivas.sort()
print(f"Movimentações positivas em ordem crescente:\n{entradas_positivas}")
print("-" * 50)
###
# extra 3: Coletor de Quadrados de Números
valores = [2,4,6,8,10]
quadrados = []
for v in valores:
    v = v ** 2
    quadrados.append(v)
print(f"Valores quadrados:\n{quadrados}")
print("-" * 50)
###
# extra 4: Alerta de Estoque Baixo
quantidades = [15,3,28,8,2,40]
estoque_critico = []
for q in quantidades:
    if q < 10:
        estoque_critico.append(q)
        estoque_critico.sort()
print(f"Produtos em estoque crítico:\n{estoque_critico}")
print("-" * 50)
###
# extra 5:
nomes = ["marcos","aline","rodrigo","luciana"]
emails_gerados = []
for n in nomes:
    n = n + "@empresa.com.br"
    emails_gerados.append(n)
print(f"Lista de emails:\n{emails_gerados[0]}\n{emails_gerados[1]}\n{emails_gerados[2]}\n{emails_gerados[3]}")
print("-" * 50)
###
# 1.8.7 - Segregador de Pares e ìmpares
numeros = [12, 7, 19, 24, 8, 3, 30, 41, 50]
pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
        pares.sort()
    else:
        impares.append(n)
        impares.sort()
print(f"Lista de Pares:\n{pares}\nLista de Ímpares:\n{impares}")
print("-" * 50)
###
# 1.8.8 - Portaria de Evento VIP
vip = ["Alice", "Bob", "Carlos", "Diana"]
def verificar_lista(nome,listavip):
    if nome in vip:
        return("Entrada Liberada")
    else:
        return("Entrada Negada")
teste1 = verificar_lista("Carlos",vip)
teste2 = verificar_lista("Marcos",vip)
print(f"Teste 1: {teste1}\nTeste 2: {teste2}")
print("-" * 50)
###
# 1.8.9 - Urna de Votação
votos = ["A", "B", "A", "A", "C", "B", "A", "C", "A"]
v = votos.count("A")
print(f"Quantidade de votos no A: {v}")
print("-" * 50)
###
# 1.8.10 - Atualização cadastral
emails = ["joao@empresa.com", "maria@empresa.com", "antigo@empresa.com"]
emails[2] = "carlos@empresa.com"
print(f"Nova lista: {emails}")
print("-" * 50)
###
# 1.8.11 - Média de Despesas
def media_despesas(lista_gastos):
    v_sum = sum(lista_gastos)
    v_avg = v_sum / len(lista_gastos)
    return v_avg
lista1 = [150.0, 300.0, 450.0, 100.0]
resultadoavg = media_despesas(lista1)
print(f"Resultado: {resultadoavg}")
print("-" * 50)
###
# 1.8.12 - Maior Temperatura na Raça
temperaturas = [28, 35, 19, 41, 32, 25]
maior = temperaturas[0]
for temp in temperaturas:
    if temp > maior:
        maior = temp
print(f"Resultado: {maior}")
print("-" * 50)
###
# 1.8.13 - Reajuste de Tabela de Preços
precos_antigos = [10.0, 20.0, 50.0, 100.0]
pco_novos = []
for pca in precos_antigos:
    pca1 = round(pca * 1.10,2)
    pco_novos.append(pca1)
print(f"Lista com aumento: {pco_novos}")
print("-" * 50)
###
# 1.8.14 - Localizador de Parada na Rota
cidades = ["São Paulo", "Campinas", "Ribeirão Preto", "Uberlândia"]
pos = cidades.index("Ribeirão Preto")
print(f"Posição: {pos}")
print("-" * 50)
###
fila_tarefas = ["Backup", "Relatório", "Limpeza", "Deploy"]
fila_tarefas.reverse()
print(f"Fila nova: {fila_tarefas}")