# Capítulo 4 — O Despertar dos Deuses
# Formato das falas: (ambiente, personagem, texto)
# Este arquivo contém somente os diálogos. As batalhas e transições são
# controladas pelo main.py.

# CENA 1 — Depois dos acontecimentos do capítulo 3.
# Ao terminar, o main.py deve iniciar a batalha contra 3 Angoeras comuns.
CENA1_4 = [
    ('noite', 'Narrador', 'Depois do encontro com o Boitatá, Maíra e seus companheiros continuaram seguindo pela floresta. A criatura havia falado sobre uma presença sombria que estava despertando, mas não conseguiu explicar sua origem.'),
    ('noite', 'Jaciara', 'Desde que saímos daquela clareira, tenho a sensação de que estamos sendo observados.'),
    ('noite', 'Caubi', 'Eu também percebi. Os sons dos animais desapareceram. Até o vento parece ter parado.'),
    ('noite', 'Akin', 'Isso não é um bom sinal. Quando a floresta fica silenciosa assim, geralmente significa que alguma coisa está por perto.'),
    ('mata_corrompida', 'Curupira', 'A mata está sofrendo. As raízes estão enfraquecendo e os espíritos menores estão fugindo desta região.'),
    ('mata_corrompida', 'Maíra', 'Então a presença que o Boitatá sentiu está causando tudo isso?'),
    ('mata_corrompida', 'Curupira', 'É possível. Mas sinto que há algo ainda mais profundo por trás dessa corrupção.'),
    ('mata_corrompida', 'Caubi', 'Precisamos descobrir o que está acontecendo antes que essa energia alcance outras aldeias.'),
    ('mata_corrompida', 'Maíra', 'Vamos continuar. Não podemos deixar que mais pessoas sofram por causa disso.'),
    ('mata_corrompida', 'Jaciara', 'Esperem! Há alguma coisa se movendo entre as árvores!'),
    ('mata_corrompida', 'Akin', 'Angoeras! Estão vindo em nossa direção!'),
    ('mata_corrompida', 'Maíra', 'Preparem-se! Não deixem que nos cerquem!'),
]

# CENA 1 — FIM
# Diálogos depois da vitória contra os 3 Angoeras comuns.
# A última fala prepara a aparição do Angoera Primordial.
CENA1_4_FIM = [
    ('mata_corrompida', 'Caubi', 'Esses Angoeras estavam muito mais fortes do que os que enfrentamos antes. Quase não consegui acompanhar os movimentos deles.'),
    ('mata_corrompida', 'Jaciara', 'Eles não estavam agindo como criaturas descontroladas. Pareciam estar protegendo alguma coisa.'),
    ('mata_corrompida', 'Akin', 'Ou tentando impedir que chegássemos até ela. Seja o que for, está mais adiante.'),
    ('mata_corrompida', 'Curupira', 'Não... Escutem. A energia deles não vinha apenas daquela direção. Ela está em toda parte, concentrada em um único ponto.'),
    ('mata_corrompida', 'Maíra', 'Então é lá que vamos encontrar a origem dessa corrupção.'),
    ('clareira', 'Narrador', 'O grupo chegou a uma clareira tomada por raízes escuras. O chão estava rachado, e uma energia arroxeada pulsava sob a terra, como se a própria floresta tivesse um coração doente.'),
    ('clareira', 'Caubi', 'O que aconteceu aqui? Parece que toda a vida deste lugar foi sugada.'),
    ('clareira', 'Curupira', 'Esta clareira já foi um lugar sagrado. Alguma coisa profanou suas raízes e está usando a força da floresta para se alimentar.'),
    ('clareira', 'Akin', 'A energia está aumentando. Afastem-se!'),
    ('clareira', 'Narrador', 'Um estrondo sacudiu a clareira. As raízes se romperam e, de dentro da terra, ergueu-se uma criatura gigantesca, envolta por energia sombria.'),
    ('clareira', 'Angoera Primordial', 'Quem... ousa perturbar... meu despertar?'),
    ('clareira', 'Maíra', 'Você está por trás da corrupção da floresta?'),
    ('clareira', 'Angoera Primordial', 'A floresta... é apenas o começo. Minha força... voltará a crescer.'),
    ('clareira', 'Curupira', 'Essa criatura está ligada às raízes da mata! Nunca senti uma presença tão antiga e poderosa.'),
    ('clareira', 'Jaciara', 'Não importa o tamanho dela. Se está destruindo a floresta, precisamos detê-la!'),
    ('clareira', 'Angoera Primordial', 'Então... desapareçam!'),
]

