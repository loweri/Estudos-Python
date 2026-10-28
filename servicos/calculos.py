"""
Módulo de cálculos financeiros e fiscais.
"""

def calcular_imposto_retido(valor_bruto: float, aliquota: float = 0.15) -> float:
    """
    Calcula o valor do imposto retido com base em uma alíquota percentual.
    Retorna o valor arredondado em 2 casas decimais.
    """
    if valor_bruto <= 0:
        return 0.0
    return round(valor_bruto * aliquota, 2)
