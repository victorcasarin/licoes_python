#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

itens = ('Pedra', 'Papel','Tesoura')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('\033[1mPO!!!\033[m')
sleep(0.5)
print('-=' * 11)
print(f'Computador Jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('\033[34mEMPATE\033[m')
    elif jogador == 1:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[31mO COMPUTADOR VENCEU!!!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador ==1: # computador jogou PAPEL
    if jogador == 0:
        print('\033[31mO COMPUTADOR VENCEU!!!\033[m')
    elif jogador == 1:
        print('\033[34mEMPATE\033[m')
    elif jogador == 2:
        print('\033[32mVOCÊ VENCEU!!!\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('\033[32mVOCÊ VENCEU\033[m')
    elif jogador == 1:
        print('\033[31mO COMPUTADOR VENCEU!!!\033[m')
    elif jogador == 2:
        print('\033[34mEMPATE\033[m')
    else:
        print('JOGADA INVÁLIDA')

