import math
import datetime
import random
import time as tm

# math
raiz_quadrada = math.sqrt(9)
print(raiz_quadrada)

log = math.log(32, 2)
print(log)

pi = math.pi
print(pi)
print('-=' * 15)

# datetime
print(dir(datetime))
hoje = datetime.date.today()
print(hoje)
hora = datetime.datetime.now()
print(hora)
data = datetime.date(2020, 7, 10)
print(data)
print(data.day)
print(data.month)
print(data.year)
horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print(horario)
print(horario.hour)
print(horario.minute)
print('-=' * 15)

# random
print(random.random())
num_aleatorio = random.randint(1, 5)
print(num_aleatorio)
print(random.randrange(0, 10, 2))
x = ['k', 'd', 13, '34-j', 'x']
print(random.choice(x))
print('-=' * 15)

# time
print(tm.time())
antes = tm.time()
lista = []
for i in range(0, 10000):
    lista.append(i)
depois = tm.time()

intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')

print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')
