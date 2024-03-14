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