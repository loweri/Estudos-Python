"""
MÓDULO 5 - AULA 20: MODULARIZAÇÃO, ARQUITETURA DE CÓDIGO E ARQUIVOS .ENV
Objetivo:
1. Gestão segura de credenciais e segredos com arquivos .env e a biblioteca 'python-dotenv'.
2. Leitura de variáveis de ambiente com 'os.getenv', tratamento de fallbacks e tipagem.
3. Importação modular de funções e classes a partir de pacotes externos ('servicos').
4. Construção de pipelines com separação clara de responsabilidades.
"""

print("=" * 65)
print("AULA 20: MODULARIZAÇÃO E VARIÁVEIS DE AMBIENTE (.ENV)")
print("=" * 65)


### Kata 1: Carregamento do Arquivo .env e Leitura Básica
# Cenário: Em um ambiente corporativo, senhas e endereços de servidores NUNCA ficam hardcoded no código.
# 1. Carregue as variáveis do arquivo '.env' usando a função 'load_dotenv' da biblioteca 'dotenv'.
# 2. Leia a variável 'DB_HOST' e guarde na variável 'host_configurado' (str).
# 3. Leia a variável 'DB_USER' e guarde na variável 'usuario_configurado' (str).
host_configurado = ""
usuario_configurado = ""

# Espaço para resolução do Kata 1:
import os
from dotenv import load_dotenv
load_dotenv()
host_configurado = os.getenv("DB_HOST")
usuario_configurado = os.getenv("DB_USER")


print(f"K1 - Host: {host_configurado} | Usuário: {usuario_configurado}")
# Saída esperada:
# K1 - Host: cluster-analitico.empresa.internal | Usuário: eng_dados
print("=" * 65)


### Kata 2: Leitura com Valor Padrão (Fallback) e Conversão de Tipos
# Cenário: Variáveis de ambiente são SEMPRE lidas como strings. Algumas variáveis podem estar ausentes no .env.
# 1. Leia a variável 'DB_PORT' do .env e converta para int, guardando em 'porta_banco' (int).
# 2. Leia a variável 'TIMEOUT_SEGUNDOS', que NÃO existe no arquivo .env.
#    Configure o 'os.getenv' para usar o valor padrão "30" caso a variável não exista, e converta para int em 'timeout_configurado' (int).
# 3. Leia a variável 'BATCH_SIZE' do .env e converta para int em 'tamanho_lote' (int).
porta_banco = 0
timeout_configurado = 0
tamanho_lote = 0

# Espaço para resolução do Kata 2:
porta_banco = int(os.getenv("DB_PORT"))
timeout_configurado = int(os.getenv("TIMEOUT_SEGUNDOS", "30"))
tamanho_lote = int(os.getenv("BATCH_SIZE"))


print(f"K2 - Porta: {porta_banco} | Timeout: {timeout_configurado}s | Lote: {tamanho_lote}")
# Saída esperada:
# K2 - Porta: 5432 | Timeout: 30s | Lote: 250
print("=" * 65)


### Kata 3: Importação Modular de Funções
# Cenário: Funções de cálculo não devem poluir o arquivo principal de execução.
# 1. Importe a função 'calcular_imposto_retido' que está dentro do módulo 'servicos.calculos'.
# 2. Execute o cálculo para uma transação bruta de 1500.0 com alíquota padrão de 15% (0.15).
#    Guarde o resultado na variável 'imposto_calculado_a' (float).
# 3. Execute o cálculo para uma transação bruta de 4000.0 com alíquota personalizada de 20% (0.20).
#    Guarde o resultado na variável 'imposto_calculado_b' (float).
imposto_calculado_a = 0.0
imposto_calculado_b = 0.0

# Espaço para resolução do Kata 3:
from servicos.calculos import calcular_imposto_retido
imposto_calculado_a = calcular_imposto_retido(1500.0, 0.15)
imposto_calculado_b = calcular_imposto_retido(4000.0, 0.20)

print(f"K3 - Imposto A (15% de 1500): R$ {imposto_calculado_a} | Imposto B (20% de 4000): R$ {imposto_calculado_b}")
# Saída esperada:
# K3 - Imposto A (15% de 1500): R$ 225.0 | Imposto B (20% de 4000): R$ 800.0
print("=" * 65)


### Kata 4: Importação Modular de Classes e Injeção de Configuração
# Cenário: Classes de conexão de infraestrutura ficam em módulos próprios e recebem as configurações do .env.
# 1. Importe a classe 'ConexaoArmazem' do módulo 'servicos.armazenamento'.
# 2. Instancie essa classe passando as credenciais que você leu nos Katas 1 e 2:
#    'host_configurado', 'porta_banco' e 'usuario_configurado'.
#    Guarde a instância na variável 'conexao_dw'.
# 3. Chame o método 'conectar()' desse objeto e guarde o retorno em 'status_conexao' (str).
conexao_dw = None
status_conexao = ""

# Espaço para resolução do Kata 4:
from servicos.armazenamento import ConexaoArmazem
conexao_dw = ConexaoArmazem(host_configurado, porta_banco, usuario_configurado)
status_conexao = conexao_dw.conectar()

print(f"K4 - Status: {status_conexao}")
# Saída esperada:
# K4 - Status: CONECTADO: eng_dados@cluster-analitico.empresa.internal:5432
print("=" * 65)


### Kata 5: Pipeline Modular Integrado com Dados em Lote
# Cenário: Um lote de transações precisa ter seus impostos calculados via módulo e seu total validado.
# 1. Abaixo está uma lista com valores brutos de vendas.
# 2. Itere sobre essa lista, calculando o imposto retido de cada uma usando a função 'calcular_imposto_retido' (com alíquota padrão de 15%).
# 3. Guarde o valor líquido de cada transação (valor_bruto - imposto) na lista 'valores_liquidos' (arredondado em 2 casas decimais).
# 4. Acumule o total de impostos gerados pelo lote na variável 'total_impostos_lote' (float, arredondado em 2 casas).
vendas_lote = [1200.0, 350.0, 5000.0, 850.0, 2100.0]
valores_liquidos = []
total_impostos_lote = 0.0

# Espaço para resolução do Kata 5:
for venda in vendas_lote:
    imposto = calcular_imposto_retido(venda, 0.15)
    imposto_calculado = round(venda - imposto, 2)
    valores_liquidos.append(imposto_calculado)
    total_impostos_lote += imposto
total_impostos_lote = round(total_impostos_lote, 2)    

print(f"K5 - Valores Líquidos: {valores_liquidos}")
print(f"K5 - Total Impostos Lote: R$ {total_impostos_lote}")
# Saída esperada:
# K5 - Valores Líquidos: [1020.0, 297.5, 4250.0, 722.5, 1785.0]
# K5 - Total Impostos Lote: R$ 1425.0
print("=" * 65)
