class Armas:
    def __init__(self, nome: str, tipo: str, dano: int) -> None:
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        

punch = Armas(nome="Soco", tipo="Melee", dano=1)

iron_sword = Armas(nome="Espada de Ferro", tipo="Melee", dano=10)

bow_arrow = Armas(nome="Arco", tipo="Meelee", dano=5)

Axe = Armas(nome="Machado", tipo="Melee", dano=7)
