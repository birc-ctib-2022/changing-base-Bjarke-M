"""Changing bases."""

digits = {}

for i in range(0, 10):
    digits[i] = str(i)

digits[10] = 'A'
digits[11] = 'B'
digits[12] = 'C'
digits[13] = 'D'
digits[14] = 'E'
digits[15] = 'F'


def change_to_base(n: int, b: int) -> str:
    """
    Return `n` in base `b`.

    The base `b` must be in the range 2 to 16.

    >>> change_to_base(1, 2)
    '1'
    >>> change_to_base(31, 2)
    '11111'
    >>> change_to_base(31, 8)
    '37'
    >>> change_to_base(31, 16)
    '1F'
    """
    if n < 0:        #when n < 0 we have to consider how to handle division on negative numbers
        tegn = -1    #we do so by making a way of adding a minus sign, if we know n to be negative as // (flooring) is funny on negative numbers
    elif n==0:       # to ensure we do not break python we include what will happen when n==0
        return '0'
    else:             # if n is positive we will not have to append a sign
        tegn = 1
    n *= tegn         # because flooring work by rounding to the lowest number we have a problem when negative, i've tried to remove that by making n positive for now
    liste = []         #a list for our results
    while n:
        liste.append(str(n%b)) #making n in our base
        n = int(n//b)          # moduloing around (n will be true while not 0)
    if tegn < 0:                # if the number was negative 
        liste.append('-')       # we append a minus sign
    assert 2 <= b <= 16
    return ''.join(liste[::-1])  # to get the minus sign in the right place 
