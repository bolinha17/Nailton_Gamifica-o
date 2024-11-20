with open('DesafioFinal.txt', 'r', encoding='utf-8') as a:
    with open('Resultado.txt', 'w', encoding='utf-8') as r:
        for linha in a:
            palavra = linha.strip()
            if palavra.startswith('B') and palavra.endswith('o'):
                r.write(palavra +'\n')


