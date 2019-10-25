from class_INSS import Calculate_INSS

def test_class_desconto_INSS():
    calcINSS = Calculate_INSS(3000)
    assert calcINSS.calculate() == 330
