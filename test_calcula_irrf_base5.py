from calcula_irrf_base5 import Calcula_IRFF_Base5

def teste_calcula_irrf_base5():
    valor_liquido = Calcula_IRFF_Base5(5000, 27.5)
    assert valor_liquido.calcular() == 3625.00
