from app.fizzbuzz import calculate


def test_calculate_input_of_three_returns_fizz():
    value = calculate(3)

    assert "Fizz" == value

def test_multiple_of_five_buzz():
    value = calculate(5)

    assert "Buzz" == value

def test_multiple_of_three_and_five_fizzbuzz():
    value = calculate(15)

    assert  "FizzBuzz" == value

def test_calculate_input_of_one_returns_one():
    value = calculate(1)

    assert 1 == value

def test_multiple_of_three():
    value = calculate(6)

    assert "Fizz" == value

def test_multiple_of_five():
    value = calculate(10)

    assert "Buzz" == value

def test_multiple_of_five_and_three():
    value = calculate(30)

    assert "FizzBuzz" == value

def test_no_multiples_of_five_and_three():
    value = calculate(2)

    assert 2 == value