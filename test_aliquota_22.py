from class_02 import Calculate_IRRF
import pytest

def test_aliquota_22_50():
    aliquota = Calculate_IRRF(4000.0)
    assert aliquota.aplicar_desconto() == 471.60