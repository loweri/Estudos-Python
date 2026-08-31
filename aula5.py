def calcular_triplo(numero):
    calculo = numero * 3
    return calculo
variavel_x = calcular_triplo(15)
print(variavel_x)
print("=" * 45)
###
def combo(preço_lanche,preço_refri):
    valor_total = preço_lanche + preço_refri
    return valor_total
cliente1 = combo(10,5)
cliente2 = combo(40,17.50)
print(f"O total para o cliente 1 é de {cliente1:.2f}")
print(f"O total para o cliente 2 é de {cliente2:.2f}")
print("=" * 45)
###
def calcular_banho(porte,quer_tosa):
    #Tenho 3 tamanhos, opção de tosa ou não tosa
    # ajuste posterior: entrada de minúsculas:
    porte = porte.lower()
    prt1 = "pequeno"
    prt2 = "médio"
    prt3 = "grande"
    if porte == prt1:
        preco_banho = 40.00
    elif porte == prt2:
        preco_banho = 60.00
    else:
        preco_banho = 90.00
    preco_tosa = 0
    if quer_tosa == "Sim":
        preco_tosa += 20.00
    else:
        preco_tosa = 0.0
    total = preco_banho + preco_tosa
    return total
cliente1 = calcular_banho("Pequeno","Sim")
cliente2 = calcular_banho("Grande", "Sim")
cliente3 = calcular_banho("Médio", "Não")
print(f" Os preços para cada cliente são:\n cliente 1 - {cliente1};\n cliente 2 - {cliente2};\n cliente 3 - {cliente3}.")
print("="*45)
###
def estacionamento(veiculo,horas,vip):
    # Tenho 3 tipos de veiculos, cada um com seu preço:
    if veiculo == "Moto":
        tarifa_hora = 5.00
    elif veiculo == "Carro":
        tarifa_hora = 10.00
    elif veiculo == "Caminhonete":
        tarifa_hora = 15.00
    valor_bruto = tarifa_hora * horas
    #para os veiculos temos que considerar os três:
    #Também temos o status vip:
    if vip == True:
        valor_final = valor_bruto - 5.00
    else:
        valor_final = valor_bruto
    return valor_final
cliente1 = estacionamento("Carro",3,False)
cliente2 = estacionamento("Moto",4,True)
cliente3 = estacionamento("Caminhonete",2,True)
print(f"Cliente 1: {cliente1};\nCliente 2: {cliente2};\nCliente 3: {cliente3}.")