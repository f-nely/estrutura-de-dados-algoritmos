j = 0
soma = 0
media = 0
notas = 0

while j < 5:
    notas = float(input("Digite a nota: "))
    soma += notas
    # print(s)
    j += 1

media = soma / 5
print(media)
