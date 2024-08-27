# Solicita ao usuário para inserir um valor em metros

metros = float(input('Digite um valor em metros: '))

# Converte metros para centímetros e milímetros
cm = metros * 100
mm = metros * 1000
km = metros / 1000
# Exibe os resultados
print('A medida de {}m corresponde a {}cm e {:.0f}mm, e a {:.0f}km.'.format(metros, cm, mm, km))