while True:

    print('Bem vindo ao programa que inverte palavras!')
    word = input('Digite uma palavra ou se deseja sair digite 1: ')
    if word == '1':
        break
    inverted_word = word[::-1]
    print(f'A palavra {word} invertida fica {inverted_word} \n')