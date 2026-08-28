# aula2.py
preco_arroz = 24.90
qtd_arroz = 3
preco_feijao = 8.50
qtd_feijao = 2
total_compra = float(preco_arroz * qtd_arroz + preco_feijao * qtd_feijao)
valor_total = total_compra
print(f"Total da compra: {valor_total:.2f}")
print("-" * 30)
# # #
total_viajado = 450
combustivel_consumido = 36.5
consumo_medio = float(total_viajado/combustivel_consumido)
print(f"Consumo médio: {consumo_medio:.2f}")
print("-" * 30)
# # #
pizza_grande = 14
qtd_pessoas = 4
qtd_inteira_p_pessoa = pizza_grande // qtd_pessoas
pizza_sobras = pizza_grande % qtd_pessoas
print(f"Total de pedaços por pessoa: {qtd_inteira_p_pessoa}")
print(f"Sobra de pedaços: {pizza_sobras}")
print("-" * 30)
# # #
metragem_total_terreno = 15
metragem_quadrada = metragem_total_terreno ** 2
print(f"Total em Metros Quadrados do Terreno: {metragem_quadrada}")
print("-" * 30)
# # #
qtd_str = "120"
qtd_int_str = int(qtd_str)
pco_unit_str = "14.50"
pco_unit_int_fl = float(pco_unit_str)
valor_final = qtd_int_str * pco_unit_int_fl
print(f"Valor final: R${valor_final:.2f}")
print("-" * 30)
# # #