# Capítulo 5 — A Ira de Tupã
# Formato das falas: (ambiente, personagem, texto)
# Este arquivo contém somente os diálogos. As batalhas e transições são
# controladas pelo main.py.
#
# Fluxo sugerido para integração:
# CENA1_5 -> batalha contra soldados portugueses
# CENA1_5_FIM -> CENA2_5 -> batalha contra soldados e oficial
# CENA2_5_FIM -> CENA3_5 -> batalha final contra o Capitão
# CENA3_5_FIM -> CENA4_5 (derrota da equipe e chegada de Tupã)
# CENA4_5_FIM -> tela de encerramento / capítulos concluídos
#
# Observação: ainda não há portrait/actor de Tupã no projeto enviado.
# Por isso, suas falas estão neste roteiro, mas a integração visual dele
# deverá ser feita depois que os assets forem criados.

# CENA 1 — A ameaça se aproxima
# O grupo descobre que os portugueses estão preparando um ataque a uma aldeia.
CENA1_5 = [
    ('mata', 'Narrador', 'Depois de deixarem a clareira, Maíra e seus companheiros seguiram por uma trilha que levava para além da floresta. A presença dos portugueses naquela região já não era apenas um rumor: os sinais de sua passagem estavam por toda parte.'),
    ('mata', 'Jaciara', 'Olhem ao redor. Árvores derrubadas, marcas de rodas e pegadas por todo o caminho. Eles estão avançando cada vez mais para dentro das nossas terras.'),
    ('mata', 'Akin', 'E não parecem estar apenas explorando. Há marcas de acampamentos recentes e sinais de que muitos soldados passaram por aqui.'),
    ('mata', 'Caubi', 'Se continuarem nessa direção, podem encontrar outra aldeia. As pessoas de lá talvez nem saibam que estão chegando.'),
    ('mata', 'Maíra', 'Eu sei o que acontece quando eles encontram uma aldeia despreparada. Não vou deixar que outra família passe pelo que a minha passou.'),
    ('mata', 'Guaraci', 'Sua determinação é admirável, Maíra. Mas não confundam coragem com imprudência. Os invasores estão armados e parecem estar em grande número.'),
    ('mata', 'Jaci', 'Precisamos descobrir quantos são e onde pretendem atacar. Só assim poderemos impedir que avancem.'),
    ('mata', 'Curupira', 'A floresta está cheia de rastros. Posso seguir o caminho que eles abriram, mas precisamos permanecer atentos.'),
    ('mata', 'Narrador', 'O grupo encontrou marcas recentes no barro e seguiu por elas até avistar uma coluna de fumaça entre as árvores.'),
    ('acampamento', 'Caubi', 'Ali! É um acampamento. Há soldados por toda parte.'),
    ('acampamento', 'Akin', 'E olhem aquelas carroças. Estão reunindo mantimentos e armas. Isso parece uma preparação para partir em campanha.'),
    ('acampamento', 'Jaciara', 'Há uma bandeira perto da tenda principal. Esse símbolo... Maíra, você reconhece?'),
    ('acampamento', 'Maíra', 'Reconheço. É o mesmo símbolo que vi naquela noite. O capitão que comandou o ataque à minha aldeia está aqui.'),
    ('acampamento', 'Caubi', 'Então é ele... O homem que destruiu sua casa.'),
    ('acampamento', 'Maíra', 'Passei muito tempo imaginando se um dia o encontraria novamente. Agora que sei onde está, não vou deixá-lo atacar outra aldeia.'),
    ('acampamento', 'Akin', 'Não podemos simplesmente entrar pela frente. Primeiro precisamos abrir caminho e impedir que os soldados deem o alerta.'),
    ('acampamento', 'Guaraci', 'Vamos agir juntos. Nosso objetivo é deter o avanço deles e proteger quem estiver em perigo.'),
    ('acampamento', 'Maíra', 'Então vamos. Mas fiquem atentos: não sabemos quantos soldados ainda estão escondidos.'),
]

