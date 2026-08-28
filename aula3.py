# aula 3 bateria de 5 desafios
# 1.3.1 - Validador de Saque Bancário
saldo_cliente = 250.00
valor_saque = 300.00
if saldo_cliente >= valor_saque:
    saldo_atualizado = saldo_cliente - valor_saque
    print(f"Saque aprovado! Novo saldo: R${saldo_atualizado}")
else:
    print(f"Saldo insuficiente para saque!")
print("=" * 30)
# # #
# 1.3.2 - Radar de velocidade na rodovia 
velocidade_carro = 101
limite_via = 80
if velocidade_carro <= limite_via:
    print("Velocidade permitida, boa viagem")
elif velocidade_carro > limite_via and velocidade_carro < 100:
    print("Multa leve por excesso de velocidade")
elif velocidade_carro >= 100:
    print("Multa grave, velocidade acima de 100km/h")
print("=" * 30)
# # #
# 1.3.3 - Triagem de Pronto-Socorro
temperatura = 39.2
pressao_alta = True
if temperatura > 38.5 and pressao_alta == True:
    print("Alerta vermelho: encaminhar para emergência imediata!")
else:
    print("Atendimento padrão: aguardar na recepção.")
print("=" * 30)
# # #
# 1.3.4 - Desconto de fidelidadee no ecommerce
valor_compra = 180.00
cliente_vip = True
if valor_compra > 200.00 or cliente_vip == True:
    #aplicar 10% de desconto
    valor_final = valor_compra * 0.90
    print(f"Desconto de 10% aplicado, valor final: R${valor_final:.2f}")
else:
    print(f"Sem desconto, valor final: R${valor_compra:.2f}")
print("=" * 30)
# # #
# 1.3.5 - Par ou impar
numero = 27
if numero % 2 == 1:
    print(f"O resultado para o número {numero} é ímpar.")
else:
    print(f"O resultado para o número {numero} é par.")