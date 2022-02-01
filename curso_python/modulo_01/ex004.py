nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))

media = (nota1 + nota2 + nota3) / 3

if (media >= 0.0) and (media <= 4.0):
    print('O aluno está reprovado: ')
elif (media >= 4.1) and (media <= 6.0):
    print('O aluno pegou exame: ')
    exame = float(input('Digite a nota do exame: '))
    if exame >= 6.0:
        print('Aluno está aprovado: ')
    else:
        print('Aluno está reprovado: ')
else:
    print('O aluno está aprovado: ')
