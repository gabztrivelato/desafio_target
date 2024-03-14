try:
    user_input = int(input('Digite um número inteiro válido de 1 a 100: '))
    fibonacci_sequence = [0,1]
    for n in range(0,101):
        third_number = fibonacci_sequence[n] + fibonacci_sequence[n+1]
        fibonacci_sequence.append(third_number)
    if user_input in fibonacci_sequence:
        print(f'O número {user_input} se encontra na sequência de fibonacci!')
    else:
        print(f'O número {user_input} não se encontra na sequência de fibonacci.')
            

except ValueError:
    print('O valor inserido não é um número inteiro válido.')


