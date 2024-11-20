x = input('Digite uma frase: ').capitalize()

def verificar_inicio(): 
    if x.startswith("Olá"):
        print(f'A frase inicia com Olá!')
    else:
        print(f'A frase não inicia com Olá!')

verificar_inicio()