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