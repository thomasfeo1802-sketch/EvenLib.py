def is_even(a):
    return a % 2 == 0

def is_not_even(a):
    return not is_even(a)

def is_max_even(a, b):
    # max(a, b) já retorna o maior valor automaticamente
    return is_even(max(a, b))

def is_max_not_even(a, b):
    return not is_max_even(a, b)

def is_min_even(a, b):
    return is_even(min(a, b))

def is_min_not_even(a, b):
    return not is_min_even(a, b)