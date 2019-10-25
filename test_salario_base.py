import pytest
from class_02 import Calculate_IRRF

def test_salario_base():
    aliquota = Calculate_IRRF(1000.0)
    assert aliquota.salarioBase == 890