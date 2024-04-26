class Carro():
    def __init__(self,Modelo,Marca,Tração,TC,Km,Combustivel,Motor) :
        self.Modelo = Modelo
        self.Marca = Marca
        self.Traçao = Tração
        self.Tipo_de_Carroceria = TC
        self.Quilometragem = Km
        self.Tipo_de_Combustivel = Combustivel
        self.Motor = Motor

Corsa=Carro("corsa","Chevrolet","Fwd","hatch","221.312,00 km","normal","flex")
print(Corsa.Traçao)