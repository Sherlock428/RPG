import random

class Personagem:
    def __init__(self,
                 nome: str,
                 dano: int,
                 hp: int,
                 velocidade: int,
                 level: int,
                 multi_crit: float,
                 taxa_crit: float,
                   ) -> None:
        
        self.nome = nome
        self.dano = dano
        self.hp = hp
        self.hp_max = hp
        self.velocidade = velocidade
        self.level = level
        self.multi_crit = multi_crit
        self.taxa_crit = taxa_crit

    def atacar(self, alvo):
        dano_final = self.dano + self.arma.dano
        if random.random() <= self.taxa_crit:
            dano_final *= self.multi_crit
            print(f"[Critical] {self.nome} Acertou critico em {alvo.nome} Causando {dano_final}")

        else:
            print(f"{self.nome} Atacou {alvo.nome} causando {dano_final}")
        
        alvo.hp -= dano_final
        alvo.hp = max(alvo.hp, 0)

class Hero(Personagem):
    def __init__(self, nome: str, dano: int, hp: int, velocidade: int, level: int, multi_crit: float, taxa_crit: float, exp: int, arma) -> None:
        super().__init__(nome, dano, hp, velocidade, level, multi_crit, taxa_crit)
        self.exp = exp
        self.exp_max = 20 * 1.5
        self.arma = arma

class Inimigo(Personagem):
    def __init__(self, nome: str, dano: int, hp: int, velocidade: int, level: int, multi_crit: float, taxa_crit: float, exp: int, arma) -> None:
        super().__init__(nome, dano, hp, velocidade, level, multi_crit, taxa_crit)
        self.exp = exp
        self.arma = arma
