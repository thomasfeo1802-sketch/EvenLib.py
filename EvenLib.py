#EvenLib.py

def isEven(a): #é par
    if a % 2 == 0:
        return True
    else:
        return False

def ntEven(a): #não é par
    if a % 2 == 0:
        return False
    else:
        return True

def bgEven(a , b): #maior é par
    if a > b:
        if a % 2 == 0:
            return True
        else:
            return False
    else:
        if b % 2 == 0:
            return True
        else:
            return False

def nbgEven(a , b): #maior não é par
    if a > b:
        if a % 2 == 0:
            return False
        else:
            return True
    else:
        if b % 2 == 0:
            return False
        else:
            return True

def smEven(a , b): #menor é par
    if a < b:
        if a % 2 == 0:
            return False
        else:
            return True
    else:
        if b % 2 == 0:
            return False
        else:
            return True

def nsmEven(a , b): #menor não é par
    if a < b:
        if a % 2 == 0:
            return True
        else:
            return False
    else:
        if b % 2 == 0:
            return True
        else:
            return False