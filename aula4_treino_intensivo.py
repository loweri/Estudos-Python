###
Tabuada_9 = 9
for item in range (1,11):
    Tabuada_9_res = Tabuada_9 * item
    print(f"Resultado: {Tabuada_9_res}")
print("=" * 45)
###
for i in range(5,51, 5):
    print(f"Número: {i}")
print("=" * 45)
###
for contagem in range(10,-1, -1):
    print(f"Contagem regressiva: {contagem} ...")
print("Atividade bem-sucedida !! !! !!")
print("=" * 45)
###
for item in range(1,11):
    item_qd = item ** 2
    print(f"O quadrado de {item} é {item_qd}.")
print("=" * 45)
###
tabuada_3 = 3
for item in range (0,30,3):
    mult_item = tabuada_3 + item
    print(f"Resultado: {mult_item}.")
print("=" * 45)
###
soma_pares = 0
for item in range (2,51,2):
    soma_pares += item
    print(f"A soma atual: {soma_pares}")
print(f"A soma total dos números pares de 2 a 50 é: {soma_pares}")
print("=" * 45)
###
fatorial = 1
for item in range (1,6):
    fatorial = fatorial * item
    print(f"Resultado: {fatorial}")
print("=" * 45)
###
total_gasto = 0
for item in range(1,6):
    item1 = 25.50
    total_gasto = total_gasto + item1
    print(f"Total gasto = {total_gasto:.2f}")
print(f"Total da fatura: R${total_gasto:.2f}")
print("="* 45)
###
total_impares = 0
for i in range(1,31):
    if i % 2 != 0:
        total_impares += 1
print(f"Foram encontrados {total_impares} números ímpares entre 1 e 30")
print("="* 45)
###
soma_notas = 0
for i in range(1,11):
    soma_notas = soma_notas + i
avg_notas = soma_notas / 10
print(f"A média de notas entre 1 a 10 é: {avg_notas}!!")
print("="* 45)
###
for t in range(28,37):
    if t < 30:
        print(f"Temperatura: {t} ºC: Clima Agradável.")
    elif t >= 30 and t <= 33:
        print(f"Temperatura: {t} ºC: Clima Quente.")
    else:
        print(f"Temperatura: {t} ºC: ALERTA DE CALOR EXCESSIVO!")
print("="* 45)
###
for n in range(1,51):
    if n % 3 == 0 and n % 5 == 0:
        print(f"Divisivel por 3 ou 5: {n}")
print("="* 45)
###
for n in range(-3,4):
    if n > 0:
        print(f"Crédito: R${n:.2f}")
    elif n < 0:
        print(f"Débito: R${n:.2f}")
    else:
        print(f"Sado Neutro: {n:.2f}")
print("="* 45)
###
for e in range(10,0,-1):
    if e > 3:
        print(f"Estoque normal: {e} unidades disponíveis.")
    else:
        print(f"ATENÇÃO! Estoque crítico: {e} unidades!")
print("="* 45)
###
for n in range (1,16):
    if n % 4 == 0:
        print(f"{n} --> Múltiplo de 04!")
print("="* 45)
###
tanque_litros = 50
while tanque_litros > 0:
        tanque_litros -= 10
        print(f"Nível do combústivel: {tanque_litros} litros atualmente")
print(f"Alerta, tanque vazio! Pare no posto imediatamente")
print("="* 45)
###
tanque_litros = 50
while tanque_litros > 10:
        contador_aviso = 5
        tanque_litros -= contador_aviso
        print(f"Nível do combústivel: {tanque_litros} litros atualmente")
print(f"Alerta, tanque na reserva! Abasteça imediatamente.")
print("="* 45)
###
tentativas_restantes = 3
print(f"Bem vindo, você tem {tentativas_restantes} tentativas de acesso.")
while tentativas_restantes > 0:
    t = -1
    tentativas_restantes += t
    print(f"Senha incorreta! {tentativas_restantes} tentativas restantes.")
print(f"Suas tentativas acabaram, acione o suporte.")
print("="* 45)
###
andar_atual = 0
while andar_atual <= 6:
    print(f"Elevador em movimento. Andar atual: {andar_atual}.")
    andar_atual += 1
print("Chegamos à cobertura.")
print("="* 45)
###
saldo_poupanca = 0
mes = 1
while saldo_poupanca < 1000:
    saldo_poupanca += 200
    print(f"Mês {mes}: Saldo atual: R${saldo_poupanca}.")
    mes += 1
print(f"Meta de R$ 1000,00 atingida com sucesso!")
print("="* 45)
###
progresso = 0
while progresso <= 100:
    print(f"Baixando arquivo ... {progresso}% concluido.")
    progresso += 25
print("Download concluido com sucesso.")
print("="* 45)