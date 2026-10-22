from calculator import Calculator
def test_sum_two_numbers():
    assert(Calculator().sum(2, 2)== 4)

def test_sum_three_numbers():
    assert(Calculator().sum(2, 3, 7)== 12)

def test_sum_four_numbers():
    assert(Calculator().sum(1, 3, 7, 9) == 20)
