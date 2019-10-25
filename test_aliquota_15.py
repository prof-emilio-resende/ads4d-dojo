#from classe_imposto import Aliquota

def test_aliqota_15():
    A = Calculte_IRRF()
    assert A.aliquota_03(3500) == 239.4
      
