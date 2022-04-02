def mensagem():
    print('Texto da função')


mensagem()


def message(text):
    print(text)


message('Hey there!')


def soma(a, b):
    print(a + b)


soma(3, 1)


def somar(a, b):
    return a + b


result = somar(3, 5)
print(result)


def calcula_energia_potencial_gravitacional(m, h, g=10):
    """
    Calcula a energia pontencial gravitacional
    argumentos:
    m: massa, entrada como uma variável float
    h: altura, entrada como uma variável float

    Argumentos opcional:
    g: aceleração gravitacional, com valor default de 10
    """
    e = g * m * h
    return e


r = calcula_energia_potencial_gravitacional(30, 12)
print(r)

r1 = calcula_energia_potencial_gravitacional(30, 12, 9)
print(r1)
help(calcula_energia_potencial_gravitacional)
