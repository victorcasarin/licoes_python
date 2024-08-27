s = float(input('Salário atual:R$'))
a = float(input('O aumento em porcentagem é de:'))
sn = s * a / 100
au = s + sn

print('O aumento é de R${:.2f}, então o salário do funcionário vai para R${:.2f}'.format(sn, au))
