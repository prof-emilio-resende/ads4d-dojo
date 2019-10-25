from contribuintes import Contribuinte

def test_contribuinte():
    valores_contribuinte = Contribuinte(1990.00, 4)
    assert valores_contribuinte.salario_bruto == 1990.00
    assert valores_contribuinte.qtd_depen == 4