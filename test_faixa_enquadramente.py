def test_enquadramento():
    obj_faixa = Faixa_Enquadramento(2000)
    assert obj_faixa.valor_base == 1903.99 and obj_faixa.valor_limite == 2826.65 and obj_faixa.aliquota == 7.5