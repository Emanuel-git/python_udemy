class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
        # atributos de instância sobrepõem atributos de classe


if __name__ == '__main__':
    jose = Humano('José')
    grokn = Humano('Grokn').das_cavernas()

    print(f'Humano.epecie: {Humano.especie}')
    print(f'jose.epecie: {jose.especie}')
    print(f'grokn.epecie: {grokn.especie}')
