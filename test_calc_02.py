from class_02 import Calculate_IRRF

def test_class_02_desconto_IRRF():
    calcIRRF = Calculate_IRRF(3000)
    assert calcIRRF.calculate() == 57.45
