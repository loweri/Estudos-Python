### k1
ponto_gps = (-23.550520, -46.633309)
lat, long = ponto_gps
print(lat)
print(long)
print(f"Tamanho da tupla: {len(ponto_gps)}")
print("=" * 45)
### k2
colaborador = ("Ericles", "Engenharia de Dados", "São Paulo", 2026)
nome, area, cidade, ano = colaborador
print(f"Desempacotado:\n{nome}\n{area}\n{cidade}\n{ano}")
print("=" * 45)
### k3
sensor_a = 45.2
sensor_b = 91.8
print(f"Valores antes da troca:\nS_A: {sensor_a}\nS_B: {sensor_b}\n {"-" * 45}")
sensor_a, sensor_b = sensor_b, sensor_a
print(f"Valores depois da troca:\nS_A: {sensor_a}\nS_B: {sensor_b}")
print("=" * 45)
### k4
def resumo_vendas(lista_valores):
    menor = min(lista_valores)
    maior = max(lista_valores)
    total = sum(lista_valores)
    return menor, maior, total
vendas = [150.0, 80.0, 300.0, 50.0, 220.0]
teste1 = resumo_vendas(vendas)
v_min, v_max, v_total = teste1
print(f"Resultado formatado:\n{v_min}\n{v_max}\n{v_total}")
print("=" * 45)
### k5
resultado = ("Hamilton", "Verstappen", "Leclerc", "Norris", "Alonso", "Piastri")
p_ouro, p_prata, *fora_do_podio = resultado
print(f"Pódio:\nOuro: {p_ouro}\nPrata: {p_prata}\nDemais participantes: {fora_do_podio}")