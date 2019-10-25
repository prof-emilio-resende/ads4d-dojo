from class_02 import Calculate_IRRF

def test_aliquota_0():
    aliquota = Calculate_IRRF.calculate(1900)
    assert aliquota == 0