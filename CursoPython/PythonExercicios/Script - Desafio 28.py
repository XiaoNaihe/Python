from random import randint
from time import sleep
computador = randint(0, 5)  # faz o computador "pensar"
print('-=--=-=-=--=- '*20)
print('Vou pensar em um numero entre 0 e 5. tente advinhar... ')
print('-=--=-=-=--=- '*20)
jogador = int(input('Em que número eu pensei? '))  # jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens você conseguiu me vencer!')
else:
    print('GANHEI !!! Eu pensei no numero {} e não no {}'.format(computador, jogador))