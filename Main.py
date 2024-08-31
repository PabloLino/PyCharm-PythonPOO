class Main:
    pass

print("\nIniciando Consulta...")

from Cliente import Cliente
from Conta  import Conta

c1 = Cliente ("Pedro Pedroso", "077.202.869-99")
conta1 = Conta (c1._nome, '0101', -100)

print("\nTitular da conta:",conta1.titular+"\nCPF:",c1._cpf, "\nconta número:", conta1.conta+"\nSaldo dinsponível:", conta1.saldo,"Reais")