# CENA 1 — FIM
# Após a primeira batalha contra soldados portugueses.
CENA1_5_FIM = [
    ('acampamento', 'Narrador', 'Depois de uma luta intensa, os soldados que guardavam a entrada do acampamento foram derrotados. O barulho do confronto chamou a atenção dos homens que estavam mais adiante.'),
    ('acampamento', 'Caubi', 'Acho que perdemos qualquer chance de passar despercebidos.'),
    ('acampamento', 'Jaciara', 'Eles já sabem que estamos aqui. Estão se reunindo perto da tenda maior.'),
    ('acampamento', 'Akin', 'Há mais soldados do que eu esperava. E alguns parecem comandar os outros.'),
    ('acampamento', 'Curupira', 'O caminho atrás de nós está livre, mas não podemos deixar que eles continuem avançando pela floresta.'),
    ('acampamento', 'Maíra', 'O capitão está naquela tenda. Vamos atravessar o acampamento e chegar até ele.'),
    ('acampamento', 'Guaraci', 'Não se precipite. Se ele comanda todos esses homens, estará protegido por seus melhores soldados.'),
    ('acampamento', 'Maíra', 'Eu sei. Mas não vou recuar agora.'),
    ('acampamento', 'Narrador', 'O grupo avançou entre as tendas. Ao perceber a aproximação, um oficial português reuniu os soldados e bloqueou a passagem.'),
    ('acampamento', 'Oficial', 'Em posição! Não deixem esses selvagens chegarem à tenda do capitão!'),
    ('acampamento', 'Akin', 'Parece que teremos que passar por eles primeiro.'),
    ('acampamento', 'Maíra', 'Preparem-se! Não deixem que nos separem!'),
]

# CENA 2 — O caminho até o capitão
# Começa depois da primeira batalha. Ao terminar, iniciar a batalha contra
# soldados portugueses acompanhados por um oficial.
CENA2_5 = [
    ('acampamento', 'Narrador', 'O oficial caiu, e os soldados restantes recuaram. O caminho até a tenda principal estava aberto. Do lado de dentro, uma voz conhecida ordenou que os sobreviventes se afastassem.'),
    ('acampamento', 'Capitão', 'Então são vocês que estão causando toda essa confusão no meu acampamento?'),
    ('acampamento', 'Maíra', 'Você se lembra de mim?'),
    ('acampamento', 'Capitão', 'Deveria? Já encontrei dezenas de aldeias e enfrentei gente que jurava proteger suas terras. Não guardo o rosto de todos.'),
    ('acampamento', 'Maíra', 'Você atacou minha aldeia. Minha mãe morreu naquela noite. Eu me lembro de cada detalhe, inclusive de você.'),
    ('acampamento', 'Capitão', 'Ah... então é uma das sobreviventes. Pensei que todos tivessem sido levados pelo fogo ou fugido para longe.'),
    ('acampamento', 'Caubi', 'Você fala como se não tivesse destruído a vida de tantas pessoas.'),
    ('acampamento', 'Capitão', 'Fiz o que precisava ser feito. Estas terras serão ocupadas, com ou sem a aprovação de seus habitantes.'),
    ('acampamento', 'Jaciara', 'Vocês não têm direito de tomar nossas casas, nossas florestas e nossas vidas.'),
    ('acampamento', 'Capitão', 'Direito? Estamos aqui para conquistar. Quem se colocar no caminho será tratado como inimigo.'),
    ('acampamento', 'Akin', 'Você não vai passar por nós.'),
    ('acampamento', 'Capitão', 'Corajosos... ou tolos. Não importa. Meus homens vão acabar com vocês.'),
    ('acampamento', 'Guaraci', 'Maíra, não permita que a raiva decida por você. Lembre-se do que estamos tentando proteger.'),
    ('acampamento', 'Maíra', 'Eu não esqueci. É justamente por isso que estou aqui. Não vou permitir que ele faça com outras pessoas o que fez com a minha família.'),
    ('acampamento', 'Capitão', 'Guardas! Acabem com eles!'),
]

