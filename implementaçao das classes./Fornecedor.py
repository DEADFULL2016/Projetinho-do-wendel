import carro
from carro import carro

class Fornecedor(carro):
    def __init__(self, modelos, marca, traçao, carroceria, quilometragem, combustivel, motor, estoque, fornecedores, preco, e, ):
        super().__init__(modelos, marca, traçao, carroceria, quilometragem, combustivel, motor)
        self.__estoque = []
        self.__fornecedores = []
        self.__preco = []
        