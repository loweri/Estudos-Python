"""
DESAFIO DE CONSOLIDAÇÃO: SIMULADOR DE CONTA CORRENTE BANCÁRIA
Objetivo: Aplicar Orientação a Objetos (classes, atributos, métodos de depósito, saque e transferência) para consolidar o modelo mental de sistemas transacionais.

REGRAS GERAIS:
- Resolva no espaço indicado.
- Não altere os dados de teste nem as saídas esperadas.
"""

print("=" * 65)
print("DESAFIO DE CONSOLIDAÇÃO - SIMULADOR BANCÁRIO")
print("=" * 65)

### Cenário:
# Você foi encarregado de construir o núcleo transacional de um banco digital.
# 1. Defina a classe 'ContaBancaria'.
# 2. Construtor (__init__):
#    - Recebe 'titular' (str) e 'saldo_inicial' (float).
#    - Armazena ambos como atributos da instância.
# 3. Método 'depositar(valor)':
#    - Se 'valor' for maior que 0: soma ao saldo da conta e retorna True.
#    - Caso contrário: não altera o saldo e retorna False.
# 4. Método 'sacar(valor)':
#    - Se 'valor' for maior que 0 e menor ou igual ao saldo atual: subtrai do saldo e retorna True.
#    - Caso contrário: não altera o saldo e retorna False.
# 5. Método 'transferir(conta_destino, valor)':
#    - Se conseguir sacar 'valor' da conta de origem: deposita 'valor' na 'conta_destino' e retorna True.
#    - Se não houver saldo suficiente ou o valor for inválido: nada é alterado e retorna False.

conta_ericles = None
conta_nubank = None
sucesso_deposito = None
sucesso_saque = None
sucesso_transf_1 = None
sucesso_transf_2 = None
saldo_final_ericles = 0.0
saldo_final_nubank = 0.0

# =====================================================================
# ESPAÇO PARA RESOLUÇÃO DO DESAFIO:
# =====================================================================
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial
    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        return True
    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        return True
    def transferir(self, conta_destino, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo -= valor
        conta_destino.saldo += valor
        return True

# =====================================================================
# ÁREA DE TESTE (NÃO ALTERE):
# Descomente o bloco de teste abaixo assim que implementar a classe:
# =====================================================================
conta_ericles = ContaBancaria("Ericles", 100.0)
conta_nubank = ContaBancaria("Nubank Reserva", 500.0)

# 1. Depósito de 50.0 na conta do Ericles:
sucesso_deposito = conta_ericles.depositar(50.0)

# 2. Tentativa de saque de 200.0 na conta do Ericles (deve falhar por saldo insuficiente):
sucesso_saque = conta_ericles.sacar(200.0)

# 3. Transferência de 80.0 da conta do Ericles para a conta Nubank Reserva (deve suceder):
sucesso_transf_1 = conta_ericles.transferir(conta_nubank, 80.0)

# 4. Tentativa de transferência de 100.0 do Ericles para a Nubank Reserva (deve falhar por saldo insuficiente):
sucesso_transf_2 = conta_ericles.transferir(conta_nubank, 100.0)

saldo_final_ericles = conta_ericles.saldo
saldo_final_nubank = conta_nubank.saldo

print(f"Depósito (50.0): {sucesso_deposito}")
print(f"Saque (200.0): {sucesso_saque}")
print(f"Transferência 1 (80.0): {sucesso_transf_1}")
print(f"Transferência 2 (100.0): {sucesso_transf_2}")
print(f"Saldo Final Ericles: R$ {saldo_final_ericles:.2f}")
print(f"Saldo Final Nubank: R$ {saldo_final_nubank:.2f}")

# Saída esperada:
# Depósito (50.0): True
# Saque (200.0): False
# Transferência 1 (80.0): True
# Transferência 2 (100.0): False
# Saldo Final Ericles: R$ 70.00
# Saldo Final Nubank: R$ 580.00
print("=" * 65)
