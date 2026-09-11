"""
PROJETO DE CONSOLIDAÇÃO - MÓDULO 2.3 (DICIONÁRIOS)
Pipeline de Ingestão e Agregação de Telemetria de E-commerce

Objetivo:
Construir uma esteira de dados completa aplicando:
- Filtragem e higienização de payloads brutos
- De-Para de status com fallback seguro
- Agrupador de métricas analíticas por canal de pagamento
"""

transacoes_brutas = [
    {"id": 1001, "cliente": "Ana",     "canal": "PIX",     "valor": 150.0,  "status_cod": "AP"},
    {"id": 1002, "cliente": "Bruno",   "canal": "CREDITO", "valor": 320.0,  "status_cod": "AP"},
    {"id": 1003, "cliente": "Carlos",  "canal": "BOLETO",  "valor": -50.0,  "status_cod": "AP"},   # ⚠️ Valor corrompido
    {"id": 1004, "cliente": "",        "canal": "PIX",     "valor": 80.0,   "status_cod": "AP"},   # ⚠️ Cliente vazio
    {"id": 1005, "cliente": "Daniela", "canal": "PIX",     "valor": 200.0,  "status_cod": "AP"},
    {"id": 1006, "cliente": "Eduardo", "canal": "CREDITO", "valor": 450.0,  "status_cod": "RJ"},   # ⚠️ Rejeitado
    {"id": 1007, "cliente": "Fernanda","canal": "CREDITO", "valor": 120.0,  "status_cod": "XPTO"}, # ⚠️ Código desconhecido
    {"id": 1008, "cliente": "Gabriel", "canal": "BOLETO",  "valor": 90.0,   "status_cod": "AP"},
    {"id": 1009, "cliente": "Helena",  "canal": "PIX",     "valor": 310.0,  "status_cod": "AP"}
]

mapa_status = {
    "AP": "Aprovado",
    "RJ": "Rejeitado"
}

# =================================================================
# SAÍDA FINAL ESPERADA DO PIPELINE:
#
# Transações Válidas Enriquecidas:
# (Lista contendo apenas as transações válidas com status traduzido)
#
# Métricas Consolidadas por Canal (Apenas Aprovados):
# {
#     'PIX': {'faturamento': 660.0, 'pedidos': 3},
#     'CREDITO': {'faturamento': 320.0, 'pedidos': 1},
#     'BOLETO': {'faturamento': 90.0, 'pedidos': 1}
# }
# =================================================================

# Escreva seu pipeline a partir daqui:
transacoes_validas = []
metricas_por_canal = {}
for transacao in transacoes_brutas:
    idhold = transacao["id"]
    status_codhold = transacao["status_cod"]
    clientehold = transacao["cliente"]
    valorhold = transacao["valor"]
    canalhold = transacao["canal"]
    if clientehold == "" or valorhold <= 0:
        continue
    statusmap = mapa_status.get(status_codhold, "Em analise")
    novastransacoes = {
        "id": idhold,
        "cliente": clientehold,
        "canal": canalhold,
        "valor": valorhold,
        "status_cod": statusmap
        }
    transacoes_validas.append(novastransacoes)
    if statusmap == "Aprovado":
        if canalhold in metricas_por_canal:
            metricas_por_canal[canalhold]["faturamento"] += valorhold
            metricas_por_canal[canalhold]["pedidos"] += 1
        else:
            metricas_por_canal[canalhold] = {
                "faturamento": valorhold,
                "pedidos": 1
                }
print(transacoes_validas)
print(metricas_por_canal)