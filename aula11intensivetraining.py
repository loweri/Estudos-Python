"""
TREINO INTENSIVO - MÓDULO 2.4: CONJUNTOS (set)
10 Katas de Engenharia de Dados & Resolução de Problemas Reais
"""

print("=" * 65)
### Kata 1: Validação de Contrato de Dados (Schema Drift)
# Cenário: Uma nova versão de API enviou um lote de dados. Identifique quais colunas
# obrigatórias do contrato ficaram FALTANDO no lote recebido.
# Saída esperada: {'origem', 'timestamp'} (ordem pode variar)
colunas_obrigatorias = {"id", "timestamp", "valor", "cliente", "origem"}
colunas_recebidas = {"id", "valor", "cliente", "ip"}
colunas_faltantes = None
colunas_faltantes = colunas_obrigatorias - colunas_recebidas
print("K1 - Colunas faltantes:", colunas_faltantes)
print("=" * 65)

### Kata 2: Detecção de Churn (Contas Canceladas)
# Cenário: Comparar a base de assinantes ativos de Janeiro com a de Fevereiro.
# Identifique quais usuários cancelaram a assinatura (estavam ativos em Janeiro, mas não constam em Fevereiro).
# Saída esperada: {'usr_1', 'usr_4'}
assinantes_jan = {"usr_1", "usr_2", "usr_3", "usr_4", "usr_5"}
assinantes_fev = {"usr_2", "usr_3", "usr_5", "usr_6"}
cancelados = None
cancelados = assinantes_jan - assinantes_fev
print("K2 - Cancelados:", cancelados)
print("=" * 65)

### Kata 3: Novos Clientes (Aquisição de Safra)
# Cenário: Usando as mesmas bases do Kata 2, identifique quem são os clientes recém-adquiridos
# (entraram em Fevereiro, mas não existiam em Janeiro).
# Saída esperada: {'usr_6'}
novos_clientes = None
novos_clientes = assinantes_fev - assinantes_jan
print("K3 - Novos clientes:", novos_clientes)
print("=" * 65)

### Kata 4: Público Alvo de Campanha Cruzada
# Cenário: O time de marketing precisa disparar uma campanha exclusiva apenas para
# os usuários que compraram produtos na categoria 'eletronicos' E TAMBÉM na categoria 'games'.
# Saída esperada: {'u20', 'u40'}
compradores_eletronicos = {"u10", "u20", "u30", "u40"}
compradores_games = {"u20", "u40", "u50", "u60"}
publico_campanha = None
publico_campanha = compradores_games & compradores_eletronicos

print("K4 - Público VIP:", publico_campanha)
print("=" * 65)

### Kata 5: Consolidação de Catálogos de Fornecedores
# Cenário: Dois fornecedores de peças automotivas enviaram suas listas de SKUs disponíveis.
# Consolide em uma única coleção todos os códigos de peças disponíveis em estoque, eliminando duplicatas.
# Saída esperada: {'SKU-A1', 'SKU-B2', 'SKU-C3', 'SKU-D4', 'SKU-E5'}
catalogo_fornecedor_a = {"SKU-A1", "SKU-B2", "SKU-C3"}
catalogo_fornecedor_b = {"SKU-B2", "SKU-C3", "SKU-D4", "SKU-E5"}
catalogo_consolidado = None
catalogo_consolidado = catalogo_fornecedor_a | catalogo_fornecedor_b

print("K5 - Catálogo consolidado:", catalogo_consolidado)
print("=" * 65)

### Kata 6: Auditoria de Replicação em Banco Distribuído
# Cenário: Dois nós de banco de dados (Node Alpha e Node Beta) sincronizam transações.
# Identifique todas as transações que estão presentes em apenas UM dos nós (ou seja,
# transações que não estão sincronizadas em ambos os lados).
# Saída esperada: {'tx100', 'tx103', 'tx104'}
node_alpha = {"tx100", "tx101", "tx102", "tx103"}
node_beta = {"tx101", "tx102", "tx104"}
transacoes_dessincronizadas = None
transacoes_dessincronizadas = node_alpha ^ node_beta

print("K6 - Dessincronizadas:", transacoes_dessincronizadas)
print("=" * 65)

### Kata 7: Cardinalidade de Tráfego (Visitantes Únicos)
# Cenário: Um log de acessos registrou uma sequência de requisições de IPs.
# Calcule a QUANTIDADE TOTAL de visitantes únicos que acessaram o portal.
# Saída esperada: 4 (número inteiro)
ip_logs = [
    "192.168.0.1", "10.0.0.1", "192.168.0.1", "172.16.0.1",
    "10.0.0.1", "192.168.0.2", "192.168.0.1"
]
total_visitantes_unicos = None
total_visitantes_unicos = set(ip_logs)
total_visitantes_unicos = len(total_visitantes_unicos)
print("K7 - Total visitantes únicos:", total_visitantes_unicos)
print("=" * 65)

### Kata 8: Filtro de Alta Performance em Streaming
# Cenário: Em uma esteira de eventos, filtre a lista 'stream_transacoes' e armazene em
# 'transacoes_liberadas' apenas os registros cujas contas NÃO estejam listadas em 'contas_bloqueadas'.
# Saída esperada: [{'id': 1, 'conta': 'acc_10', 'valor': 50.0}, {'id': 3, 'conta': 'acc_30', 'valor': 80.0}]
contas_bloqueadas = {"acc_99", "acc_88", "acc_77"}
stream_transacoes = [
    {"id": 1, "conta": "acc_10", "valor": 50.0},
    {"id": 2, "conta": "acc_99", "valor": 120.0},
    {"id": 3, "conta": "acc_30", "valor": 80.0},
    {"id": 4, "conta": "acc_88", "valor": 200.0}
]
transacoes_liberadas = []
for transacao in stream_transacoes:
    contahold = transacao["conta"]
    if contahold not in contas_bloqueadas:
        transacoes_liberadas.append(transacao)
    else:
        continue

print("K8 - Liberadas:", transacoes_liberadas)
print("=" * 65)

### Kata 9: Gerenciamento de Sessões em Memória
# Cenário:
# 1. Adicione a sessão 'tok_live_99' ao conjunto de sessões ativas.
# 2. Remova a sessão 'tok_live_02' de forma segura (sem estourar erro caso já tenha expirado).
# 3. Tente remover a sessão 'tok_inexistente' garantindo que o programa continue executando sem falhas.
# Saída esperada: {'tok_live_01', 'tok_live_03', 'tok_live_99'}
sessoes_ativas = {"tok_live_01", "tok_live_02", "tok_live_03"}


print("K9 - Sessões ativas:", sessoes_ativas)
print("=" * 65)

### Kata 10: Validação de Checklist Regulatório
# Cenário: Para aprovação de cadastro, um cliente precisa ter enviado TODOS os documentos
# listados em 'documentos_obrigatorios'. Verifique se 'documentos_enviados' cobre integralmente
# todos os itens obrigatórios, armazenando o resultado booleano (True ou False) em 'cadastro_conforme'.
# Saída esperada: True
documentos_obrigatorios = {"RG", "CPF", "COMPROVANTE_RESIDENCIA"}
documentos_enviados = {"RG", "CPF", "COMPROVANTE_RESIDENCIA", "CNH", "HOLERITE"}
cadastro_conforme = None


print("K10 - Cadastro conforme:", cadastro_conforme)
