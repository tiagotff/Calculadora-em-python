
print('*******************************************************************')
print('*************************Python Calculator*************************')
print('*******************************************************************')
print('\n')
print('Selecione o número da operação desejada:')
print('\n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('\n')
opcao = int(input('Digite a opção desejada (1 ou 2 ou 3 ou 4): '))

primeiroNum = int(input('Digite o primeiro número: '))
segundoNum = int(input('Digite o segundo número: '))

soma = primeiroNum + segundoNum
subtracao = primeiroNum - segundoNum
multiplicacao = primeiroNum * segundoNum
divisao = primeiroNum / segundoNum

if opcao == 1:
    print('{}+{}={}'.format(primeiroNum, segundoNum, soma))
elif opcao == 2:
    print('{}-{}={}'.format(primeiroNum, segundoNum, subtracao))
elif opcao == 3:
    print('{}*{}={}'.format(primeiroNum, segundoNum, multiplicacao))
elif opcao == 4:
    print('{}/{}={}'.format(primeiroNum, segundoNum, divisao))
else:
    print('Opção inválida! A opção indicada não está disponível ! Tente novamente !')







