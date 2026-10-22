from calculator import Calculator
def test_calculator_exists():
  Calculator()

    # --- smoke-тесты: вызов не падает ---
def test_sum_no_args():
  Calculator().sum()

def test_sum_one_pair_no_check():
  Calculator().sum(2, 2)

def test_dif_no_args():
  Calculator().dif()
