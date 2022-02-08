notas = soma = media = 0

for _ in range(0, 5):
    notas = float(input('Digite a nota: '))
    soma += notas

media = soma / 5
print(media)
