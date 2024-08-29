from personagens import Hero, Inimigo
from armas import iron_sword, Axe

hero = Hero(nome="Hero", dano=10, level=1, hp=100, velocidade=10, exp=0, arma=iron_sword, multi_crit=2, taxa_crit=0.2)
inimigo = Inimigo(nome="Goblin", dano=5, level=1, hp=150, velocidade=5, exp=20, arma=Axe, multi_crit=2, taxa_crit=0.2)

while hero.hp > 0 and inimigo.hp > 0:
    print(f"""
{hero.nome} HP: {hero.hp}
{inimigo.nome} HP: {inimigo.hp}
""")
    
    if hero.hp > 0:
        hero.atacar(inimigo)
    if inimigo.hp > 0:
        inimigo.atacar(hero)