# CENA 2 — FIM
# Após a batalha contra os soldados e o oficial que protegem o capitão.
CENA2_5_FIM = [
    ('acampamento', 'Narrador', 'Os últimos soldados que protegiam a tenda foram derrotados. O capitão observou o campo e percebeu que seus homens já não conseguiam impedir a aproximação do grupo.'),
    ('acampamento', 'Capitão', 'Incompetentes! Não conseguem deter nem um pequeno grupo de guerreiros?'),
    ('acampamento', 'Jaciara', 'Seus homens não vão mais nos impedir.'),
    ('acampamento', 'Capitão', 'Talvez eu tenha subestimado vocês. Mas não cometam o erro de acreditar que isso acabou.'),
    ('acampamento', 'Akin', 'Chega de ameaças. Acabou sua proteção.'),
    ('acampamento', 'Capitão', 'Então venham. Quero ver se são capazes de enfrentar o homem que já derrotou tantos guerreiros antes de vocês.'),
    ('acampamento', 'Maíra', 'É isso que vim fazer. Desta vez, você não vai fugir.'),
    ('acampamento', 'Caubi', 'Maíra, estamos com você. Não precisa enfrentar esse homem sozinha.'),
    ('acampamento', 'Maíra', 'Eu sei. Vamos terminar isso juntos.'),
    ('acampamento', 'Narrador', 'O capitão sacou sua arma e avançou para fora da tenda. Os dois lados se posicionaram. A batalha que decidiria o destino daquele acampamento estava prestes a começar.'),
]

# CENA 3 — O último chefe: Capitão português
# Após esta cena, iniciar a batalha final contra o Capitão.
CENA3_5 = [
    ('acampamento', 'Capitão', 'Olhem bem para mim. Sou o homem que comanda esta expedição. Já enfrentei guerreiros muito mais fortes do que vocês.'),
    ('acampamento', 'Maíra', 'Talvez tenha vencido muitas batalhas, mas não conhece a força de quem luta para proteger seu próprio povo.'),
    ('acampamento', 'Capitão', 'Palavras bonitas não detêm uma espada.'),
    ('acampamento', 'Guaraci', 'A força de um guerreiro não está apenas na arma que carrega, mas naquilo que escolhe defender.'),
    ('acampamento', 'Capitão', 'Pouco me importa o que vocês defendem. Estas terras serão nossas!'),
    ('acampamento', 'Curupira', 'A floresta não pertence a você. Nenhuma dessas terras está vazia só porque vocês decidiram ignorar quem vive aqui.'),
    ('acampamento', 'Capitão', 'Silêncio! Já ouvi o bastante.'),
    ('acampamento', 'Maíra', 'Araci não poderá voltar. Minha aldeia não será como era antes. Mas eu ainda posso impedir que você destrua outras vidas.'),
    ('acampamento', 'Capitão', 'Sua mãe deveria ter ensinado você a não desafiar homens que estão acima de sua condição.'),
    ('acampamento', 'Maíra', 'Não fale dela!'),
    ('acampamento', 'Caubi', 'Maíra! Não deixe que ele use sua dor contra você!'),
    ('acampamento', 'Jaciara', 'Estamos aqui. Lute ao nosso lado!'),
    ('acampamento', 'Akin', 'Vamos acabar com isso!'),
    ('acampamento', 'Narrador', 'Maíra respirou fundo e firmou a lança. A lembrança de sua mãe continuava doendo, mas agora ela sabia que não estava lutando apenas por vingança. Estava lutando por todos que ainda poderiam ser salvos.'),
    ('acampamento', 'Maíra', 'Pelo meu povo. Pela minha mãe. E por todos que ainda vivem nesta terra. Vamos!'),
]

