class pessoa:
    def __init__(self, nome, nascimento,):
        self.nome = nome
        self.__Nascimento = nascimento
    def calcula_idade(self):
        return 2024 - self.__Nascimento