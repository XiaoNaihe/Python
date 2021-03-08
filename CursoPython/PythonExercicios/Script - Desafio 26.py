frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira posição que foi encontrada a letra A foi: {}'.format(frase.find('A')+1))
print('A Ultima posição que foi encontrada a letra A foi: {}'.format(frase.rfind('A')+1))