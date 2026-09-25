"""
MÓDULO 3.1: TRATAMENTO DE EXCEÇÕES - TREINO INTENSIVO (10 KATAS)
Objetivo: Fixação prática e deliberada de controle de fluxo de exceções.
Regra: Resolva cada Kata no espaço reservado sem alterar os dados de entrada.
"""

print("=" * 65)

### Kata 1: Conversão Segura de Portas de Rede
# Cenário: Uma lista de portas de rede recebidas como string deve ser convertida para inteiros.
# Itens corrompidos que falharem na conversão devem receber o valor numérico padrão 8080.
# Dados de entrada:
portas_raw = ["80", "443", "INVALIDA", "8000", "CORROMPIDA"]
portas_processadas = []
for portas in portas_raw:
    try:
        portas_tratadas = int(portas)
        portas_processadas.append(portas_tratadas)
    except ValueError as e:
        erro_capt = 8080
        portas_processadas.append(erro_capt)

print("K1 - Portas Processadas:", portas_processadas)
# Saída esperada: [80, 443, 8080, 8000, 8080]
print("=" * 65)


### Kata 2: Consulta Segura de Variáveis de Ambiente
# Cenário: Uma aplicação precisa ler chaves de configuração em um dicionário.
# Para cada chave na lista 'chaves_requisitadas', consulte seu valor no dicionário 'configuracoes'.
# Se a chave não existir no dicionário, adicione a string "NAO_CONFIGURADO" na lista 'valores_finais'.
# Dados de entrada:
configuracoes = {"DB_HOST": "localhost", "DB_PORT": "5432"}
chaves_requisitadas = ["DB_HOST", "DB_USER", "DB_PORT", "DB_PASSWORD"]
valores_finais = []
for chaves in chaves_requisitadas:
    try:
        chavefinal = configuracoes[chaves]
        valores_finais.append(chavefinal)
    except KeyError:
        valores_finais.append("nao_config")

print("K2 - Valores Finais:", valores_finais)
# Saída esperada: ['localhost', 'NAO_CONFIGURADO', '5432', 'NAO_CONFIGURADO']
print("=" * 65)


### Kata 3: Extração Posicional de Header
# Cenário: Uma esteira de ingestão recebe linhas de metadados fatiadas em listas.
# Para cada linha em 'linhas_header', tente extrair o quarto elemento (índice 3).
# Se a linha possuir o quarto elemento, adicione-o na lista 'timestamps_coletados'.
# Se a posição não existir na sublista, adicione a string "SEM_TIMESTAMP" na lista 'timestamps_coletados'.
# Dados de entrada:
linhas_header = [
    ["id", "nome", "status", "2026-01-01"],
    ["id", "nome"],
    ["id", "nome", "status", "2026-01-02"]
]
timestamps_coletados = []
for linha in linhas_header:
    try:
        coleta = linha[3]
        timestamps_coletados.append(coleta)
    except IndexError:
        semcoleta = "Sem_Timestamp"
        timestamps_coletados.append(semcoleta)
print("K3 - Timestamps Coletados:", timestamps_coletados)
# Saída esperada: ['2026-01-01', 'SEM_TIMESTAMP', '2026-01-02']
print("=" * 65)


### Kata 4: Cálculo Seguro de Custo Médio por Requisição
# Cenário: Calcule o custo médio por requisição dividindo 'custo_total' por 'requisicoes_totais'.
# Se 'requisicoes_totais' for zero, defina 'custo_medio = 0.0'.
# Dados de entrada:
custo_total = 450.0
requisicoes_totais = 0
custo_medio = None
try:
    custo_medio = custo_total / requisicoes_totais
except ZeroDivisionError:
    custo_medio = 0.0


print("K4 - Custo Médio:", custo_medio)
# Saída esperada: 0.0
print("=" * 65)


### Kata 5: Triagem de Falhas em Pipeline
# Cenário: Uma lista de dados brutos passa por processamento matemático (conversão para float e divisão por 2).
# Itere sobre 'itens_brutos':
# - Se o item for convertido e dividido com sucesso, adicione o resultado na lista 'valores_validos'.
# - Se ocorrer erro de valor na conversão, incremente o contador 'erros_valor'.
# - Se ocorrer erro de tipo na operação, incremente o contador 'erros_tipo'.
# Dados de entrada:
itens_brutos = ["10.0", None, "texto", "20.0"]
valores_validos = []
erros_valor = 0
erros_tipo = 0
for item in itens_brutos:
    try:
        itemconver = float(item) / 2
        valores_validos.append(itemconver)
    except ValueError:
        erros_valor += 1
    except TypeError:
        erros_tipo += 1

print("K5 - Valores Válidos:", valores_validos)
print(f"K5 - Erros de Valor: {erros_valor} | Erros de Tipo: {erros_tipo}")
# Saída esperada:
# Valores Válidos: [5.0, 10.0]
# Erros de Valor: 1 | Erros de Tipo: 1
print("=" * 65)


### Kata 6: Auditoria com Captura da Mensagem de Exceção
# Cenário: Para cada leitura na lista 'sensores', tente converter para float.
# Se a conversão falhar, capture a mensagem da exceção e armazene na lista 'auditoria_falhas'
# uma tupla contendo (leitura, texto_da_mensagem_de_erro).
# Dados de entrada:
sensores = ["101.5", "ERR_OFFLINE", "98.2", "ERR_VOLTAGEM"]
auditoria_falhas = []
for sensor in sensores:
    try:
        num_audit = float(sensor)
    except ValueError as e:
        erro_capt = (sensor, str(e))
        auditoria_falhas.append(erro_capt)


