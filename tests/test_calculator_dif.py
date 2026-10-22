from src.calculator import Calculator
def test_dif_no_args():
    Calculator().dif()
def test_dif_positive():
    assert Calculator().dif(5, 3) == 2


def test_dif_negative_result():
    assert Calculator().dif(1, 2) == -1


def test_dif_with_negative_operand():
    assert Calculator().dif(5, -2) == 7
