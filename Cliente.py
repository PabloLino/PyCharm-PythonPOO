class Cliente:
    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    #Encapasulamento, vou adicionar um "_" em nome e cpf, tornando-os privados.
    #Ainda podem ser acessados, mas não é o ideal tendo em vista a Convenção em python.

    #Metodo get
    def get_nome(self):
        return self._nome

    #Metodo set
    def set_nome(self, nome):
        self._nome = nome
