from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max'
    assert hello_who('Leo') == 'Hello, Leo'
    assert hello_who('Artem') == 'Hello, Artem'
    assert hello_who('Denis') == 'Hello, Denis'

def test_salary():
    assert(2, 2) != 8
    assert(3, 1) != 6
