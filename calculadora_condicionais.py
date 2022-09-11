o = input('Escolha um operador: +, -, /, *\n')

if o == '+':
    print('Operador de soma selecionado')
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    c = a + b
    print('O resultado é, ', c)

elif o == '-':
    print('Operador de menos selecionado')
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    c = a - b
    print('O resultado é, ', c)

elif o == '/':
    print('Operador de divisão selecionado')
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    c = a / b
    print('O resultado é, ', c)

elif o == '*':
    print('Operador de multiplicação selecionado')
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    c = a * b
    print('O resultado é, ', c)

else:
    print('Você selecionou um operador inválido!')