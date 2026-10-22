from calculator import Calculator
def test_calculator_exists(self):
        self.assertIsNotNone(Calculator())

    # --- smoke-тесты: вызов не падает ---
def test_sum_no_args(self):
  Calculator().sum()

def test_sum_one_pair_no_check(self):
  Calculator().sum(2, 2)

def test_dif_no_args(self):
  Calculator().dif()
