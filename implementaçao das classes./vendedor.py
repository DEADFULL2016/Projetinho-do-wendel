import pessoa
from pessoa import pessoa 

class vendedor(pessoa):
    def __init__(self, nome, nascimento, anos, vendas):
        super().__init__(nome, nascimento, )
        self.__Anos_de_serviço = anos
        self.__vendas = vendas
    def salario(self):
        return self.__Anos_de_serviço * 1000
    def comissao(self):
        return self.__vendas * 0.05
