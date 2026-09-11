"""
MÓDULO 2.4: CONJUNTOS (set)
Fundamentos de Deduplicação, Busca O(1) e Álgebra de Conjuntos
"""

print("=" * 65)
### Kata 1: Deduplicação Relâmpago
# Cenário: Uma lista de logs registrou acessos com vários IDs de usuários duplicados.
# Crie um conjunto 'usuarios_unicos' contendo apenas os IDs distintos.
# Entrada:
logs_usuarios = [101, 102, 101, 103, 104, 102, 105, 101, 104]
usuarios_unicos = None

print(usuarios_unicos)
print("=" * 65)

### Kata 2: Mutação Básica (Adição e Remoção Segura)
# Cenário: Gerenciar uma lista de IPs bloqueados (blacklist).
# 1. Adicione o IP "192.168.1.50" à blacklist.
# 2. Remova o IP "10.0.0.1" usando o método seguro que não causa erro caso o item não exista.
# Entrada:
blacklist = {"10.0.0.1", "172.16.0.5"}


print(blacklist)
print("=" * 65)

### Kata 3: Interseção (Auditoria de Acessos Comuns)
# Cenário: Identificar funcionários que possuem acesso TANTO à base de 'pagamentos' QUANTO à de 'auditoria'.
# Entrada:
acesso_pagamentos = {"Alice", "Bruno", "Carlos", "Diana"}
acesso_auditoria = {"Bruno", "Diana", "Eduardo", "Fernanda"}
ambos_acessos = None

print(ambos_acessos)
print("=" * 65)

### Kata 4: Diferença (Detecção de Discrepâncias / Missing)
# Cenário: Identificar quais clientes estão na base de 'pedidos', mas AINDA NÃO constam na base de 'pagamentos' efetuados.
# Entrada:
clientes_pedidos = {"C1", "C2", "C3", "C4", "C5"}
clientes_pagos = {"C1", "C3", "C5"}
pendentes_pagamento = None

print(pendentes_pagamento)
print("=" * 65)

### Kata 5: União e Diferença Simétrica
# Cenário:
# 1. Obter a lista completa de todos os servidores existentes em duas regiões (União).
# 2. Obter apenas os servidores que existem EXCLUSIVAMENTE em uma região ou na outra, mas NUNCA em ambas (Diferença Simétrica).
# Entrada:
servidores_us_east = {"srv-01", "srv-02", "srv-03"}
servidores_us_west = {"srv-02", "srv-03", "srv-04"}
todos_servidores = None
exclusivos_por_regiao = None

print("Todos:", todos_servidores)
print("Exclusivos:", exclusivos_por_regiao)
