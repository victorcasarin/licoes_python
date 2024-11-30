#Faça um programa que tenha uma função chamada área(), que receba as dimensões
# de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def linha():
    print('-' * 30)

def area(l, c):
    a = l * c
    print(f'A área de um terrno {l} por {c} é de {a}m².')

linha()
print('    CONTROLE DE TEREENOS')
linha()
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)