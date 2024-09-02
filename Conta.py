class Conta:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.set_saldo(saldo)  #Chama o metodo set_saldo para aplicar a verificação, essa mudança foi feita por conta
#que estava retornando valores negativos ao rodar o main, agora irá primeiro será validado o saldo colocado para depois
#entrar na condição do if posteriormente

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        if saldo < 0:
            print("\nATENÇÃO: Seu saldo está negativo")
            self.saldo = saldo  # Define saldo como 0 se o valor for negativo
        else:
            self.saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saque não realizado, saldo insuficiente, você tentou sacar o valor de R${:.2f}".format(valor))

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        print("Cliente:",self.titular+", Saldo atual: R$",self.get_saldo())
