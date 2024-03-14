# Desafio Target

## Sobre mim
Olá, eu sou a Gabrielle e tenho 19 anos!

Sou apaixonada por Técnologia e Matemática desde pequena, estou em busca de uma  oportunidade onde possa contribuir com minhas habilidades técnicas e
crescer profissionalmente, e onde eu possa colaborar com uma equipe.

## Meus Hobbies
- Fazer trilhas e acampar
- Viajar
- Ler
- Assistir documentários,séries e filmes
- Praticar esportes
- Jogar

## Linguagens e ferramentas
Estas são algumas ferramentas e linguagens que possuo algum contato inicial:
- HTML
- CSS
- JavaScript
- Python
- PySpark
- SQL
- Git and GitHub

## Idiomas
- Inglês (intermediário)


## Resoluçaõ dos desafios
Estou realizando o processo seletivo da vaga Estágio Desenvolvedora (Vaga afirmativa Feminina) - São Paulo, onde desenvolvi as resoluções dos desafios que foram propostos pela vaga.

Os códigos a seguir foram realizados em minha autoria para completar o desafio da Target Sistemas:

### Desafio 2

Link para o código fonte, caso prefira: [Script Desafio 2](desafio_2.py)

Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

Resolução:
```
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

```

### Desafio 3
Link para o código fonte, caso prefira: [Script Desafio 3](desafio_3.py)
Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
- O menor valor de faturamento ocorrido em um dia do mês;
- O maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
  
Resolução:
```
import json

with open('dados.json','r') as file:
    data = json.load(file)

max_value = max(data, key=lambda x: x['valor'])['valor']
min_value = min(x['valor'] for x in data if x['valor'] != 0) #Ignorando os 0 
days_worked = sum(1 for x in data if x['valor'] != 0)
average_monthly = sum(x['valor'] for x in data) / days_worked
days_average = sum(1 for x in data if x['valor'] > average_monthly)

print(f'O menor valor ocorrido em um dia do mês foi de: {min_value}')
print(f'O maior valor ocorrido em um dia do mês foi de: {max_value}')
print(f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal é de: {days_average} dias')
```

### Desafio 4
Link para o código fonte, caso prefira: [Script Desafio 4](desafio_4.py)
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
  
Resolução:
```
data = [
    {
     'Estado' : 'SP',
     'Valor': 67836.43
    },
    {
     'Estado' : 'RJ',
     'Valor': 36678.66
    },
    {
     'Estado' : 'MG',
     'Valor': 29229.88
    },
    {
     'Estado' : 'ES',
     'Valor': 27165.48
    },
    {
     'Estado' : 'Outros',
     'Valor': 19849.53
    },
]

monthly_revenue = sum(x['Valor'] for x in data)
for state in data:
    percentual = (state['Valor'] / monthly_revenue) * 100
    print(f"O percentual de representação de {state['Estado']} é de: {percentual:.1f}%") 
```

### Desafio 5
Link para o código fonte, caso prefira: [Script Desafio 5](desafio_5.py)
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
- Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
- Evite usar funções prontas, como, por exemplo, reverse;

Resolução:
```
while True:

    print('Bem vindo ao programa que inverte palavras!')
    word = input('Digite uma palavra ou se deseja sair digite 1: ')
    if word == '1':
        break
    inverted_word = word[::-1]
    print(f'A palavra {word} invertida fica {inverted_word} \n')
```




