def soma(a, b, c):
    somatorio = a + b + c
    return somatorio


def mul(a, b, c):
    return a * b * c


def isPalindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False
