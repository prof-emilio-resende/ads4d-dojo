def test_aliquota_0():
    aliquota = Aliquota(1900)
    assert aliquota.aplicar_desconto() == 0
