class Personagem:
    """
    A classe Personagem representa um personagem do jogo.
    """
    CUSTO_ESPECIAL = 25

    def __init__(self, nome, idade, vida, energia=100, ataque_basico=16, ataque_especial=22):
        self.nome = nome
        self.idade = idade
        self.vida = vida
        self.vida_max = vida
        self.energia = energia
        self.energia_max = energia
        self.ataque_basico = ataque_basico
        self.ataque_especial = ataque_especial

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        self.vida += incremento
        if self.vida > self.vida_max:
            self.vida_max = self.vida
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida(self, dano=15):
        """
        Reduz a vida do personagem, sem deixar ficar negativa.
        """
        self.vida = max(0, self.vida - dano)
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def esta_vivo(self):
        return self.vida > 0

    def ataque(self, alvo, especial=False):
        # Devolve o dano causado, ou None se faltar energia no especial
        if especial:
            if self.energia < self.CUSTO_ESPECIAL:
                return None
            self.energia -= self.CUSTO_ESPECIAL
            dano = self.ataque_especial
        else:
            dano = self.ataque_basico
        print(f'{self.nome} atacou {alvo.nome}!')
        alvo.downgrade_vida(dano)
        return dano

    def __str__(self):
        return f'Personagem: {self.nome}, Idade: {self.idade}, Vida: {self.vida}'
