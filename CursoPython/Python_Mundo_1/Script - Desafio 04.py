a = input('Digite algo: ')
print(f'Só tem espaços? {a.isspace()}')
print(f'É numérico? {a.isnumeric()}')
print(f'É alfabético? {a.isalpha()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'Está em letras maiúsculas?{a.isupper()}')
print(f'Está em letras minúsculas? {a.islower()}')
print(f'Está capitalizada? {a.istitle()}')

#versão 3.7 do python não precisa mais usar .format (), apenas coloque um f antes das aspas " "
#e escreva o nome da variavel dentro dos colchetes {}  exemplo: print (f'A soma de {n1} e {n2} é {s}')