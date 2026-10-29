import random
from personagem import Personagem


class Vilao(Personagem):
    """
    A classe Vilao representa um vilão do jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade, forca=9):
        super().__init__(nome, idade, vida, energia=0, ataque_basico=forca, ataque_especial=forca)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.forca = forca

    def ataque(self, alvo, especial=False, reducao=0):
        # O dano varia um pouco (força -3 até +3)
        dano = random.randint(self.forca - 3, self.forca + 3)
        if reducao:
            dano = max(2, dano - reducao)
        print(f'{self.nome} atacou {alvo.nome}!')
        alvo.downgrade_vida(dano)
        return dano

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
