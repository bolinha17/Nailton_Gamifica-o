soma = 0

with open('Numbers.txt','r') as arquivo:
    try:   
        for linha in arquivo:
            numero = float(linha)
            if numero % 3 == 0:
                soma += numero
    except ValueError:
        print('Valor Invalido!')
print(soma)