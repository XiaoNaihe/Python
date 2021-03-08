Preco = float(input('qual é o preço do produto? R$ '))
Novo = Preco - (Preco * 5 / 100)
print('O produto que custava R${:.2f} na promoção com desconto de 5% vai custar R${:.2f}'.format(Preco, Novo))