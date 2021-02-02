
print('*******************************************************************')
print('*************************Python Calculator*************************')
print('*******************************************************************')
print('\n')
print('Digite, abaixo, o número da opção desejada: ')
print('\n')
print('1-Soma')
print('2-Subtração')
print('3-Multiplicação')
print('4-Divisão')
print('\n')

opcao = int(input('Informe a opção desejada: ou 1 ou 2 ou 3 ou 4: '))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

def add (x,y):
    return x + y

def subtract (x,y):
    return x - y

def multiply (x,y):
    return x * y

def divide (x,y):
    return x / y

if opcao == 1:
    print(num1, '+', num2, '=', add(num1, num2))
elif opcao == 2:
    print(num1, '-', num2, '=', subtract(num1, num2))
elif opcao == 3:
    print(num1, '*', num2, '=', multiply(num1, num2))
elif opcao == 4:
    print (num1, '/', num2, '=', divide(num1, num2))
else:
    print ('Opção inválida. Tente novamente !')

