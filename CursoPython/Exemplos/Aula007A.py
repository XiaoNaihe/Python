n1 = int(input('Um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, O Produto é {} e a Divisão é {:.3}'.format(s, m, d), end=' ')
print('A Divisão inteira é {} e Potência {}'.format(di, e))
