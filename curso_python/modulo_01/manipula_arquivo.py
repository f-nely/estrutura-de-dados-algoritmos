# with open('frase.txt', 'r') as arquivo:
#     texto = arquivo.read()
#     print(texto)
#
# with open('arquivo_teste', 'w') as arquivo_teste:
#     arquivo_teste.write('Good Evening!\n')
#
# with open('arquivo_teste', 'r') as ar:
#     print(ar.read(), end='')

with open('frase1.txt', 'w') as text:
    text.write('Learn Python Programming!\n')
    text.write('Python is a powerful general-purpose programming language.\n')
    text.write('It is used in web development, data science, creating software prototypes, and so on.\n')
    text.write('Fortunately for beginners, Python has simple easy-to-use syntax.\n')
    text.write('This makes Python an excellent language to learn to program for beginners.\n')

# with open('frase1.txt', 'r') as tex:
#     for linha in tex:
#         print(linha)

with open('frase1.txt', 'r') as tex:
    r = tex.readlines()
    print(r)
