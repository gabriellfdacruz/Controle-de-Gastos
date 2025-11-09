import os 
def limpar_tela():
    os.system('clear')

def coletar_conta(tipo):
    contas = {}
    qtd = int(input(f'Insira a quantidade de contas {tipo}: '))
    limpar_tela()

    for i in range(qtd):
        n = str(input(f'Digite o nome da {i+1}ª conta fixa: '))
        num = float(input('Digite o valor da conta: '))
        contas_fixas.update({n : num})
        limpar_tela()
    return contas

renda = float(input('Digite o valor de sua renda total: '))
limpar_tela()

contas_fixas = coletar_conta('fixas')
contas_eventuais = coletar_conta('eventuais')
investment = coletar_conta('insvestimentos')


v_fix = sum(contas_fixas.values())
por_fix = ( v_fix / renda) * 100

v_even =  sum(contas_eventuais.values())
por_even = ( v_even / renda) * 100

v_inv = sum(investment.values())
p_inv = ( v_inv / renda ) * 100

restante = renda - (v_even + v_fix + v_inv)

print("\n===== RESUMO FINANCEIRO =====")
print(f"Gastos Fixos: R$ {v_fix:.2f} ({por_fix:.2f}%)")
print(f"Gastos Eventuais: R$ {v_even:.2f} ({por_even:.2f}%)")
print(f"Investimentos: R$ {v_inv:.2f} ({p_inv:.2f}%)")
print(f"Saldo Restante: R$ {restante:.2f}")
print("==============================")
