from dependentes import Calcula_Dependentes

def test_dependentes():
    obj_dependente = Calcula_Dependentes()
    valor_dependentes =  obj_dependente.realiza_calculo(2)
    assert valor_dependentes == 379.18