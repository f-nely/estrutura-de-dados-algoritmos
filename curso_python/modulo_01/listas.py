lista1 = ['Amarok', 'Jeep Compass', 'Renegade']
print(lista1)
lista1.append('Duster')  # adicionando elemento da lista
print(lista1)
lista2 = ['Jetta', 'Cruzes', 'Honda Civic', 'Argo', 'Cronos']
print(lista2)
lista2.remove('Cruzes')  # removendo elemento da lista
print(lista2)

lista3 = lista1 + lista2
for elemento in lista3:
    print(elemento)

lista1_2 = lista1 * 2
print(lista1_2)
print(lista1_2[0])
print(lista1_2[0:2])
#  del lista1_2 - removendo lista

