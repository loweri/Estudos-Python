"""
MÓDULO 3.1: TRATAMENTO DE EXCEÇÕES (try / except / else / finally / raise)
Fundamentos de Resiliência de Código em Engenharia de Dados
"""

print("=" * 65)
### Kata 1: Conversão Segura com Fallback
# Cenário: Um payload de dados enviou uma lista com valores de medições de sensores.
# Algumas medições vieram corrompidas como texto inválido.
# Itere sobre 'medicoes_brutas', tente converter cada item para float e adicione em 'medicoes_validas'.
# Se a conversão falhar (ValueError), adicione o valor de segurança 0.0 na lista.
# Saída esperada: [12.5, 0.0, 45.2, 0.0, 18.9]
medicoes_brutas = ["12.5", "N/A", "45.2", "CORRUPTED", "18.9"]
medicoes_validas = []
for medicao in medicoes_brutas:
    try:
        peso = float(medicao)
        medicoes_validas.append(peso)
    except ValueError:
        medicoes_validas.append(0.0)
print("K1 - Medições válidas:", medicoes_validas)
print("=" * 65)

### Kata 2: Cálculo Seguro de Métrica (Divisão por Zero)
# Cenário: Calcular o Ticket Médio de uma loja (faturamento total / quantidade de pedidos).
# Se a quantidade de pedidos for zero, trate a exceção matemática e defina o 'ticket_medio' como 0.0.
# Saída esperada: 0.0
faturamento = 15000.0
quantidade_pedidos = 0
ticket_medio = None
try:
    ticket_medio = faturamento / quantidade_pedidos
except ZeroDivisionError:
    print("Tratando o erro de divisão por zero")
    ticket_medio = 0
finally:
    print("Fim da conexão.")
print("K2 - Ticket Médio:", ticket_medio)
print("=" * 65)

### Kata 3: Captura Específica Múltipla
# Cenário: Um lote de requisições de usuários possui registros defeituosos:
# - Alguns não possuem o campo obrigatório 'id' (KeyError).
# - Outros possuem a pontuação com tipo incompatível (TypeError ao tentar somar com bônus fixo de 10).
# Itere sobre 'requisicoes':
# 1. Capture o 'id' e some 10 na 'pontuacao'.
# 2. Se faltar a chave 'id', incremente o contador 'erros_chave' em 1.
# 3. Se houver erro de tipo na soma, incremente o contador 'erros_tipo' em 1.
# 4. Registros sem erro devem ter o id adicionado na lista 'processados_sucesso'.
# Saída esperada:
# processados_sucesso = [101, 104]
# erros_chave = 1
# erros_tipo = 1
requisicoes = [
    {"id": 101, "pontuacao": 50},
    {"pontuacao": 30},              # ⚠️ Sem chave 'id'
    {"id": 103, "pontuacao": None},# ⚠️ TypeError ao somar com número
    {"id": 104, "pontuacao": 80}
]
processados_sucesso = []
erros_chave = 0
erros_tipo = 0
for requisicao in requisicoes:
    try:
        requisi_temp = requisicao["id"]
        pontua_temp = requisicao["pontuacao"] + 10
        processados_sucesso.append(requisi_temp)
    except KeyError:
        erros_chave += 1
    except TypeError:
        erros_tipo += 1

print("K3 - Sucessos:", processados_sucesso)
print(f"K3 - Erros de Chave: {erros_chave} | Erros de Tipo: {erros_tipo}")
print("=" * 65)

### Kata 4: Bloco de Limpeza e Fechamento (finally)
# Cenário: Simular a conexão com um banco de dados.
# 1. Tente realizar a consulta 'resultado = 100 / divisor'.
# 2. Se houver divisão por zero, capture o erro e defina 'resultado' como 0.
# 3. INDEPENDENTEMENTE de dar erro ou não (na cláusula de limpeza final),
#    defina 'conexao_fechada' como True.
# Saída esperada: resultado = 0, conexao_fechada = True
divisor = 0
resultado = None
conexao_fechada = False
try:
    resultado = 100 / divisor
except:
    resultado = 0
finally:
    conexao_fechada = True

print(f"K4 - Resultado: {resultado} | Conexão Fechada: {conexao_fechada}")
print("=" * 65)

### Kata 5: Validação Regulatória com Lançamento Intencional (raise)
# Cenário: Uma função 'validar_idade_contratual' recebe uma idade.
# Se a idade for menor que 18, lance uma exceção ValueError com a mensagem: "Idade inferior ao permitido".
# Caso contrário, retorne True.
# Chame a função passando idade = 15 dentro de um bloco try/except e capture a mensagem de erro
# na variável 'mensagem_capturada'.
# Saída esperada: "Idade inferior ao permitido"
def validar_idade_contratual(idade):
    if idade < 18:
        raise ValueError("Idade inferior ao permitido")
    return True
