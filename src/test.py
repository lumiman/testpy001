from main import Calculator

def test_sums_2_numbers():
    calculator = Calculator()
    result = calculator.suma(2, 3)
    assert result == 5, f"Expected 5 but got {result}"