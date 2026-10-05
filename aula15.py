"""
MÓDULO 4.2: TRATAMENTO, TRANSFORMAÇÃO E AGREGAÇÃO COM PANDAS
Objetivo: Tratamento de nulos, filtros compostos, agrupamentos e ordenação.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

import pandas as pd

print("=" * 65)

### Kata 1: Identificação e Imputação de Valores Ausentes
# Cenário: Uma esteira de ingestão recebe cadastros com campos de telefone incompletos.
# 1. Identifique e conte a quantidade total de valores ausentes na coluna 'telefone' do DataFrame 'df_contatos',
#    armazenando o total na variável 'total_nulos_telefone' (int).
# 2. Crie um novo DataFrame chamado 'df_contatos_preenchidos' onde todos os valores ausentes
#    da coluna 'telefone' sejam substituídos pelo texto "NÃO INFORMADO".
# Dados de entrada:
dados_contatos = {
    "cliente_id": [1, 2, 3, 4, 5],
    "nome": ["Ana", "Carlos", "Beatriz", "Daniel", "Eduarda"],
    "telefone": ["11999991111", None, "21988882222", None, "31977773333"]
}
df_contatos = pd.DataFrame(dados_contatos)
total_nulos_telefone = 0
df_contatos_preenchidos = None
total_nulos_telefone = df_contatos["telefone"].isna().sum()
df_contatos_preenchidos = df_contatos.fillna({"telefone":"NÃO INFORMADO"})


print(f"K1 - Total Nulos Telefone: {total_nulos_telefone}")
print(f"K1 - Valores Preenchidos:\n{df_contatos_preenchidos['telefone'].tolist() if df_contatos_preenchidos is not None else []}")
# Saída esperada:
# Total Nulos Telefone: 2
# Valores Preenchidos: ['11999991111', 'NÃO INFORMADO', '21988882222', 'NÃO INFORMADO', '31977773333']
print("=" * 65)


### Kata 2: Descarte de Registros Corrompidos/Incompletos
# Cenário: Em um lote de transações financeiras, registros sem identificador de conta são inválidos
# e devem ser removidos do fluxo analítico.
# 1. A partir do DataFrame 'df_transacoes', descarte todas as linhas que contenham valores ausentes
#    especificamente na coluna 'conta_id', armazenando o resultado no DataFrame 'df_transacoes_limpas'.
# 2. Armazene a quantidade de linhas restantes na variável 'linhas_restantes' (int).
# Dados de entrada:
dados_transacoes = {
    "transacao_id": [101, 102, 103, 104, 105],
    "conta_id": [501.0, None, 503.0, None, 505.0],
    "valor": [150.0, 320.0, 89.9, 1200.0, 45.0]
}
df_transacoes = pd.DataFrame(dados_transacoes)
df_transacoes_limpas = None
linhas_restantes = 0
df_transacoes_limpas = df_transacoes.dropna(subset=["conta_id"])
linhas_restantes = len(df_transacoes_limpas)

print("K2 - Linhas Restantes:", linhas_restantes)
# Saída esperada: 3
print("=" * 65)


### Kata 3: Filtragem com Múltiplas Condições Lógicas
# Cenário: Uma esteira de risco precisa selecionar clientes elegíveis para um produto de crédito.
# A partir de 'df_clientes', filtre os registros que atendam simultaneamente aos critérios:
# - 'idade' maior ou igual a 30
# - 'renda_mensal' estritamente maior que 5000.0
# Armazene o DataFrame resultante em 'df_elegiveis' e a quantidade total de clientes filtrados em 'total_elegiveis' (int).
# Dados de entrada:
dados_clientes = {
    "nome": ["Lucas", "Mariana", "Roberto", "Fernanda", "Gabriel"],
    "idade": [25, 34, 45, 29, 38],
    "renda_mensal": [4200.0, 6800.0, 5000.0, 7500.0, 9200.0]
}
df_clientes = pd.DataFrame(dados_clientes)
df_elegiveis = None
total_elegiveis = 0
filtro = (df_clientes["idade"] >= 30) & (df_clientes["renda_mensal"] > 5000.0)
df_elegiveis = df_clientes[filtro]
total_elegiveis = len(df_elegiveis)

print("K3 - Total de Clientes Elegíveis:", total_elegiveis)
# Saída esperada: 2
print("=" * 65)


### Kata 4: Agrupamento e Agregação de Métricas
# Cenário: O setor financeiro necessita de um relatório consolidado com o total vendido por categoria.
# 1. A partir do DataFrame 'df_pedidos', calcule a soma da coluna 'valor' agrupada por 'setor'.
#    Armazene a estrutura resultante em 'faturamento_por_setor'.
# 2. Extraia o valor específico do faturamento do setor "Eletrônicos" para a variável 'faturamento_eletronicos' (float).
# Dados de entrada:
dados_pedidos = {
    "pedido_id": [1, 2, 3, 4, 5, 6],
    "setor": ["Eletrônicos", "Móveis", "Eletrônicos", "Alimentos", "Móveis", "Eletrônicos"],
    "valor": [1200.0, 800.0, 450.0, 150.0, 350.0, 900.0]
}
df_pedidos = pd.DataFrame(dados_pedidos)
faturamento_por_setor = None
faturamento_eletronicos = 0.0
faturamento_por_setor = df_pedidos.groupby("setor")["valor"].sum()
faturamento_eletronicos = float(faturamento_por_setor["Eletrônicos"])

print("K4 - Faturamento de Eletrônicos:", faturamento_eletronicos)
# Saída esperada: 2550.0
print("=" * 65)


### Kata 5: Deduplicação e Ordenação
# Cenário: Logs operacionais registraram chamados duplicados durante instabilidades de rede.
# 1. Remova os registros duplicados de 'df_chamados' com base na coluna 'chamado_id', mantendo a primeira ocorrência.
# 2. Ordene os registros restantes de forma decrescente pela coluna 'nivel_prioridade' (do maior para o menor).
# 3. Armazene o DataFrame resultante em 'df_chamados_higienizados'.
# 4. Extraia o valor da coluna 'chamado_id' do primeiro registro dessa tabela ordenada para a variável 'primeiro_chamado_id' (int).
# Dados de entrada:
dados_chamados = {
    "chamado_id": [101, 102, 101, 103, 102, 104],
    "descricao": ["Erro login", "Lentidão", "Erro login", "Falha pagamento", "Lentidão", "Bug visual"],
    "nivel_prioridade": [3, 2, 3, 5, 2, 1]
}
df_chamados = pd.DataFrame(dados_chamados)
df_chamados_higienizados = None
primeiro_chamado_id = 0
df_chamados_higienizados = df_chamados.drop_duplicates(subset=["chamado_id"])
df_ranking = df_chamados_higienizados.sort_values(by="nivel_prioridade", ascending=False)
primeiro_chamado_id = int(df_ranking.iloc[0]["chamado_id"])

print("K5 - Total de Chamados Únicos:", len(df_chamados_higienizados) if df_chamados_higienizados is not None else 0)
print("K5 - Primeiro Chamado ID:", primeiro_chamado_id)
# Saída esperada:
# Total de Chamados Únicos: 4
# Primeiro Chamado ID: 103
print("=" * 65)