try:
    mensagem_capturada = validar_idade_contratual(15)
except ValueError as e:
    mensagem_capturada = e

print("K5 - Mensagem capturada:", mensagem_capturada)
print("=" * 65)

### Kata 6: Conversão e Registro da Mensagem do Erro (as e)
# Cenário: Uma esteira de telemetria recebe leituras de temperatura como string.
# Para cada item em 'leituras', tente converter para float e adicione na lista 'temperaturas_ok'.
# Se houver falha de conversão, capture a exceção, extraia o texto da mensagem de erro e adicione
# uma tupla (item, str(e)) na lista 'erros_log'.
# Saída esperada:
# temperaturas_ok = [25.4, 30.1]
# erros_log = [('FALHA_SENSOR', ...), ('TIMEOUT', ...)]
leituras = ["25.4", "FALHA_SENSOR", "30.1", "TIMEOUT"]
temperaturas_ok = []
erros_log = []
for leitura in leituras:
    try:
        temperaturas_tratadas = float(leitura)
        temperaturas_ok.append(temperaturas_tratadas)
    except ValueError as e:
        erro_capturado = (leitura, str((e)))
        erros_log.append(erro_capturado)

print("K6 - Temperaturas OK:", temperaturas_ok)
print("K6 - Log de Erros:", erros_log)
print("=" * 65)

### Kata 7: Validação de Saldo com Disparo Intencional (raise)
# Cenário: Uma função 'sacar(saldo, valor)' gerencia saques bancários.
# - Se 'valor' for maior que 'saldo', dispare ValueError com a mensagem exata: "Saldo insuficiente"
# - Se 'valor' for menor ou igual a zero, dispare ValueError com a mensagem exata: "Valor de saque invalido"
# - Caso contrário, retorne o saldo restante (saldo - valor).
# Teste a função chamando sacar(100.0, 150.0) dentro de uma estrutura de proteção e capture
# o texto da mensagem na variável 'motivo_recusa'.
# Saída esperada: "Saldo insuficiente"
def sacar(saldo, valor):
    saque = saldo - valor
    return saque
try:
    saque01 = sacar(100.0, 150.0)
except ValueError as e:
    motivo_recusa = valor > saldo
    e = "Saldo insuficiente"


motivo_recusa = ""


print("K7 - Motivo da recusa:", motivo_recusa)
print("=" * 65)

### Kata 8: Fluxo Completo com Sucesso Exclusivo (else)
# Cenário: O bloco 'else' de um try/except só executa quando NENHUM erro acontece no try.
# Itere sobre 'arquivos_recebidos'.
# Tente verificar o nome do arquivo. Se o nome for vazio (""), dispare ValueError com a mensagem "Nome ausente".
# Se houver ValueError, adicione o texto da mensagem na lista 'rejeitados'.
# Se o arquivo for validado sem erros (no bloco de sucesso exclusivo 'else'), adicione o nome em 'aprovados'.
# Saída esperada:
# aprovados = ['vendas.csv', 'clientes.parquet', 'relatorio.json']
# rejeitados = ['Nome ausente']
arquivos_recebidos = ["vendas.csv", "clientes.parquet", "", "relatorio.json"]
aprovados = []
rejeitados = []


print("K8 - Aprovados:", aprovados)
print("K8 - Rejeitados:", rejeitados)
print("=" * 65)

### Kata 9: Acesso Posicional Protegido (IndexError)
# Cenário: Uma lista de coordenadas espaciais contém pontos com diferentes dimensões.
# Para cada ponto em 'coordenadas', tente extrair o terceiro elemento (eixo Z, índice 2).
# Se o ponto possuir o terceiro elemento, adicione-o na lista 'eixos_z'.
# Se a posição não existir (IndexError), adicione o valor padrão 0 na lista 'eixos_z'.
# Saída esperada: [30, 0, 80]
coordenadas = [
    [10, 20, 30],
    [40, 50],
    [60, 70, 80]
]
eixos_z = []


print("K9 - Eixos Z:", eixos_z)
print("=" * 65)

### Kata 10: Auditoria Resiliente com Limpeza Obrigatória (finally)
# Cenário: Uma rotina de auditoria precisa calcular a taxa de conversão (conversoes / visitantes).
# A variável 'auditoria_finalizada' deve registrar se o processo foi encerrado.
# 1. Tente calcular 'taxa = conversoes / visitantes'.
# 2. Se houver divisão por zero, defina 'taxa = 0.0'.
# 3. INDEPENDENTEMENTE de ter ocorrido erro ou sucesso, defina 'auditoria_finalizada = True' na cláusula de limpeza final.
# Saída esperada: taxa = 0.0, auditoria_finalizada = True
conversoes = 150
visitantes = 0
taxa = None
auditoria_finalizada = False


print(f"K10 - Taxa: {taxa} | Auditoria Finalizada: {auditoria_finalizada}")

