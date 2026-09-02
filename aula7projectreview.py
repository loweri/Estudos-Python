## Cenário: Processador de vendas do e-commerce
def processar_pedido(nome_cliente,preco_unitario,quantidade,cupom_desconto):
    nome_cliente_limpo = nome_cliente.strip().upper()
    calculo_bruto = preco_unitario * quantidade
    if cupom_desconto == "CUPOM10":
        calculo_bruto_desc = calculo_bruto * 0.90
    elif cupom_desconto == "CUPOM20":
        calculo_bruto_desc = calculo_bruto * 0.80
    else:
        calculo_bruto_desc = calculo_bruto
    return nome_cliente_limpo, calculo_bruto_desc
teste1 = processar_pedido("Marcos Limeira ", 400,10,"CUPOM10")
teste2 = processar_pedido("  Rose Campos", 350,10,"CUPOM20")
teste3 = processar_pedido(" Til de Oliveira ", 500, 5, "")
pedidos = [teste1, teste2, teste3]
for nome_cliente_limpo, calculo_bruto_desc in pedidos:
    print(f"Pedido processado para: {nome_cliente_limpo} - Total a pagar: R$ {calculo_bruto_desc:.2f}")