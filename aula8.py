def verificar_disponibilidade(lista_estoque,item_buscado):
    if item_buscado in lista_estoque:
        return "Produto disponível em estoque"
    else:
        return "Produto esgotado"
estoque = ["teclado","mouse","monitor","headset"]
busca1 = verificar_disponibilidade(estoque,"mouse")
busca2 = verificar_disponibilidade(estoque,"webcam")
print(f"{busca1}")
print(f"{busca2}")
print("=" * 45)
###
carrinho = []
carrinho.append("Coca-cola")
carrinho.append("Bolacha")
carrinho.append("Arroz")
print(f"Quantidade de produtos: {len(carrinho)}\nItens da lista:{carrinho}")
print("=" * 45)
###
fila_banco = ["Ana","Bruno","Carlos","Diana"]
atendido = fila_banco.pop(0)
fila_banco.append("Eduardo")
print(f"Cliente atendido: {atendido}.\nLista da fila: {fila_banco}.")
print("=" * 45)
###
precos = [45.90, 12.50, 99.00, 5.00, 32.80]
precos.sort()
print(f"Lista ordem crescente: {precos}")
precos.sort(reverse=True)
print(f"Lista decrescente: {precos}")
print(f"Menor preço: {precos[4]}")
print(f"Maior preço: {precos[0]}")
print("=" * 45)
###
def somar_faturamento(lista_valores):
    total = 0
    for valor in lista_valores:
        total = total + valor
    return total
vendas_do_dia = [120.00,450.50,89.90,310.00,15.00]
teste0 = somar_faturamento(vendas_do_dia)
print(f"Teste > {teste0:.2f}")