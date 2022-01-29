a = 'casaco'
print(a)

maiuscula = a.upper()
print(maiuscula)

minuscula = maiuscula.lower()
print(minuscula)

capital = a.capitalize()
print(capital)

metade_palavra = a[0:4]
print(metade_palavra)

ultima_letras = a[3:]
print(ultima_letras)

b = a.replace('aco', 'inha')
print(a)
print(b)

c = a.replace('o', 'a')
print(c)

print(c.find('s'))
print(c.find('a'))
print(c.find('y'))

e = ' casaco '
print(len(e))

f = e.strip()
print(len(f))

n1 = 14
n2 = 16

print(f'Dividindo {n1} por {n2} o resultado é {n1/n2}')
