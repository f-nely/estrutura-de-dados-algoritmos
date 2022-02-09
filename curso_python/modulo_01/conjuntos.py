biomoleculas = ('proteína', 'ácidos nucleicos', 'carboidratos', 'lipídeos',
                'ácidos nucleicos', 'carboidratos', 'carboidratos', 'carboidratos')
print(biomoleculas)
print(set(biomoleculas))  # elementos que não se repetem

c1 = {1, 2, 3, 4, 5}
c2 = {3, 4, 5, 6, 7}
c3 = c1.intersection(c2)
print(c3)
c4 = c1.difference(c2)
print(c4)
