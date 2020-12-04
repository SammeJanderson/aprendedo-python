# Declarando um variavel
a = 1
b = 5
c = True
d = 1.2
e = 1.56545

soma = a + b
nome = 'samme janderson'

# printando
print(a,
      b,
      c,
      d,
      e,
      soma,
      nome)

#Convertendo tipos

print(type(a))
print(type(str(a)))
print('soma : ' + str(soma))
x = '3'
soma2 = int(x)+b
print(soma2)

#print with format

print('soma : {}'.format(soma))
print('soma : {}. soma2 : {}'.format(soma, soma2))
print('\n\nsoma : {soma}. \nsoma2 : {soma2}. \nmeu nome : {nome}'.format(soma=soma, soma2=soma2, nome=nome))

#trabalhando com inputs

dig1 = input('entre com o primeiro valor\n')
dig2 = input('entre com o segundo valor\n')
soma3 = int(dig1)+int(dig2)
print('o resultado é da soma é : {}'.format(soma3))

#ou

dig3 =  int(input('entre com o primeiro valor\n'))
dig4 = int(input('entre com o segundo valor\n'))
soma4 = dig3 + dig4
print('o resultado é da soma é : {}'.format(soma4))