# CENA 3 — FIM
# A equipe deve ser derrotada pelo capitão. A cena seguinte mostra a chegada
# de Tupã, que impede o golpe final e salva o grupo.
CENA3_5_FIM = [
    ('acampamento', 'Narrador', 'A batalha foi longa. Maíra e seus companheiros lutaram com tudo o que tinham, mas o capitão conhecia cada movimento de seus soldados e aproveitou qualquer abertura. Um a um, os guerreiros foram derrubados.'),
    ('acampamento', 'Caubi', 'Maíra... eu não consigo mais levantar...'),
    ('acampamento', 'Jaciara', 'Nós... fizemos tudo o que podíamos...'),
    ('acampamento', 'Akin', 'Maldição... não podemos deixar que ele avance...'),
    ('acampamento', 'Maíra', 'Ainda... não...'),
    ('acampamento', 'Capitão', 'Acabou. Vocês tiveram coragem, mas coragem não é suficiente para vencer um exército.'),
    ('acampamento', 'Capitão', 'Quanto a você, menina, deveria ter permanecido escondida. Agora vai assistir ao fim de sua resistência.'),
    ('acampamento', 'Narrador', 'O capitão ergueu sua arma e se aproximou de Maíra. Ela tentou se levantar, mas seus braços já não tinham forças. Seus companheiros estavam caídos ao seu redor.'),
    ('acampamento', 'Maíra', 'Eu... não vou deixar...'),
    ('acampamento', 'Capitão', 'Chega!'),
]

# CENA 4 — A chegada de Tupã
# Esta cena começa imediatamente após a derrota da equipe. A aparição de Tupã
# deve ser acompanhada de uma mudança visual para o cenário 'storm'.
CENA4_5 = [
    ('storm', 'Narrador', 'Antes que o capitão pudesse desferir o golpe, um trovão ensurdecedor rasgou o céu. O vento atravessou o acampamento, apagando tochas e levantando a poeira do chão.'),
    ('storm', 'Capitão', 'O que está acontecendo?!'),
    ('storm', 'Narrador', 'Nuvens escuras cobriram o céu. Um clarão iluminou a floresta, e uma presença poderosa surgiu diante dos guerreiros caídos.'),
    ('storm', 'Tupã', 'Afaste-se deles.'),
    ('storm', 'Capitão', 'Quem é você? Que truque é esse?'),
    ('storm', 'Tupã', 'Você avançou sobre estas terras, destruiu lares e tirou vidas. Ainda assim, acredita que pode ordenar até mesmo que o céu se cale?'),
    ('storm', 'Maíra', 'Essa voz...'),
    ('storm', 'Guaraci', 'Tupã...'),
    ('storm', 'Jaci', 'Ele veio.'),
    ('storm', 'Caubi', 'Então... esse é Tupã?'),
    ('storm', 'Tupã', 'Maíra, você e seus companheiros lutaram até onde suas forças permitiram. Descansem. Agora, eu protegerei este povo.'),
    ('storm', 'Maíra', 'Eu tentei... tentei impedir que eles chegassem até aqui.'),
    ('storm', 'Tupã', 'Eu sei. Sua coragem não passou despercebida. Mas nenhuma pessoa deveria carregar sozinha o peso de proteger todos os outros.'),
    ('storm', 'Capitão', 'Soldados! De pé! Atirem nessa criatura!'),
    ('storm', 'Narrador', 'Os soldados apontaram suas armas. Antes que pudessem disparar, relâmpagos atingiram o chão diante deles. O estrondo fez os homens recuarem, apavorados.'),
    ('storm', 'Capitão', 'Mantenham a formação! Não recuem!'),
    ('storm', 'Tupã', 'Esta terra não será tomada pela força enquanto houver quem a proteja.'),
    ('storm', 'Narrador', 'Uma sequência de trovões percorreu o céu. O vento derrubou as tendas, as carroças foram lançadas para longe e os soldados perderam sua formação. O capitão tentou ordenar um último avanço, mas seus homens já estavam fugindo.'),
    ('storm', 'Capitão', 'Covardes! Voltem! Eu ordeno que voltem!'),
    ('storm', 'Narrador', 'Sem tropas para apoiá-lo e diante do poder de Tupã, o capitão foi obrigado a recuar. Os portugueses abandonaram o acampamento e fugiram em direção à costa.'),
    ('storm', 'Tupã', 'Vão embora. Não voltem a ameaçar este povo.'),
]

