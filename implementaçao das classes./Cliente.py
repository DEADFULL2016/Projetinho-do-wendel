import pessoa
from pessoa import pessoa    

class cliente(pessoa):
    def __init__(self, nome, nascimento,cpf,rg,cep):
        super().__init__(nome, nascimento, )
        self.__CPF = cpf
        self.__RG = rg
        self.__CEP = cep
    def efetua_pagamento(self):
        print("Pagamento efetuado com sucesso!")
    def cancela_pagamento(self):
        print("Pagamento cancelado com sucesso!")    
       







