class Humano:
    # atributo de classe
    especie = 'Homo Sapiens'

    def __init__(self, nome):
        self.nome = nome

    def das_cavernas(self):
        self.especie = 'Homo Neanderthalensis'
        return self
        # atributos de instância sobrepõem atributos de classe

    @staticmethod
    def especies():
        adjetivos = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopiteco',) + tuple(f'Homo {adj}' for adj in adjetivos)

    @classmethod
    def is_evoluido(cls):
        return cls.especie == cls.especies()[-1]


class Neaderthal(Humano):
    especie = Humano.especies()[-2]


class HomoSapiens(Humano):
    especie = Humano.especies()[-1]


if __name__ == '__main__':
    jose = HomoSapiens('José')
    grokn = Neaderthal('Grokn')
    print(
        f'Evolução (a partir da classe): {", ".join(HomoSapiens.especies())}')
    print(f'Evolução (a partir da instância): {", ".join(jose.especies())}')
    print(f'Homo Sapiens evoluido? {HomoSapiens.is_evoluido()}')
    print(f'Neanderthal evoluido? {Neaderthal.is_evoluido()}')
    print(f'José evoluido? {jose.is_evoluido()}')
    print(f'Grokn evoluido? {grokn.is_evoluido()}')
