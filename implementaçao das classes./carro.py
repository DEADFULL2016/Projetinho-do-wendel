class carro():
    def __init__(self, Modelo,marca,traçao,carroceria,quilometragem,combustivel,motor):
        self.Modelo = Modelo
        self.Marca = marca
        self.__traçao = traçao
        self.__Tipo_de_Carroceria = carroceria
        self.Quilometragem = quilometragem
        self.Tipo_de_combustível = combustivel
        self.Motor = motor

    def ligar_motor(self):
        print("O carro ligou o motor.")

    def ligar_farol(self):
        print("O carro ligou o farol.") 

    def desligar_farol(self):
        print("O carro desligou o farol.")

    def desligar_motor(self):
        print("O carro desligou o motor.")