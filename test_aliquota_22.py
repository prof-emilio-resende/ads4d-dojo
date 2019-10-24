def test_aliquota_22_50()
    aliquota = Aliquota(6000.0)
    assert aliquota.aplicar_desconto() == 921.60