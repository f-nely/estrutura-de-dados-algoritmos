alunos = {}

for i in range(0, 3):
    nome = str(input('Digite o nome: '))
    nota = float(input('Digite a nota: '))
    alunos[nome] = nota

print(alunos)

soma = 0
for nota in alunos.values():
    print(nota)
    soma += nota

print(f'Média: {soma / 3}')
