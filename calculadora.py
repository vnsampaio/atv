print('1 - SOMAR, 2 - SUBTRAIR, 3 - MULTIPLICAR, 4 - DIVIDIR')
operacao = int(input('CALCULADORA - ESCOLHA SUA OPERAÇÃO: '))

while operacao < 0 or operacao > 4:
    print('OPERAÇÃO NÃO ENCONTRADA!')
    print('1 - SOMAR, 2 - SUBTRAIR, 3 - MULTIPLICAR, 4 - DIVIDIR')
    operacao = int(input('CALCULADORA - ESCOLHA SUA OPERAÇÃO: '))
if operacao == 1:
    print('OPERAÇÃO ESCOLHIDA: SOMA')
    n1 = float(input('Digite o Primeiro número: '))
    n2 = float(input('Digite o Segundo número: '))
    resultado = n1 + n2
    print(f'O resultado da operação é: {resultado}')
elif operacao == 2:
    print('OPERAÇÃO ESCOLHIDA: SUBTRAIR')
    n1 = float(input('Digite o Primeiro número: '))
    n2 = float(input('Digite o Segundo número: '))
    resultado = n1 - n2
    print(f'O resultado da operação é: {resultado}')
elif operacao == 3:
    print('OPERAÇÃO ESCOLHIDA: MULTIPLICAR')
    n1 = float(input('Digite o Primeiro número: '))
    n2 = float(input('Digite o Segundo número: '))
    resultado = n1 * n2
    print(f'O resultado da operação é: {resultado}')
elif operacao == 4:
    print('OPERAÇÃO ESCOLHIDA: DIVIDIR')
    n1 = float(input('Digite o Primeiro número: '))
    n2 = float(input('Digite o Segundo número: '))
    resultado = n1 / n2
    print(f'O resultado da operação é: {resultado}')
    


