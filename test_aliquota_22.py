def test_aliquota_22_50()
    aliquota = Aliquota(4000.0)
    assert aliquota.aplicar_desconto() == 471.60