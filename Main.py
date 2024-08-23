class Main:
    pass

print("Iniciando Projeto!!!")

from Cliente import Cliente
from Conta  import Conta

c1 = Cliente ("Pedro Pedroso", "077.202.869-99")
conta1 = Conta (c1.nome, '0101', '6500')

print("Titular da conta:",conta1.titular+"\nCPF:",c1.cpf, "\nconta número:", conta1.conta+"\nSaldo dinsponível:", conta1.saldo,"Reais")