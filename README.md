# Maíra: Herdeira do Trovão

Jogo de história com batalhas por turnos, feito em **Python** com **pygame**.

A história se passa em 1500, no litoral brasileiro. Maíra, uma jovem guerreira, vê sua aldeia ser atacada e parte em uma jornada de coragem, perda e descoberta, inspirada na cultura e nos mitos indígenas.

<!-- Adicione aqui um print ou GIF do jogo. Exemplo:
![Tela do jogo](docs/print.png)
-->

## Recursos

- História dividida em **5 capítulos**, com diálogos, retratos e cenários
- **Batalhas por turnos** com ataque básico, ataque especial e energia
- **Seleção de equipe** com vários personagens (Maíra, Caubi, Jaciara, Akin, Curupira, Guaraci e Jaci)
- **Fundos animados em vídeo**, com som ambiente
- Falas separadas do código das batalhas, o que facilita editar a história

## Requisitos

- Python 3.10 ou superior
- Bibliotecas: `pygame` e `opencv-python` (listadas no `requirements.txt`)

## Como instalar e jogar

1. Baixe ou clone o repositório:

   ```bash
   git clone https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git
   cd NOME-DO-REPOSITORIO
   ```

2. Instale as bibliotecas:

   ```bash
   pip install -r requirements.txt
   ```

   No Windows, se o comando acima não funcionar, use `py -m pip install -r requirements.txt`.

3. Rode o jogo:

   ```bash
   python main.py
   ```

   No Windows, também pode usar `py main.py`.

> Se o OpenCV não estiver instalado, o jogo ainda funciona, mas usa imagens paradas no lugar dos vídeos de fundo.




## Estrutura do projeto

```
.
├── main.py            # Janela, telas, batalhas e controle do jogo
├── personagem.py      # Classe Personagem (heróis)
├── vilao.py           # Classe Vilao (herda de Personagem)
├── roteiro.py         # Falas do capítulo 1
├── capitulo2.py       # Falas do capítulo 2
├── capitulo3.py       # Falas do capítulo 3
├── capitulo4.py       # Falas do capítulo 4
├── capitulo5.py       # Falas do capítulo 5
├── requirements.txt   # Bibliotecas necessárias
└── assets/            # Imagens, vídeos de fundo e sons
```

## Conceitos de programação usados

Este projeto também serve como estudo de Python. Os principais conceitos aparecem assim:

- **Listas:** equipe do jogador, lista de inimigos e personagens desbloqueados
- **Tuplas:** cada fala da história é uma tupla `(cenário, personagem, texto)`, e também os status fixos e as cores
- **Dicionários:** ligam nomes às imagens (`RETRATOS`, `PORTRAITS`, `ACTORS`) e aos status dos personagens
- **Programação orientada a objetos:**
  - `Personagem` define atributos e métodos como `ataque`, `downgrade_vida` e `esta_vivo`
  - `Vilao` **herda** de `Personagem` e reescreve o método `ataque` (polimorfismo)
  - `VideoBG` toca os fundos em vídeo e o som ambiente

## Tecnologias

- [Python](https://www.python.org/)
- [pygame](https://www.pygame.org/)
- [OpenCV](https://opencv.org/) (leitura dos vídeos de fundo)

## Autor

Feito por **SEU NOME**.

<!-- Se quiser, adicione um link: [GitHub](https://github.com/SEU-USUARIO) -->

## Licença

Defina aqui a licença do projeto (por exemplo, MIT) ou informe que os direitos são reservados.
