#from Calcula_Dependentes import Calcula_Dependentes

def test_sample():
  assert True

def test_dependentes():
  calcula_dep = Calcula_Dependentes()
  assert calcula_dep.realiza_calculo(3) == 568.77
