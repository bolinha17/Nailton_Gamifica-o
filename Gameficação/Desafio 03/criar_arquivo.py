x = input('Digite sua frase: ')

def criar_arquivo(x):
    with open('Resultado Frase.txt','w') as a:
        a.write(x)

criar_arquivo(x)