from dependentes import Calcula_Dependentes

def test_dependentes():
    dependentes = Calcula_Dependentes()
    assert dependentes.realiza_calculo(3) == 568.77