# Leitura da largura e altura da parede

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

# Cálculo da área da parede
area = largura * altura

# Cálculo da quantidade de tinta necessário
litros_tinta = area / 2

# Exibição dos resultados
print(f'A área da parede é de {area} m².')
print(f'Você precisará de {litros_tinta} litros de tinta para pintá-la.')