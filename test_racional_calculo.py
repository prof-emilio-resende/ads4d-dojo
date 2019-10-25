from classe_racional_calculo import Racional_Calculo

def test_class_racional_calculo():
    racionalCalculo = Racional_Calculo(3000, 330, 0, 2670, 766.02, 0, 387.45, 57.45)
    assert racionalCalculo.salario_bruto == 3000
    assert racionalCalculo.desconto_inss == 330
    assert racionalCalculo.deducao_dependentes == 0
    assert racionalCalculo.valor_base == 2670
    assert racionalCalculo.valor_isencao == 766.02
    assert racionalCalculo.faixa_enquadramento == 0
    assert racionalCalculo.valor_para_descontar == 387.45
    assert racionalCalculo.valor_irrf == 57.45
