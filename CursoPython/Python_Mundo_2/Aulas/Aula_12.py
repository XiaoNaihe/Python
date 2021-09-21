nome = str(input('qual é o seu nome?'))
if nome == 'Gabriel':
    print('que nome mais bonito !')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil !')
elif nome in 'Ana Claudia Jessica Juliana':
    print ('Belo nome feminino')
else:
    print('Seu nome é bem normal !')
print('tenha um bom dia  {}'.format(nome))