transacoes_brutas = [
    ("  joao silva  ", 250.0, "PIX", "São Paulo"),
    ("maria oliveira", 12500.0, "TED", "São Paulo"),
    ("  carlos souza ", -50.0, "PIX", "Rio de Janeiro"), # ⚠️ Inválido!
    ("beatriz lima ", 8200.0, "BOLETO", "Curitiba"),
    ("marcos rocha", 45.0, "CARTAO", "Belo Horizonte"),
    ("fernanda alves", 15000.0, "PIX", "Brasília"),
]
def analisar_transacao(nome, valor, metodo, cidade):
    nome_limpo = nome.strip().upper()
    if valor <= 0:
        return None
    elif valor > 10000.00:
        nivel_risco = "Alto"
    elif 5000 < valor < 10000:
        nivel_risco = "Médio"
    else:
        nivel_risco = "Baixo"
    return (nome_limpo, valor, metodo, cidade, nivel_risco)
transacoes_validas = []
alertas_auditoria = []
for nome, valor, metodo, cidade in transacoes_brutas:
    resultado = analisar_transacao(nome, valor, metodo, cidade)
    if resultado != None:
        transacoes_validas.append(resultado)
        if resultado[4] == "Alto":
            alertas_auditoria.append(resultado)
def gerar_relatorio_financeiro(listas_validas):
    valores = []
    for val in listas_validas:
        val_limpo = val[1]
        valores.append(val_limpo)
    Soma = sum(valores)
    Minimo = min(valores)
    Maximo = max(valores)
    Qtd_max = len(listas_validas)
    return (Soma, Minimo, Maximo, Qtd_max)
teste2 = gerar_relatorio_financeiro(transacoes_validas)
Soma, Minimo, Maximo, Qtd_max = teste2
print(f"Relatório\nTotal de Transações Aprovadas: {Qtd_max}\nVolume total: {Soma:.2f}\nMenor transação: {Minimo:.2f}\nMaior transação: {Maximo:.2f}")
