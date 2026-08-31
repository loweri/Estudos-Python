###
print("="* 45)
def graus_celsius(grausc):
    fahr = grausc * 1.8 + 32
    return fahr
primeiratemp = graus_celsius(30)
segundatemp = graus_celsius(23)
terceiratemp = graus_celsius(18)
print(f"A temperatura em Fahrenheit é: {primeiratemp}ºF.")
print(f"Para 23ºC atualmente, é de {segundatemp}ºF")
print(f"E para mais tarde, 18ºC será de {terceiratemp}ºF")
print("="* 45)
###
def folha_pgto(horas_trab,valor_hora):
    salario_bruto = horas_trab * valor_hora
    return salario_bruto
salario_calculado = folha_pgto(40, 35.50)
print(f"O salário recebido foi de R${salario_calculado}.")
print("="* 45)
###
def bilheteria(tipo_publico):
    if tipo_publico == "estudante":
        valor_ing = 15.00
    elif tipo_publico == "idoso":
        valor_ing = 12.00
    else:
        valor_ing = 30.00
    return valor_ing
cliente1 = bilheteria("estudante")
cliente2 = bilheteria("idoso")
cliente3 = bilheteria("comum")
print(f"Os preços de hoje são:\nEstudante = R${cliente1:.2f} .\nComum = R${cliente3:.2f} .\nIdoso = R${cliente2:.2f} .")
print("="* 45)
###
def loja_xy(valor_compra, tem_cupom):
    if tem_cupom == True:
        valor_final = valor_compra - 20.00
    else:
        valor_final = valor_compra
    return valor_final
compra1 = loja_xy(150, True)
compra2 = loja_xy(80, False)
print(f"Sua compra totalizou: R${compra1:.2f} .")
print(f"Sua compra totalizou: R${compra2:.2f} .")
print("="* 45)
###
def exame_hab(idade):
    if idade >= 18:
        pode_dirigir = True
    else:
        pode_dirigir = False
    return pode_dirigir
aluno1 = exame_hab(19)
aluno2 = exame_hab(16)
print(f"Para ambos os alunos a resposta é: I - {aluno1} e II - {aluno2}.")
print("="* 45)