from calculator import Calculator
def test_sum_two_numbers(self):
    self.assertEqual(Calculator().sum(2, 2), 4)

def test_sum_three_numbers(self):
    self.assertEqual(Calculator().sum(2, 3, 7), 12)

def test_sum_four_numbers(self):
    self.assertEqual(Calculator().sum(1, 3, 7, 9), 20)
