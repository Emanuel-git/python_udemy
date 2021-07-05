class Carro:
    def __init__(self, velocidadeMax):
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual = 0

    def acelerar(self, delta=5):
        self.velocidadeAtual += delta
        if (self.velocidadeAtual > self.velocidadeMax):
            self.velocidadeAtual = self.velocidadeMax
        return self.velocidadeAtual

    def frear(self, delta=5):
        self.velocidadeAtual -= delta
        if (self.velocidadeAtual < 0):
            self.velocidadeAtual = 0
        return self.velocidadeAtual


if __name__ == '__main__':
    c1 = Carro(180)

    for _ in range(25):
        print(c1.acelerar(8))

    for _ in range(10):
        print(c1.frear(delta=20))
