larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('sua parede tem a dimensão{}x{} e sua area é de {}².'.format(larg, alt, area))
tinta = area / 2
print('para pintar essa parede você precisa de {}L de tinta'.format(tinta))