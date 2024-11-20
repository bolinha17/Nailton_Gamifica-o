from operadores import soma, subtrair, multiplicar, verificar_par

def calc():
    print(f'Qual operação você gostaria de tentar?: \n + para Adição \n - para Subtração \n * para Multiplicação \n % para Verificar se o número é PAR!')


def escolha():
    calc()
    op = input("Digite a operação que deseja realizar: ")

    if op in ['+', '*', '-']:
        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))
        
        if op == '+':
            print(f"O resultado de {a} + {b} é: {soma.soma(a, b)}!")
        
        elif op == '*':
            print(f'O resultado de {a} * {b} é: {multiplicar.multiplicar(a, b)}!')

        elif op == '-':
            print(f'O resultado de {a} - {b} é: {subtrair.subtrair(a, b)}!')
    
    elif op == '%' :
        a = float(input("Qual o número que deseja verificar: "))
        print(f'{verificar_par.verificar_par(a)}')

    else:
        print("Operação inválida.")
        escolha()
escolha()