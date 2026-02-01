
print("Bem-vindo a calculadora de contas residenciais")
input()
print("--- Vamos pegar as informações da casa ---")
input()

qtd_pessoas = int(input("Digite a quantidade de pessoas na casa: "))

conta_luz = float(input("Digite aqui o valor da conta de Luz: "))
conta_gas = float(input("Digite aqui o valor da conta de Gás: "))
conta_internet = float(input("Digite aqui o valor da conta da Internet: "))
conta_aluguel = float(input("Digite aqui o valor do Aluguel: "))
conta_condominio = float(input("Digite aqui o valor do Condominio: "))

conta_total = conta_luz + conta_gas + conta_internet + conta_aluguel + conta_condominio
conta_dividida = conta_total / qtd_pessoas

print(f"Esse é o valor total a ser pago: {conta_total:.2f}")
print(f"Cada um deverá pagar: {conta_dividida:.2f}")