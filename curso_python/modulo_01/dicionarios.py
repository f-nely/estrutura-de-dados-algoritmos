coleta = {'Aedes aegypt': 32, 'Aedes albopictus': 22, 'Anopheles darlingi': 14}
print(coleta['Aedes aegypt'])
coleta['Rhodnius montenegrensis'] = 11  # criando novo elemento
print(coleta)
del coleta['Aedes albopictus']  # deletando elemento
print(coleta)
print(coleta.items())
print(coleta.keys())
print(coleta.values())

coleta2 = {'Anopheles gambiae': 13, 'Anoplheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

for especie, num_especimes in coleta.items():
    print(f'Espécie: {especie}, número de espécimes coletada: {num_especimes}')
