class Carro:
    def __init__(self, consumoCombustivel, quantidadeDeCombustivelNoTanque = 0.00):
        self.consumoCombustivel = consumoCombustivel
        self.quantidadeDeCombustivelNoTanque = quantidadeDeCombustivelNoTanque
    
    def andar(self, dist):
        combustivelNecessario = dist / self.consumoCombustivel
        if combustivelNecessario <= self.quantidadeDeCombustivelNoTanque:
            self.quantidadeDeCombustivelNoTanque -= combustivelNecessario
            print("O Carro percorreu ", dist, " km.")
        else:
            print("O Carro não possui combustível suficiente para percorrer a distância desejada.")

        
    def abastecer(self, qtde):
        self.quantidadeDeCombustivelNoTanque += qtde
        print("Carro abastecido com ", qtde, " litros de combustível.")
    
