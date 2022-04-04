num = []
soma = 0
for i in range(0, 5):
    num.append(int(input('Digite um valor: ')))
    soma += num[i]

print(num)
print(f'A soma: {soma}')
