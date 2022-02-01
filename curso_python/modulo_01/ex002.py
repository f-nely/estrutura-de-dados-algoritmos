tempo = int(input('Digite o tempo gasto na viagem: '))
velociade = float(input('Digite a velociade média: '))

distacia = tempo * velociade

litros_usados = distacia / 12

print('A velociade média é: ', velociade)
print('O tempo gasto na viagem é: ', tempo)
print('A quantidade de litros utilizados na viagem é: ', round(litros_usados, 2))
