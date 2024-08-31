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
            print("ATENÇÃO: Seu saldo está negativo")
            self.saldo = saldo  # Define saldo como 0 se o valor for negativo
        else:
            self.saldo = saldo
