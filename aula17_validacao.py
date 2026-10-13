"""
TESTE ÀS CEGAS DE VALIDAÇÃO: PANDAS & SQL NATIVO
Regra de Ouro: Resolva cada desafio exclusivamente com o seu próprio raciocínio.
Sem dicas de código, sem atalhos. Apenas cenário, dados e saída esperada.
"""

import sqlite3
import pandas as pd

print("=" * 65)

### Desafio 1: Higienização, Deduplicação e Imputação no Pandas
# Cenário: Uma esteira de faturamento recebeu um lote de pedidos com duplicatas e cupons não preenchidos.
# 1. A partir de 'df_pedidos', remova as duplicatas baseando-se na coluna 'pedido_id', mantendo a primeira ocorrência.
# 2. Na coluna 'cupom_desconto', substitua todos os valores ausentes pelo texto "SEM_CUPOM".
# 3. Guarde o DataFrame tratado em 'df_pedidos_limpos'.
# 4. Armazene a quantidade total de linhas válidas na variável 'total_pedidos_validos' (int).
# Dados de entrada:
dados_pedidos = {
    "pedido_id": [101, 102, 101, 103, 104, 102],
    "cliente": ["Alice", "Bob", "Alice", "Carlos", "Diana", "Bob"],
    "valor": [150.0, 200.0, 150.0, 80.0, 320.0, 200.0],
    "cupom_desconto": ["DESC10", None, "DESC10", None, "BLACKFRIDAY", None]
}
df_pedidos = pd.DataFrame(dados_pedidos)
df_pedidos_limpos = None
total_pedidos_validos = 0

# Espaço para sua resolução:


print("D1 - Total de Pedidos Válidos:", total_pedidos_validos)
print("D1 - Cupons Tratados:", df_pedidos_limpos["cupom_desconto"].tolist() if df_pedidos_limpos is not None else [])
# Saída esperada:
# Total de Pedidos Válidos: 4
# Cupons Tratados: ['DESC10', 'SEM_CUPOM', 'SEM_CUPOM', 'BLACKFRIDAY']
print("=" * 65)


### Desafio 2: Criação, Carga e Consulta Filtrada no SQLite
# Cenário: Um catálogo de produtos precisa ser estruturado e consultado em um banco relacional em memória.
# 1. Crie uma conexão SQLite em memória na variável 'conexao_db' e obtenha o 'cursor_db'.
# 2. Crie a tabela 'produtos' com as colunas:
#    - 'id': inteiro e chave primária
#    - 'nome': texto
#    - 'categoria': texto
#    - 'preco': decimal (REAL)
# 3. Insira todos os registros de 'catalogo_produtos' na tabela 'produtos' e confirme a transação.
# 4. Execute uma consulta SQL que traga apenas 'nome' e 'preco' dos produtos da categoria "Eletronicos"
#    cujo 'preco' seja estritamente maior que 500.0.
# 5. Recupere os registros filtrados na lista 'produtos_filtrados'.
# Dados de entrada:
catalogo_produtos = [
    (1, "Mouse Gamer", "Eletronicos", 150.0),
    (2, "Monitor 4K", "Eletronicos", 1800.0),
    (3, "Cadeira Ergonomica", "Moveis", 950.0),
    (4, "Notebook Pro", "Eletronicos", 4500.0),
    (5, "Mesa de Escritorio", "Moveis", 600.0)
]
conexao_db = None
cursor_db = None
produtos_filtrados = []

# Espaço para sua resolução:


print("D2 - Produtos Filtrados:", produtos_filtrados)
# Saída esperada: [('Monitor 4K', 1800.0), ('Notebook Pro', 4500.0)]
print("=" * 65)


### Desafio 3: Extração SQL para Pandas e Agregação
# Cenário: A diretoria financeira precisa calcular o preço médio dos produtos por categoria a partir do banco.
# 1. Usando a mesma 'conexao_db' do Desafio 2, execute a consulta SQL "SELECT categoria, preco FROM produtos"
#    carregando o resultado diretamente em um DataFrame do Pandas chamado 'df_catalogo'.
# 2. A partir de 'df_catalogo', calcule a média da coluna 'preco' agrupada por 'categoria'
#    e armazene a estrutura resultante na variável 'media_por_categoria'.
# 3. Extraia o valor médio específico da categoria "Moveis" para a variável 'media_moveis' (float).
df_catalogo = None
media_por_categoria = None
media_moveis = 0.0

# Espaço para sua resolução:


print("D3 - Média da Categoria Móveis:", media_moveis)
# Saída esperada: 775.0
print("=" * 65)

# Fechamento seguro da conexão
if conexao_db is not None:
    conexao_db.close()