# CENA 2 — DEPOIS DA DERROTA OBRIGATÓRIA
# Esta cena só deve começar quando a equipe do jogador for derrotada pelo
# Angoera Primordial. Guaraci e Jaci chegam depois da derrota, não antes.
CENA2_4 = [
    ('clareira', 'Narrador', 'A energia do Angoera Primordial explodiu pela clareira. Maíra tentou se levantar, mas seu corpo já não respondia. Um a um, seus companheiros foram derrubados.'),
    ('clareira', 'Caubi', 'Maíra...! Não consigo... continuar...'),
    ('clareira', 'Maíra', 'Não... ainda não... podemos... desistir...'),
    ('clareira', 'Angoera Primordial', 'Vocês lutaram... com coragem. Mas sua força... não significa nada diante de mim.'),
    ('clareira', 'Narrador', 'O Angoera Primordial ergueu o braço, reunindo energia para desferir o golpe final. Quando a luz da criatura estava prestes a atingir o grupo, um clarão dourado cortou o céu.'),
    ('clareira', 'Guaraci', 'Já chega! Você não causará mais sofrimento nesta floresta.'),
    ('clareira', 'Narrador', 'Uma segunda presença surgiu ao lado da figura dourada. Uma luz prateada envolveu a clareira, fazendo a energia sombria recuar por alguns instantes.'),
    ('clareira', 'Jaci', 'A escuridão que você espalha ameaça romper o equilíbrio desta terra. Não permitiremos isso.'),
    ('clareira', 'Angoera Primordial', 'Guaraci... Jaci... Até os deuses vieram assistir ao meu despertar?'),
    ('clareira', 'Guaraci', 'Viemos impedir que sua corrupção alcance o restante da floresta.'),
    ('clareira', 'Maíra', 'Quem... são vocês?'),
    ('clareira', 'Jaci', 'Sou Jaci. E este é Guaraci. Viemos porque sentimos a perturbação que está se espalhando por estas terras.'),
    ('clareira', 'Caubi', 'Vocês são divindades?'),
    ('clareira', 'Guaraci', 'Sim. Mas mesmo nossos poderes não devem ser usados sem propósito. Esta criatura está ligada a uma força que ainda não compreendemos por completo.'),
    ('clareira', 'Jaci', 'Agora, precisamos acabar com a ameaça diante de nós. Maíra, seus companheiros ainda podem lutar?'),
    ('clareira', 'Maíra', 'Estamos feridos... mas não vamos fugir.'),
    ('clareira', 'Guaraci', 'Então lutaremos juntos. Escolham quem irá enfrentar essa criatura. Desta vez, não estarão sozinhos.'),
]

# CENA 2 — FIM
# Diálogos após a vitória do jogador na revanche contra o Angoera Primordial.
CENA2_4_FIM = [
    ('clareira', 'Narrador', 'Com o último golpe, o Angoera Primordial cambaleou. A energia arroxeada que cobria seu corpo começou a se desfazer, e as raízes corrompidas perderam o brilho.'),
    ('clareira', 'Angoera Primordial', 'Não... Isso ainda... não terminou...'),
    ('clareira', 'Narrador', 'A criatura se desfez em partículas escuras que foram levadas pelo vento. O silêncio tomou conta da clareira, mas, pela primeira vez, não parecia um silêncio de medo.'),
    ('clareira', 'Caubi', 'Conseguimos... Dessa vez, conseguimos.'),
    ('clareira', 'Jaciara', 'A energia está desaparecendo. Acho que a floresta está finalmente livre daquela criatura.'),
    ('clareira', 'Curupira', 'A clareira está se recuperando, mas ainda sinto marcas profundas na mata. A corrupção não começou aqui.'),
    ('clareira', 'Maíra', 'Então o Angoera Primordial estava sendo usado por algo ainda maior?'),
    ('clareira', 'Guaraci', 'É possível. Antes de desaparecer, ele falou sobre um despertar. Essa força não surgiu por acaso.'),
    ('clareira', 'Jaci', 'Há muito tempo observamos sinais de desequilíbrio. Agora sabemos que a ameaça está crescendo e que não ficará restrita a esta floresta.'),
    ('clareira', 'Maíra', 'Por que vocês vieram nos ajudar?'),
    ('clareira', 'Guaraci', 'Porque sentimos uma ligação entre essa escuridão e a força que existe em você.'),
    ('clareira', 'Maíra', 'Em mim?'),
    ('clareira', 'Jaci', 'Sua energia lembra a de Tupã. Ainda não sabemos por que, mas talvez sua jornada esteja ligada ao que está acontecendo.'),
    ('clareira', 'Maíra', 'Então preciso descobrir o que isso significa. E preciso impedir que essa ameaça alcance meu povo.'),
    ('clareira', 'Guaraci', 'Iremos com vocês. Não podemos permitir que o equilíbrio desta terra seja destruído.'),
    ('clareira', 'Jaci', 'Mas há outra ameaça se aproximando. A floresta não é o único lugar em perigo.'),
]

# CENA 3 — ENCERRAMENTO DO CAPÍTULO
CENA3_4 = [
    ('mata', 'Narrador', 'Enquanto o grupo deixava a clareira, Akin percebeu uma coluna de fumaça surgindo além das árvores. Não parecia ser um incêndio natural.'),
    ('mata', 'Akin', 'Parem. Aquela fumaça vem de um acampamento. Há pessoas reunidas adiante.'),
    ('mata', 'Jaciara', 'Essas marcas no chão... são pegadas humanas. Muitas.'),
    ('mata', 'Caubi', 'Quem estaria tão longe da costa?'),
    ('mata', 'Maíra', 'Os portugueses. Eles continuam avançando para dentro de nossas terras.'),
    ('mata', 'Curupira', 'A presença deles também está ferindo a floresta. Árvores derrubadas, caminhos abertos à força...'),
    ('mata', 'Guaraci', 'A ameaça que enfrentamos não tem uma única origem. A corrupção espiritual e a invasão dos homens estão colocando esta terra em perigo.'),
    ('mata', 'Jaci', 'Precisaremos compreender as duas antes que seja tarde.'),
    ('mata', 'Maíra', 'Eles já tiraram demais de nós. Não vou permitir que destruam mais nenhuma aldeia.'),
    ('mata', 'Akin', 'Então precisamos descobrir quantos são e o que estão planejando.'),
    ('mata', 'Maíra', 'Vamos nos aproximar com cuidado. Nossa jornada ainda não terminou.'),
    ('mata', 'Narrador', 'o grupo seguiu em direção à fumaça. A vitória contra o Angoera Primordial havia revelado uma ameaça ainda maior — e o próximo passo os levaria diretamente ao avanço dos portugueses.'),
]
