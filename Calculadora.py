operação = input('escolhar uma função \n1.soma\n2.subtração\n3.multiplicação\n4.divisão')

a = int(input('digite o primeiro digito'))
b = int(input('digite o segundo numero'))

if operação == '1':
    print('{} + {} = {}'.format(a,b,a+b))
elif operação == '2':
    print('{} - {} = {}'.format(a, b, a - b))
elif operação == '3':
    print('{} * {} = {}'.format(a, b, a * b))
elif operação == '4':
    print('{} / {} = {}'.format(a, b, a / b))

