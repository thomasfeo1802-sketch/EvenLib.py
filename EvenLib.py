def is_even(a):
    return a % 2 == 0

def not_even(a):
    return not is_even(a)

def max_even(a, b):
    # max(a, b) já retorna o maior valor automaticamente
    return is_even(max(a, b))

def max_not_even(a, b):
    return not max_even(a, b)

def min_even(a, b):
    return is_even(min(a, b))

def min_not_even(a, b):
    return not min_even(a, b)