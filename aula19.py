"""
MÓDULO 4.5: PROGRAMAÇÃO ORIENTADA A OBJETOS (OOP) NO PYTHON
Objetivo: Classes, construtor (__init__), atributos, métodos de instância, validação de estado e interação entre objetos.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

print("=" * 65)

### Kata 1: Definição de Classe, Construtor e Atributos de Instância
# Cenário: Uma esteira de monitoramento precisa representar instâncias de servidores na nuvem.
# 1. Defina a classe 'ServidorCloud'.
# 2. No construtor, receba 'hostname' (str), 'ip' (str) e 'memoria_gb' (int),
#    armazenando-os como atributos do próprio objeto.
# 3. Instancie um servidor com os dados:
#    - hostname: "srv-prod-01"
#    - ip: "10.0.0.1"
#    - memoria_gb: 64
#    Armazene esse objeto na variável 'servidor_producao'.
# 4. Extraia os valores dos atributos desse objeto para as variáveis correspondentes:
#    'host_extraido', 'ip_extraido' e 'memoria_extraida'.
servidor_producao = None
host_extraido = ""
ip_extraido = ""
memoria_extraida = 0

# Espaço para resolução do Kata 1:
class ServidorCloud:
    def __init__(self, hostname, ip, memoria_gb):
        self.hostname = hostname
        self.ip = ip
        self.memoria_gb = memoria_gb
    def fazer_upgrade(self, adicional_gb):
        self.memoria_gb += adicional_gb
servidor_producao = ServidorCloud("srv-prod-01", "10.0.0.1", 64)
host_extraido = servidor_producao.hostname
ip_extraido = servidor_producao.ip
memoria_extraida = servidor_producao.memoria_gb

print(f"K1 - Host: {host_extraido} | IP: {ip_extraido} | Memória: {memoria_extraida}GB")
# Saída esperada:
# Host: srv-prod-01 | IP: 10.0.0.1 | Memória: 64GB
print("=" * 65)


### Kata 2: Métodos de Instância e Modificação de Estado
# Cenário: Recursos de um servidor podem ser expandidos conforme a demanda operacional.
# 1. Na classe 'ServidorCloud' (ou em uma nova definição contendo o construtor do Kata 1),
#    crie o método 'fazer_upgrade(adicional_gb)'.
# 2. Esse método deve somar 'adicional_gb' à memória atual do servidor.
# 3. Instancie o servidor 'srv-cache-01' com IP "10.0.0.5" e 16 GB de memória na variável 'servidor_cache'.
# 4. Aplique um upgrade de 16 GB nesse servidor.
# 5. Armazene a nova quantidade de memória em 'memoria_apos_upgrade' (int).
servidor_cache = None
memoria_apos_upgrade = 0

# Espaço para resolução do Kata 2:
servidor_cache = ServidorCloud("srv=cache-01", "10.0.0.5", 16)
servidor_cache.fazer_upgrade(16)
memoria_apos_upgrade = servidor_cache.memoria_gb

print(f"K2 - Memória após Upgrade: {memoria_apos_upgrade}GB")
# Saída esperada:
# Memória após Upgrade: 32GB
print("=" * 65)


### Kata 3: Regras de Negócio e Validação de Estado
# Cenário: Uma esteira de armazenamento precisa controlar o consumo de cotas de disco e impedir que clientes consumam mais do que possuem.
# 1. Crie a classe 'CotaDisco' que recebe no construtor 'cliente_id' (str) e 'gigas_disponiveis' (float).
# 2. Crie o método 'consumir(quantidade_gb)':
#    - Se 'quantidade_gb' for menor ou igual a zero OU maior que 'gigas_disponiveis': a operação é inválida. O saldo de gigas não muda e o método deve retornar False.
#    - Se houver gigas suficientes: subtrai 'quantidade_gb' do saldo e o método retorna True.
# 3. Crie a instância 'cota_cliente' para o cliente "CLI-900" com 100.0 gigas disponíveis.
# 4. Tente realizar duas operações na sequência:
#    - Operação A: consumir 40.0 GB (deve ser autorizada) -> guarde o retorno em 'resultado_op_a' (bool).
#    - Operação B: consumir 80.0 GB (deve ser rejeitada por falta de cota) -> guarde o retorno em 'resultado_op_b' (bool).
# 5. Guarde o saldo final restante de gigas em 'saldo_final_gigas' (float).
cota_cliente = None
resultado_op_a = None
resultado_op_b = None
saldo_final_gigas = 0.0

# Espaço para resolução do Kata 3:
class CotaDisco:
    def __init__(self, cliente_id, gigas_disponiveis):
        self.cliente_id = cliente_id
        self.gigas_disponiveis = gigas_disponiveis
    def consumir(self, quantidade_gb):
        if quantidade_gb <= 0 or quantidade_gb > self.gigas_disponiveis:
            return False
        self.gigas_disponiveis -= quantidade_gb
        return True
    def transferir(self, cota_destino, quantidade_gb):
        if quantidade_gb <= 0 or quantidade_gb > self.gigas_disponiveis:
            return False
        self.gigas_disponiveis -= quantidade_gb
        cota_destino.gigas_disponiveis += quantidade_gb
        return True
cota_cliente = CotaDisco("CLI-900", 100.0)
resultado_op_a = cota_cliente.consumir(40)
resultado_op_b = cota_cliente.consumir(80)
saldo_final_gigas = cota_cliente.gigas_disponiveis

print(f"K3 - Operação A: {resultado_op_a} | Operação B: {resultado_op_b} | Saldo Restante: {saldo_final_gigas}GB")
# Saída esperada:
# Operação A: True | Operação B: False | Saldo Restante: 60.0GB
print("=" * 65)


### Kata 4: Interação Entre Múltiplos Objetos (Transferência de Recursos)
# Cenário: É necessário permitir a transferência de cotas de disco entre dois clientes diferentes.
# 1. Na classe 'CotaDisco', adicione o método 'transferir(cota_destino, quantidade_gb)':
#    - Validação: se a cota de origem não conseguir consumir 'quantidade_gb' (por saldo insuficiente ou valor inválido), a transferência falha: nada é alterado e o método retorna False.
#    - Sucesso: se houver cota suficiente, subtrai da cota de origem, adiciona à 'cota_destino' e o método retorna True.
# 2. Crie duas instâncias:
#    - 'cota_ana': cliente "ANA-01" com 50.0 GB
#    - 'cota_beto': cliente "BETO-02" com 20.0 GB
# 3. Realize uma transferência de 30.0 GB da 'cota_ana' para a 'cota_beto', guardando o retorno em 'sucesso_transferencia' (bool).
# 4. Armazene o saldo final de cada um em 'saldo_ana' e 'saldo_beto' (float).
cota_ana = None
cota_beto = None
sucesso_transferencia = None
saldo_ana = 0.0
saldo_beto = 0.0

# Espaço para resolução do Kata 4:
cota_ana = CotaDisco("ANA-01", 50.0)
cota_beto = CotaDisco("BETO-02", 20.0)
sucesso_transferencia = cota_ana.transferir(cota_beto, 30.0)
saldo_ana = cota_ana.gigas_disponiveis
saldo_beto = cota_beto.gigas_disponiveis

print(f"K4 - Transferência Sucesso: {sucesso_transferencia}")
print(f"K4 - Saldo Ana: {saldo_ana}GB | Saldo Beto: {saldo_beto}GB")
# Saída esperada:
# Transferência Sucesso: True
# Saldo Ana: 20.0GB | Saldo Beto: 50.0GB
print("=" * 65)


### Kata 5: Coleção de Objetos e Processamento em Lote
# Cenário: Um painel de infraestrutura precisa monitorar o consumo total de uma lista de cotas ativas.
# 1. A partir da lista de cotas abaixo, filtre apenas aquelas cujo 'gigas_disponiveis' seja maior ou igual a 50.0.
# 2. Armazene os 'cliente_id' dessas cotas filtradas na lista 'clientes_com_alta_cota'.
# 3. Calcule a soma total de gigas disponíveis apenas dessas cotas filtradas na variável 'total_gigas_alto_consumo' (float).
lista_cotas = [
    CotaDisco("CLI-01", 120.0) if 'CotaDisco' in locals() else None,
    CotaDisco("CLI-02", 30.0) if 'CotaDisco' in locals() else None,
    CotaDisco("CLI-03", 85.0) if 'CotaDisco' in locals() else None,
    CotaDisco("CLI-04", 15.0) if 'CotaDisco' in locals() else None,
    CotaDisco("CLI-05", 200.0) if 'CotaDisco' in locals() else None
]
clientes_com_alta_cota = []
total_gigas_alto_consumo = 0.0

# Espaço para resolução do Kata 5:
for item in lista_cotas:
    if item.gigas_disponiveis >= 50.0:
        clientes_com_alta_cota.append(item.cliente_id)
        total_gigas_alto_consumo += item.gigas_disponiveis

print("K5 - Clientes com Alta Cota:", clientes_com_alta_cota)
print("K5 - Total de Gigas em Alta Cota:", total_gigas_alto_consumo)
# Saída esperada:
# Clientes com Alta Cota: ['CLI-01', 'CLI-03', 'CLI-05']
# Total de Gigas em Alta Cota: 405.0
print("=" * 65)
