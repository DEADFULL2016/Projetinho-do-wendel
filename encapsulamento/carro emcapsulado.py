class carro_encapsulado():
    def __init__(self, Modelo,marca,traçao,carroceria,quilometragem,combustivel,motor):
        self.__Modelo = Modelo
        self.__Marca = marca
        self.__traçao = traçao
        self.__Tipo_de_Carroceria = carroceria
        self.__Quilometragem = quilometragem
        self.__Tipo_de_combustível = combustivel
        self.__Motor = motor

    def setModelo(self, Audi):
        self.__Modelo = Audi

    def getModelos(self):
        return self.__Modelo
    
    def setModelo(self, modelo):
        self.__Modelo = modelo