# CENA 4 — FIM / EPÍLOGO
# Encerramento definitivo da história.
CENA4_5_FIM = [
    ('peace', 'Narrador', 'Quando a tempestade passou, o silêncio voltou à floresta. Os portugueses haviam sido expulsos daquela região, e o caminho até as aldeias estava livre novamente.'),
    ('peace', 'Caubi', 'Conseguimos... Eles realmente foram embora.'),
    ('peace', 'Jaciara', 'Não foi uma vitória fácil. Mas impedimos que avançassem e colocassem outras aldeias em perigo.'),
    ('peace', 'Akin', 'Eles podem tentar voltar algum dia. Mas agora sabem que não encontrarão estas terras desprotegidas.'),
    ('peace', 'Curupira', 'A floresta ainda precisa se recuperar. Há muito a reconstruir, mas a vida vai encontrar seu caminho novamente.'),
    ('peace', 'Guaraci', 'Vocês enfrentaram perigos que pareciam impossíveis. E, mesmo quando foram derrotados, não abandonaram aquilo em que acreditavam.'),
    ('peace', 'Jaci', 'A coragem de vocês inspirou aqueles que ainda resistiam. A proteção desta terra não depende de uma única pessoa.'),
    ('peace', 'Maíra', 'Eu passei tanto tempo pensando no dia em que encontraria o capitão. Achei que derrotá-lo faria a dor desaparecer.'),
    ('peace', 'Caubi', 'E fez?'),
    ('peace', 'Maíra', 'Não. Minha mãe continua fazendo falta. Minha aldeia não voltou. Mas agora sei que posso continuar vivendo sem deixar que a tristeza decida tudo por mim.'),
    ('peace', 'Caubi', 'Você não precisa enfrentar o que vier sozinha. Nós vamos continuar ao seu lado.'),
    ('peace', 'Maíra', 'Eu sei. E quero que continuemos protegendo nossas terras juntos.'),
    ('peace', 'Narrador', 'Tupã observou o grupo por alguns instantes. Sua presença já não parecia tão distante ou incompreensível. Maíra deu um passo à frente.'),
    ('peace', 'Maíra', 'Tupã... por que demorou tanto para aparecer?'),
    ('peace', 'Tupã', 'Porque a força de um povo não deve depender apenas da intervenção dos deuses. Vocês precisavam descobrir a própria coragem, escolher pelo que lutar e permanecer unidos.'),
    ('peace', 'Maíra', 'Então você esteve nos observando?'),
    ('peace', 'Tupã', 'Acompanhei sua jornada. Vi sua dor, suas dúvidas e sua determinação. O trovão não existe para substituir a coragem dos vivos, mas para lembrar que eles não estão esquecidos.'),
    ('peace', 'Maíra', 'Ainda tenho muito a aprender. Mas não vou parar de proteger meu povo.'),
    ('peace', 'Tupã', 'Então siga em frente, Maíra. Que sua coragem continue iluminando o caminho.'),
    ('peace', 'Narrador', 'Uma luz atravessou as nuvens. Tupã desapareceu junto ao último trovão, deixando para trás um céu tranquilo.'),
    ('peace', 'Curupira', 'A mata vai se recuperar. E, desta vez, estaremos aqui para cuidar dela.'),
    ('peace', 'Akin', 'Temos muito trabalho pela frente. As aldeias precisarão de ajuda para reconstruir o que foi perdido.'),
    ('peace', 'Jaciara', 'Então vamos começar. A vitória só terá sentido se ajudarmos nosso povo a recomeçar.'),
    ('peace', 'Caubi', 'E, se depender de mim, ninguém vai precisar enfrentar tudo isso sozinho novamente.'),
    ('peace', 'Maíra', 'Vamos para casa. Ainda há muito pelo que lutar, mas hoje podemos descansar.'),
    ('peace', 'Narrador', 'Maíra e seus companheiros seguiram em direção às aldeias. A invasão havia sido interrompida, os portugueses expulsos daquela região e a esperança começava a renascer.'),
    ('peace', 'Narrador', 'A jornada de Maíra não terminou com a vingança, mas com a escolha de proteger aqueles que ainda tinham um futuro.'),
    ('peace', 'Narrador', 'FIM — MAÍRA: HERDEIRA DO TROVÃO.'),
]
