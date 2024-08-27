
# Variáveis
larg = float(input("Insira a largura da parede: "))
alt = float(input("Insira a altura da parede: "))

# Cálculo das variáveis
ar = larg * alt

# Resultado
print('A dimensão da parede é de {}x{} e sua área é de {:.1f}m²'.format(larg, alt, ar))
tinta = ar / 2
print('Para pintar essa parede, vc precisará de {}l de tinta.'.format(tinta))