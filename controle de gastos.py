import os 
os.system('clear')

contas_fixas = {}
contas_eventuais = {}
investment = {}

renda = float(input('Insira sua renda total (insira o decimal com ponto sendo exemplo 0.1): '))

os.system('clear')

cont_fix = int(input('Insira a quantidade de contas fixas (valores que não se alteram com tempo): '))

os.system('clear')

for _ in range(cont_fix):
    n = str(input(f'Digite o nome da {_+1}° conta fixa: '))
    num = float(input('Digite o valor da conta: '))
    contas_fixas.update({n : num})
    os.system('clear')

cont_event = int(input('Insira a quantidade de contas eventuais (valores que podem variar com tempo): '))

for _ in range(cont_event):
    v = str(input(f'Digite o nome da {_+1}° conta eventual: '))
    valor = float(input('Digite o valor da conta:'))
    contas_eventuais.update({v : valor})
    os.system('clear')

invest = int(input('Insira a quatidades de seus investimentos (pensando como FI, CDB, e etc): '))

for _ in range(invest):
    i = str(input(f'Insira o nome do {_+1}° investimento: '))
    inv = float(input('Insira o valor do investimento: '))
    investment.update({ i : inv })
    os.system('clear')

os.system('clear')

print("\nEsses sãos os valores das contas fixas: ")

for chave, valor in contas_fixas.items():
    print(f"{chave}: {valor}")
v_fix = sum(contas_fixas.values())
por_fix = ( v_fix / renda) * 100
print(f'A porcentagem de gastos fixos é {por_fix:.2f}%.')

print("\nEsses sãos os valores das contas eventuais: ")

for chave, valor in contas_eventuais.items():
    print(f"{chave}: {valor}")
v_even =  sum(contas_eventuais.values())
por_even = ( v_even / renda) * 100
print(f'A porcentagem de gastos eventuais é {por_even:.2f}%.')

print("\nEsses sãos os valores das contas dos investimentos: ")

for chave, valor in investment.items():
    print(f"{chave}: {valor}")
v_inv = sum(investment.values())
p_inv = ( v_inv / renda) * 100
print(f'A porcentagem de investimentos {p_inv:.2f}%.')

restante = renda - (v_even + v_fix + v_inv)

print (f'seu restante é de {restante:.2f}.')
