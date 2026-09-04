### 1.9.1 - Traçado de rota GPS de caminhão
origem = (-23.5505, -46.6333)
destino = (-22.9068, -43.1729)
lat1, long1 = origem
lat2, long2 = destino
print(f"Rota traçada, origem:\nLatitude: {lat1}\nLongitude: {long1}\nDestino:\nLatitude: {lat2}\nLongitude: {long2}")
print("=" * 45)
### 1.9.2
estados_lista = ["SP", "RJ", "MG"]
tp1 = tuple(estados_lista)
print(f"Lista convertida em tupla:\n{tp1}")
p1 = type(tp1)
print(f"Tipo: {p1}")
list1 = list(tp1)
list1.append("ES")
tp2 = tuple(list1)
print(f"Nova tupla:\n{tp2}")
print("=" * 45)
### 1.9.3
dias_uteis = ("Segunda", "Terca", "Quarta", "Quinta", "Sexta")
tam_dias = len(dias_uteis)
print(f"Tupla atual:\n{dias_uteis}\nTamanho:\n{tam_dias}")
print("Procurando ""Sábado"" na tupla ...")
if "Sábado" in dias_uteis:
    print("Está presente")
else:
    print("Não existe o dia procurado na lista")
print("\nProcurando ""Quarta"" na tupla ...")
if "Quarta" in dias_uteis:
    print("Está presente")
else:
    print("Não existe o dia procurado na lista")
print("\nFim das buscas.")
print("=" * 45)
### 1.9.4
semestre1 = ("Jan", "Fev", "Mar", "Abr", "Mai", "Jun")
mes1, mes2, mes3, *demais_meses = semestre1
prim_trim = mes1, mes2, mes3
segun_trim = tuple(demais_meses)
print(f"Primeiro trimestre:\n{prim_trim}\nSegundo trimestre:\n{segun_trim}")
print("=" * 45)
### 1.9.5
transacao = ("2026-09-04", 1500.50, "PIX", "Aprovada")
data, valor, tipo, status = transacao
print(f"As quatro partes, separadas:\nData: {data}\nValor: {valor}\nTipo: {tipo}\nEstado: {status}")
print("=" * 45)
### 1.9.6
x = "A"
y = "B"
z = "C"
x, y, z = y, z, x
print(f"Valores trocados:\n{x}\n{y}\n{z}")
print("=" * 45)
### 1.9.7
tempos = (9.58, 9.69, 9.75, 9.88, 9.93, 10.02)
t_ouro, t_prata, *t_restantes = tempos
print(f"Primeiro tempo: {t_ouro}\nSegundo tempo: {t_prata}\nDemais: {t_restantes}")
print("=" * 45)
### 1.9.8
anos = (2010, 2012, 2015, 2018, 2021, 2024, 2026)
ano_inicio, *outros_anos, ano_final = anos
inic_fim = ano_inicio, ano_final
print(f"Inicio e fim: {inic_fim}")
print("=" * 45)
### 1.9.9
avaliacoes = (5, 4, 5, 3, 5, 2, 4, 5, 1, 5)
av_tot = avaliacoes.count(5)
print(f"Total de vezes: {av_tot}")
pos2 = avaliacoes.index(1)
print(f"Posição do '1': {pos2}")
print("=" * 45)
### 1.9.10
def converter_moeda(valor_reais, taxa_dolar, taxa_euro):
    valor_dol = valor_reais * taxa_dolar
    valor_euro = valor_reais * taxa_euro
    return valor_dol, valor_euro
teste3 = converter_moeda(1000.00, 5.50, 6.00)
print(f"Conversão: {teste3}")
dol, eur = teste3
print(f"Valor convertido em dólar:\n{dol}\nValor convertido em euro:\n{eur}")
print("=" * 45)
### 1.9.11
def analisar_numeros(lista):
    min_valr = min(lista)
    max_valr = max(lista)
    avg_valr = sum(lista)/len(lista)
    return min_valr, max_valr, avg_valr
lista2 = [20, 50, 10, 80, 40]
teste5 = analisar_numeros(lista2)
menor1, maior1, media1 = teste5
print(f"Menor valor:\n{menor1}\nMaior valor:\n{maior1}\nMedia de valores:\n{media1}")
print("=" * 45)
### 1.9.12
remessas = [("Pacote_A", 12.5, 4), ("Pacote_B", 3.0, 1), ("Pacote_C", 25.0, 2)]
#(Cada tupla representa: identificador do pacote, peso em kg e prazo de entrega em dias).
#Regra de Negócio: O custo de envio de cada pacote é de R$ 15,00 por quilo.
for id_pack, peso_pack, prazo_pack in remessas:
    frete = peso_pack * 15
    print(f"Relatório formatado:\nIdentificador do pacote: {id_pack}\nPrazo do pacote: {prazo_pack}\nValor final com frete: {frete:.2f}\n{"-" * 35}")
print("=" * 45)
### 1.9.13
remessas = [("Pacote_A", 12.5, 4), ("Pacote_B", 3.0, 1), ("Pacote_C", 25.0, 2)]
cargas_pesadas = []
for id_pack, peso_pack, prazo_pack in remessas:
    if peso_pack > 10.0:
        carga_pesadona = id_pack, peso_pack, prazo_pack
        cargas_pesadas.append(carga_pesadona)
print(f"{cargas_pesadas}")
print("=" * 45)
### 1.9.14
setores = ["Platea", "Camarote", "Balcao"]
filas = [1, 2, 3, 4]
Mapa_assentos = []
for setor in setores:
    for fila in filas:
        tp3 = setor, fila
        Mapa_assentos.append(tp3)
print(Mapa_assentos)