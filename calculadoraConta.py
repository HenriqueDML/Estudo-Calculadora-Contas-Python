
print("Bem-vindo a calculadora de contas residenciais")
input()
print("--- Vamos pegar as informações da casa ---")
input()

qtd_morador = int(input("Digite quantas pessoas vão pagar a contas: "))
lista_pagador = []
qtd_pagador = lista_pagador
while len(lista_pagador) < qtd_morador:
    nome_morador = str(input("Digite o nome da primeira pessoa"))
    lista_pagador.append(nome_morador)
print(lista_pagador)

"""
#qtd_pessoas = numero de nomes na lista

conta_luz = float(input("Digite aqui o valor da conta de Luz: "))
conta_gas = float(input("Digite aqui o valor da conta de Gás: "))
conta_internet = float(input("Digite aqui o valor da conta da Internet: "))
conta_aluguel = float(input("Digite aqui o valor do Aluguel: "))
conta_condominio = float(input("Digite aqui o valor do Condominio: "))

conta_total = conta_luz + conta_gas + conta_internet + conta_aluguel + conta_condominio
conta_dividida = conta_total / qtd_pessoas

print(f"Esse é o valor total a ser pago: {conta_total:.2f}")
print(f"Cada um deverá pagar: {conta_dividida:.2f}")"""