# Tratamento de erros e exceções

"""
- NameError: variável nao foi definida
- TypeError: tipos de dados incompatíveis
- RuntimeError: erro de execução
- SyntaxError: sintaxe digitada é inválida e não reconhecida pelo interpretador
- ZeroDivisionError: divisão por zero
- IndexError: índice está fora da coleção
"""

# try:
#     n = int(input('Digite um número inteiro: '))
# except:
#     print('Valor inválido!')
# else:
#     print(f'Valor digitado é {n}')

while True:
    try:
        num = int(input('Digite um número inteiro: '))
    except ValueError:
        print('Valor inválido')
    except KeyboardInterrupt:
        print('\nUsuário interropeu a execução')
        break
    else:
        print(f'Valor digitado é {num}')
        break