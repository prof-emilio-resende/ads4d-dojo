def teste_calcula_irrf_base5():
    valor_liquido = Calculate_IRRF(5000)
    assert valor_liquido.calculate() == 851.40
