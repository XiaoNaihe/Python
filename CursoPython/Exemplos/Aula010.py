n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua media é: {}'.format(m))
if m >= 7.0:
    print('Sua media foi boa! PARABÉNS')
else:
    print('Sua media foi ruim! ESTUDE MAIS!!!')