print("K6 - Auditoria de Falhas:", auditoria_falhas)
# Saída esperada: [('ERR_OFFLINE', "could not convert string to float: 'ERR_OFFLINE'"), ('ERR_VOLTAGEM', "could not convert string to float: 'ERR_VOLTAGEM'")]
print("=" * 65)


### Kata 7: Validação de Limite de Temperatura com Disparo Intencional
# Cenário: Uma função 'validar_temperatura_servidor(temperatura)' monitora a CPU de um servidor.
# - Se 'temperatura' for maior que 85.0, dispare exceção do tipo ValueError com a mensagem: "Alerta: Superaquecimento critico"
# - Se 'temperatura' for menor que 0.0, dispare exceção do tipo ValueError com a mensagem: "Alerta: Sensor defeituoso"
# - Caso contrário, retorne a string "Temperatura normal"
# Fora da função, teste chamando validar_temperatura_servidor(92.5) dentro de uma estrutura de proteção
# e armazene a mensagem de erro disparada na variável 'registro_alerta'.
registro_alerta = ""

def validar_temperatura_servidor(temperatura):
    if temperatura > 85.0:
        raise ValueError("Alerta: Superaquecimento critico")
    if temperatura < 0.0:
        raise ValueError("Alerta: sensor defeituoso")
    return "Temperatura Normal"

# Espaço para a chamada protegida:
registro_alerta = ""
try:
    validar_temperatura_servidor(92.5)
except ValueError as e:
    registro_alerta = str(e)

print("K7 - Registro de Alerta:", registro_alerta)
# Saída esperada: "Alerta: Superaquecimento critico"
print("=" * 65)


### Kata 8: Validação com Sucesso Exclusivo
# Cenário: Itere sobre a lista 'contratos'.
# Para cada item, se o tamanho do texto for menor que 3 caracteres, dispare exceção do tipo ValueError com a mensagem: "Contrato invalido".
# - Se houver a exceção ValueError, adicione o texto da mensagem na lista 'falhas'.
# - Se a validação do contrato passar sem erros, adicione o nome do contrato na lista 'aprovados' exclusivamente através da cláusula de sucesso do bloco.
# Dados de entrada:
contratos = ["CTR-991", "OK", "CTR-882", ""]
aprovados = []
falhas = []

# Espaço para resolução:
for contrato in contratos:
    try:
        contrato_hold = len(contrato)
        if contrato_hold < 3:
            raise ValueError ("Contrato invalido")
    except ValueError as e:
        falhas.append(str(e))
    else:
            aprovados.append(contrato)


print("K8 - Aprovados:", aprovados)
print("K8 - Falhas:", falhas)
# Saída esperada:
# Aprovados: ['CTR-991', 'CTR-882']
# Falhas: ['Contrato invalido', 'Contrato invalido']
print("=" * 65)


### Kata 9: Encerramento Garantido de Sessão
# Cenário: Uma operação de persistência de dados opera com a variável 'sessao_ativa = True'.
# Tente calcular '100 / divisor'.
# Se houver divisão por zero, defina 'status_operacao = "FALHA"'.
# Independentemente de ter ocorrido erro ou sucesso, a variável 'sessao_ativa' deve ser definida como False
# obrigatoriamente dentro da cláusula de finalização do bloco.
divisor = 0
sessao_ativa = True
status_operacao = "PENDENTE"

# Espaço para resolução:
try:
    divisao = 100 / divisor
except ZeroDivisionError:
    status_operacao = "FALHA"
finally:
    sessao_ativa = False

print(f"K9 - Status: {status_operacao} | Sessão Ativa: {sessao_ativa}")
# Saída esperada: Status: FALHA | Sessão Ativa: False
print("=" * 65)


### Kata 10: Processamento de Lote com Triagem Integrada
# Cenário: Uma esteira financeira processa valores de transações na lista 'transacoes'.
# Itere sobre 'transacoes':
# - Se o valor for negativo (menor que zero), dispare ValueError com a mensagem: "Transacao negativa".
# - Se houver ValueError, capture e adicione o texto da mensagem na lista 'erros_lote'.
# - Se o valor passar sem erros, adicione o valor na lista 'processadas_lote' através da cláusula de sucesso exclusivo do bloco.
# - A cada iteração do laço, incremente o contador 'total_processamentos' em 1 dentro da cláusula que executa obrigatoriamente independente do resultado.
# Dados de entrada:
transacoes = [100, -20, 350, -5]
processadas_lote = []
erros_lote = []
total_processamentos = 0

# Espaço para resolução:
for transacao in transacoes:
    try:
        if transacao < 0:
            raise ValueError ("Transacao Negativa")  
    except ValueError as err:
        erro = str(err)
        erros_lote.append(erro)
    else:
        processadas_lote.append(transacao) 
    finally:
        total_processamentos += 1

print("K10 - Processadas:", processadas_lote)
print("K10 - Erros do Lote:", erros_lote)
print("K10 - Total de Processamentos:", total_processamentos)
# Saída esperada:
# Processadas: [100, 350]
# Erros do Lote: ['Transacao negativa', 'Transacao negativa']
# Total de Processamentos: 4
print("=" * 65)
