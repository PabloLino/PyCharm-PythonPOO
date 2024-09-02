class Main:
    pass

print("\nDigite seus dados")

from Cliente import Cliente
from Conta  import Conta

nome_cliente = input("Por favor, insira o nome do cliente: ")
cpf_cliente = input("Por favor, insira o CPF do cliente: ")
print("\nIniciando consulta...")

c1 = Cliente(nome_cliente, cpf_cliente)
##IMPORTANTE: definir aqui o saldo da conta ; )
conta1 = Conta(c1._nome, '0001', 2500)

print("Titular da conta:",conta1.titular+"\nCPF:",c1._cpf, "\nconta número:", conta1.conta+"\nSaldo dinsponível:",
conta1.saldo,"Reais")

# Realizando depósito
valor_deposito = float(input("\nInsira o valor para depósito: "))
conta1.deposita(valor_deposito)
print(f"Você depositou R$ {valor_deposito:.2f}. \nSaldo atualizado: R$ {conta1.get_saldo():.2f}")

# Solicitando valor de saque
valor_saque = float(input("\nInsira o valor para saque: "))
conta1.saque(valor_saque)

#Verifica extrato
conta1.extrato()
