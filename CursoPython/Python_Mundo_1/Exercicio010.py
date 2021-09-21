real = float(input('Quanto de dinheiro você tem na carteira? '))
dolar = real / 5.43
print('com R${:.2f} vc pode comprar US${:.2f}'.format(real, dolar))