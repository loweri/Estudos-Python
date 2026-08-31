def formatar_nome(nome_sujo):
    nome_limpo = nome_sujo.strip().upper()
    return nome_limpo
teste1 = "   ericles oliveira   "
teste2 = formatar_nome(teste1)
print(f"{teste2}")
print("="* 45)
###
def validar_senha(senha):
    if len(senha) > 8:
        return "Senha forte"
    else:
        return "Senha fraca"
teste3 = validar_senha("12345")
teste4 = validar_senha("segredo2026")
print(f"Testes:\n{teste3}\n{teste4}")
print("="* 45)
###
def mascarar_dominio(email):
    emailmasc1 = email.replace("@gmail.com","@yahoo.com.br")
    return emailmasc1
emailtrocado = mascarar_dominio("ericlesg@gmail.com")
print(f"Novo email: {emailtrocado}")
print("="* 45)
###
def pegar_iniciais(primeiro_nome, sobrenome):
    primeiro_nome_limpo = primeiro_nome[0]
    sobrenome_limpo = sobrenome[0]
    nome_completo = primeiro_nome_limpo.upper() + "." + sobrenome_limpo.upper() + "."
    return nome_completo
teste5 = pegar_iniciais("Ericles", "Oliveira")
print(f"Teste: {teste5}")
print("="* 45)
###
def extrair_ano(data_em_texto):
    datalimpa = data_em_texto.split("/")
    dataprocessada = datalimpa[2]
    return dataprocessada
teste6 = extrair_ano("15/12/2024")
print(f"Nova data: {teste6}")
print("="* 45)
