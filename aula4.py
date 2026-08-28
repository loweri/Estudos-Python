# Aula 4 - Estruturas de repetição/ loops
#for i in range(5):
#    print(f"Número atual: {i}")
#print("=" * 45)
#for ii in range(1,11):
#    print(f"Número atual: {ii}")
#print("=" * 45)
#for iii in range(0,11,2):
#    print(f"Pares: {iii}")
#print("=" * 45)
# # #
#bateria = 100
#while bateria > 0:
#    print(f"Bateria em {bateria}% ...")
#    bateria -= 5
#print("Aparelho descarregou")
#print("=" * 45)
# # #
#total_gasto = 0
#for item in range(1,4):
#    preco = 10
#    total_gasto += preco
#print(f"Total final: R${total_gasto}")
#print("=" * 45)
# # #
# 1.4.1 - Contagem regressiva
cont_foguete = 5
while cont_foguete >= 0:
    print(f"Contagem regressiva: {cont_foguete}")
    cont_foguete -= 1
print("Fim da contagem regressiva")
print("=" * 45)
# # #
# 1.4.2 - Tabuada automatica
numero_tabuada = 7
for item in range(0, 11):
    resultado_multip = numero_tabuada * item
    print(f"Resultado {resultado_multip}")
print("=" * 45)
# # #
# 1.4.3 - Cofrinho acumulador
soma_total = 0
for item in range (1,101):
    soma_total = soma_total + item
    print(f"Resultado da soma: {soma_total}")
print("=" * 45)
# # #
# 1.4.4 - Simulador de carregamento
carga_celular = -20
while carga_celular < 100:
    carga_celular += 20
    print(f"Carregando ... A carga atual é de {carga_celular}%")
print(f"Carga completa, {carga_celular}%")
print("=" * 45)
# # #
# 1.4.5 - Filtro de números pares
for i in range (1, 21):
    if i % 2 == 0:
        print(f"Número par atual: {i}")
print("=" * 45)