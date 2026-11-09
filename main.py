"""Tupã: Herdeira do Trovão — capítulo 1. Python 3 + pygame."""
import random
from pathlib import Path
from roteiro import SCENES, AFTER_LOSS, ENDING
from capitulo2 import CENA1, CENA2, CENA3, CENA4, CENA5, CENA5_FIM
from capitulo3 import CENA1_3, CENA2_3, CENA3_3, CENA4_3 
import pygame
from personagem import Personagem
from vilao import Vilao
import os
os.environ['PYGAME_FORCE_SCALE'] = 'photo'
pygame.init()
W, H = 960, 540
screen = pygame.display.set_mode((W, H), pygame.FULLSCREEN | pygame.SCALED)
pygame.display.set_caption('Tupã: Herdeira do Trovão | Capítulo 1')
clock = pygame.time.Clock()
FONT = pygame.font.SysFont('arial', 23)
SMALL = pygame.font.SysFont('arial', 18)
BIG = pygame.font.SysFont('arial', 48, bold=True)
MID = pygame.font.SysFont('arial', 31, bold=True)
WHITE=(245,237,214); GOLD=(239,191,92); RED=(198,73,66); BLUE=(110,193,255)
GREEN=(94,196,125); DARK=(13,19,27)

# Arquivos de imagem usados pelo jogo.
ASSET = Path(__file__).resolve().parent / 'assets'
def load(name):
    return pygame.image.load(str(ASSET / (name + '.png'))).convert_alpha()
BACKS={n:pygame.transform.smoothscale(load('bg_'+n),(W,H)) for n in ('fire','storm','peace','dawn','floresta','equipe', 'acampamento','noite', 'clareira', 'mata', 'mata_fogo')}
PORTRAITS={n:load('portrait_'+n) for n in ('maira','caubi','araci','captain','leader','soldier', 'jaciara', 'akin', 'curupira', 'boitata')}
ACTORS={n:load('actor_'+n) for n in ('maira','maira2','caubi','araci','captain','leader','soldier', 'jaciara', 'akin', 'angoera', 'ancestral', 'curupira', 'boitata')}
TELA_INICIAL=pygame.transform.smoothscale(load('tela_inicial'),(W,H))
TELA_CAPITULOS=pygame.transform.smoothscale(load('tela_capitulos'),(W,H))
TELA_FIM=pygame.transform.smoothscale(load('tela_fim'),(W,H))
TELA_EQUIPE=pygame.transform.smoothscale(load('tela_equipe'),(W,H))
# Personagens disponíveis no jogo
PERSONAGENS = [
    'Maíra',
    'Caubi',
    'Jaciara',
    'Akin',
    'Curupira',
    '???',
    '???',
    '???',
    '???',
    '???'
]

# Personagens que já podem ser escolhidos
DESBLOQUEADOS = ['Maíra', 'Caubi', 'Jaciara']

# Equipe inicial
EQUIPE = []
# Personagens que participarão da batalha do capítulo 2
equipe_batalha = []
def txt(s,x,y,font=FONT,color=WHITE):
    screen.blit(font.render(s,True,color),(x,y))

def wrap(s,font,width):
    out=[];line=''
    for word in s.split():
        attempt=(line+' '+word).strip()
        if font.size(attempt)[0]>width and line:out.append(line);line=word
        else:line=attempt
    if line:out.append(line)
    return out

def rect(color,r):pygame.draw.rect(screen,color,r)

def backdrop(kind,t):
    if kind=='sleep':kind='peace'
    screen.blit(BACKS.get(kind,BACKS['peace']),(0,0))
    if kind=='storm':
        veil=pygame.Surface((W,H),pygame.SRCALPHA);veil.fill((6,18,44,35));screen.blit(veil,(0,0))
        if int(t*2.3)%10==0:
            pygame.draw.lines(screen,(185,230,255),False,[(500,0),(466,90),(507,111),(447,210)],5)

def actor(key,center,bottom=393,height=325,focused=True,flip=False):
    """Mostra a arte do personagem na cena, destacando quem fala."""
    art=ACTORS[key]
    ratio=height/art.get_height()
    width=max(1,round(art.get_width()*ratio))
    pic=pygame.transform.smoothscale(art,(width,height))
    if flip:pic=pygame.transform.flip(pic,True,False)
    if not focused:
        shade=pygame.Surface(pic.get_size(),pygame.SRCALPHA)
        shade.fill((10,17,30,115));pic.blit(shade,(0,0),special_flags=pygame.BLEND_RGBA_SUB)
    screen.blit(pic,(int(center-width/2),int(bottom-height)))


# Posições das molduras na imagem tela_equipe.png (medidas para 960x540)
COLUNAS = [48, 154, 261, 369, 476]
LINHAS_ELENCO = [143, 284]
PLACAS_ELENCO = [230, 372]
X_EQUIPE = [597, 712, 830]

# Nome do personagem -> nome do arquivo do retrato
RETRATOS = {'Maíra': 'maira', 'Caubi': 'caubi', 'Jaciara': 'jaciara', 'Akin': 'akin', 'Curupira': 'curupira', 'Araci': 'araci', 'Capitão': 'captain', 'Líder': 'leader', 'Soldado 1': 'soldier', 'Soldado 2': 'soldier', 'Soldado 3': 'soldier'}
NOME_FONT = pygame.font.SysFont('arial', 12, bold=True)

def desenhar_retrato(nome, area):
    """Desenha o retrato dentro da moldura, sem esticar a imagem."""
    chave = RETRATOS.get(nome)
    if not chave:
        return
    img = PORTRAITS[chave]
    escala = max(area.width / img.get_width(), area.height / img.get_height())
    nova = pygame.transform.smoothscale(img, (round(img.get_width() * escala), round(img.get_height() * escala)))
    screen.set_clip(area)
    screen.blit(nova, nova.get_rect(center=area.center))
    screen.set_clip(None)

def desenhar_nome(nome, placa):
    """Escreve o nome centralizado na placa."""
    texto = NOME_FONT.render(nome.upper(), True, WHITE)
    screen.blit(texto, texto.get_rect(center=placa.center))
def desenhar_selecao_equipe():
    screen.blit(TELA_EQUIPE, (0, 0))

    # Elenco: 10 cartas em duas fileiras de 5
    for i, nome in enumerate(PERSONAGENS):
        coluna = i % 5
        linha = i // 5
        if nome in DESBLOQUEADOS:
            area = pygame.Rect(COLUNAS[coluna], LINHAS_ELENCO[linha], 70, 82)
            desenhar_retrato(nome, area)
            desenhar_nome(nome, pygame.Rect(COLUNAS[coluna] + 1, PLACAS_ELENCO[linha], 69, 18))

    # Equipe escolhida: 3 cartas
    for i, nome in enumerate(EQUIPE):
        desenhar_retrato(nome, pygame.Rect(X_EQUIPE[i], 177, 81, 129))
        desenhar_nome(nome, pygame.Rect(X_EQUIPE[i], 312, 80, 20))
            
    

def cast_scene(kind,who):
    # Two actors at most. Araci enters naturally beside Maíra, not between cards.
    if kind=='peace':
        if who=='Araci':
            actor('maira',277,398,280,False)
            actor('araci',676,398,315,True)
        else:
            actor('maira',255,398,333,who=='Maíra')
            actor('caubi',695,398,333,who=='Caubi',flip=True)
    elif kind=='fire':
        if who in ('Capitão','Líder'):
            actor('captain',268,396,340,who=='Capitão')
            actor('leader',690,396,322,who=='Líder',flip=True)
        elif who=='Araci' or (who=='Narrador' and script is AFTER_LOSS):
            actor('maira',266,398,305,False)
            actor('araci',680,398,340,True)
        else:
            actor('maira',275,398,353,who=='Maíra')
    elif kind=='storm':
        actor('maira2',302,398,370,who=='Maíra')
        if who=='Líder':
            actor('leader',716,398,317,True,flip=True)

    elif kind=='dawn':
        if script in (CENA1, CENA2):

            if script is CENA2 and who.startswith('Soldado'):
                actor('soldier',700,398,330,True)

            elif who=='Caubi':
                actor('caubi',270,398,330,True)

            else:
                actor('maira',270,398,340,who=='Maíra')

            if not who.startswith('Soldado'):
                actor('jaciara',700,398,330,who=='Jaciara')

        elif script is CENA3:
            if who=='Caubi':
                actor('caubi',270,398,330,True)
            else:
                actor('maira',270,398,340,who=='Maíra')
        elif script is CENA4:
            # Grupo à esquerda, Akin sozinho à direita
            actor('maira',120,398,300,who=='Maíra')
            actor('caubi',280,398,300,who=='Caubi')
            actor('jaciara',440,398,300,who=='Jaciara')
            actor('akin',760,398,310,who=='Akin',flip=True)

        elif script in (CENA1_3, CENA2_3):
            actor('maira',120,398,300,who=='Maíra')
            actor('caubi',280,398,300,who=='Caubi')
            actor('jaciara',440,398,300,who=='Jaciara')
            actor('akin',600,398,300,who=='Akin')
            actor('curupira',810,398,300,who=='Curupira')

        elif script is CENA3_3:
            if idx < 10:
                actor('maira',120,398,300,who=='Maíra')
                actor('caubi',280,398,300,who=='Caubi')
                actor('jaciara',440,398,300,who=='Jaciara')
                actor('akin',600,398,300,who=='Akin')
                actor('curupira',810,398,300,who=='Curupira')
            else:
                actor('maira',70,398,270,who=='Maíra')
                actor('caubi',185,398,270,who=='Caubi')
                actor('jaciara',300,398,270,who=='Jaciara')
                actor('akin',415,398,270,who=='Akin')
                actor('curupira',530,398,270,who=='Curupira',flip=True)
                actor('boitata',760,398,260,True)

        elif script is CENA4_3:
            if idx < 11:
                actor('maira',70,398,270,who=='Maíra')
                actor('caubi',185,398,270,who=='Caubi')
                actor('jaciara',300,398,270,who=='Jaciara')
                actor('akin',415,398,270,who=='Akin')
                actor('curupira',530,398,270,who=='Curupira',flip=True)
                actor('boitata',760,398,260,who in ('Boitatá','Narrador'))
            else:
                actor('maira',120,398,300,who=='Maíra')
                actor('caubi',280,398,300,who=='Caubi')
                actor('jaciara',440,398,300,who=='Jaciara')
                actor('akin',600,398,300,who=='Akin')
                actor('curupira',810,398,300,who=='Curupira')

        else:
            actor('maira',270,398,340,who=='Maíra')
            actor('caubi',702,398,330,who=='Caubi',flip=True)    

def portrait_for(who):
    key={
    'Maíra':'maira',
    'Caubi':'caubi',
    'Araci':'araci',
    'Jaciara':'jaciara',
    'Akin':'akin',
    'Capitão':'captain',
    'Líder':'leader',
    'Soldado 1':'soldier',
    'Soldado 2':'soldier',
    'Soldado 3':'soldier',
    'Curupira':'curupira',
    'Boitatá':'boitata',
        }.get(who)
    if not key:return
    # Retrato pequeno dentro da caixa de diálogo.
    im=PORTRAITS[key]; w=86; h=106
    crop=pygame.transform.smoothscale(im,(w,h))
    screen.blit(crop,(33,405))
    pygame.draw.rect(screen,GOLD,(32,404,w+2,h+2),2)

def panel(y=388):
    rect((12,20,31),(22,y,W-44,H-y-16));pygame.draw.rect(screen,(178,137,81),(22,y,W-44,H-y-16),3)

def btn(label,x,y,w=210,h=46,active=True):
    r=pygame.Rect(x,y,w,h)
    rect((83,65,47) if active else (48,50,54),r)
    pygame.draw.rect(screen,GOLD if active else (99,99,99),r,2)
    f=SMALL; txt(label,x+max(8,(w-f.size(label)[0])//2),y+12,f,WHITE if active else (145,145,145))
    return r

# As falas ficam em roteiro.py, para facilitar a edição da história.
state='menu'; idx=0; script=SCENES; phase=1; maira=None; enemies=[]; turn=0; notice=''; notice_until=0; shake=0; t=0

def start_battle(second=False):
    """Cria os inimigos; second=True ativa a revanche com raios."""
    global state,phase,maira,enemies,turn,notice,notice_until
    state='battle';phase=2 if second else 1;turn=0
    # Heroína: nome, idade, vida, energia, ataque básico, ataque especial
    maira=Personagem('Maíra',20,130 if second else 100,100,23 if second else 16,44 if second else 22)
    # Vilões: nome, idade, vida, maldade, força
    enemies=[Vilao('Soldado 1',30,48,'Baixa',9),
             Vilao('Soldado 2',30,48,'Baixa',9),
             Vilao('Líder da Patrulha',40,125 if second else 110,'Alta',15)]
    notice='A tempestade fortalece Maíra!' if second else 'Derrote os invasores!';notice_until=pygame.time.get_ticks()+1900

def advance():
    global idx,script,state,cap2_parte 
    idx+=1
    if idx>=len(script):
        if script is SCENES:start_battle(False)
        elif script is AFTER_LOSS:start_battle(True)
        elif script is ENDING:state='end'
        elif script is CENA1:
         next_script(CENA2)

        elif script is CENA2:
             state='team_select'
        elif script is CENA3:
            next_script(CENA4)
        elif script is CENA4:
            if 'Akin' not in DESBLOQUEADOS:
                DESBLOQUEADOS.append('Akin')
            EQUIPE.clear()
            cap2_parte = 2
            state = 'team_select'
        elif script is CENA5:
            state = 'battle_cap2'
        elif script is CENA5_FIM:
            state = 'chapters'
        elif script is CENA1_3:
            if 'Curupira' not in DESBLOQUEADOS:
                DESBLOQUEADOS.append('Curupira')
            EQUIPE.clear()
            cap2_parte = 3
            state = 'team_select'
        elif script is CENA2_3:
            next_script(CENA3_3)
        elif script is CENA3_3:
            EQUIPE.clear()
            cap2_parte = 4
            state = 'team_select'
        elif script is CENA4_3:
            state = 'chapters'    

def next_script(which):
    global script,idx,state
    script=which;idx=0;state='story'

def enemy_action():
    global notice,notice_until,shake,state
    living=[e for e in enemies if e.esta_vivo()]
    if not living:return
    foe=random.choice(living)
    damage=foe.ataque(maira,reducao=4 if phase==2 else 0)
    notice=f"{foe.nome} atacou: -{damage} HP";notice_until=pygame.time.get_ticks()+1200;shake=8
    if not maira.esta_vivo():
        if phase==1:next_script(AFTER_LOSS)
        else:state='defeat'

def attack(special,target):
    """Calcula dano, energia e passagem para a próxima cena."""
    global turn,notice,notice_until,shake
    if target<0 or target>=len(enemies) or not enemies[target].esta_vivo():return
    damage=maira.ataque(enemies[target],special)
    if damage is None:
        notice='Energia insuficiente!';notice_until=pygame.time.get_ticks()+1300;return
    turn+=1;shake=5
    notice=f"{('Lança Relampejante' if phase==2 else 'Investida') if special else 'Golpe de Lança'}: {damage} de dano!"
    notice_until=pygame.time.get_ticks()+1400
    if not any(e.esta_vivo() for e in enemies):
        if phase==1:next_script(AFTER_LOSS)
        else:next_script(ENDING)
        return
    # A primeira derrota faz parte do roteiro; depois vem o despertar.
    if phase==1 and turn>=5:
        notice='O líder da patrulha prepara um golpe devastador!'
        next_script(AFTER_LOSS)
        return
    enemy_action()

def fim_batalha_cap2():
    global state
    if cap2_parte == 1:
        next_script(CENA3)
    elif cap2_parte == 3:
        next_script(CENA2_3)
    elif cap2_parte == 4:
        next_script(CENA4_3)
    else:
        next_script(CENA5_FIM)

def atacar_cap2(especial=False):
    global alvo_cap2, notice, notice_until, state

    if not equipe_batalha or not inimigos_cap2:
        return

    aliado = equipe_batalha[aliado_selecionado]

    if not aliado.esta_vivo():
        notice = 'Esse personagem está derrotado!'
        notice_until = pygame.time.get_ticks() + 1500
        return

    vivos = [i for i, e in enumerate(inimigos_cap2) if e.esta_vivo()]

    if not vivos:
        fim_batalha_cap2()
        return

    if alvo_cap2 not in vivos:
        alvo_cap2 = vivos[0]

    inimigo = inimigos_cap2[alvo_cap2]
    dano = aliado.ataque(inimigo, especial)

    if dano is None:
        notice = 'Energia insuficiente!'
        notice_until = pygame.time.get_ticks() + 1500
        return

    notice = f'{aliado.nome} causou {dano} de dano!'
    notice_until = pygame.time.get_ticks() + 1500

    vivos = [i for i, e in enumerate(inimigos_cap2) if e.esta_vivo()]

    if not vivos:
        fim_batalha_cap2()
        return

    alvo_cap2 = vivos[0]

    # Contra-ataque de um inimigo contra um aliado vivo
    inimigos_vivos = [e for e in inimigos_cap2 if e.esta_vivo()]
    aliados_vivos = [p for p in equipe_batalha if p.esta_vivo()]

    inimigo = random.choice(inimigos_vivos)
    alvo = random.choice(aliados_vivos)

    dano_inimigo = inimigo.ataque(alvo)

    notice = f'{inimigo.nome} atacou {alvo.nome}: -{dano_inimigo} HP!'
    notice_until = pygame.time.get_ticks() + 1800

    if not any(p.esta_vivo() for p in equipe_batalha):
        state = 'cap2_defeat'

selected=0; selected_action=0; aliado_selecionado=0
cap2_parte = 1
running=True
while running:
    dt=clock.tick(60)/1000;t+=dt;now=pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                if state=='menu':running=False
                elif state in ('end','defeat'):state='menu'
            if state=='menu' and event.key in (pygame.K_RETURN,pygame.K_SPACE):
                script=SCENES;idx=0;state='chapters'
            elif state=='story' and event.key in (pygame.K_SPACE,pygame.K_RETURN):advance()
            
            elif state=='battle':
                if event.key in (pygame.K_1,pygame.K_2,pygame.K_3):selected=int(event.unicode)-1
                if event.key==pygame.K_q:selected_action=0
                if event.key==pygame.K_e:selected_action=1
                if event.key in (pygame.K_RETURN,pygame.K_SPACE):attack(selected_action==1,selected)
            elif state in ('end','defeat') and event.key in (pygame.K_RETURN,pygame.K_SPACE):
                if state=='defeat':start_battle(True)
                else:state='menu'
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            mx,my=event.pos
            if state=='menu' and pygame.Rect(534,394,237,70).collidepoint(mx,my):script=SCENES;idx=0;state='chapters'
            elif state=='story':advance()
            elif state=='battle':
                for i in range(3):
                    if pygame.Rect((432,628,827)[i]-96,30,192,307).collidepoint(mx,my):
                        selected=i

                if pygame.Rect(26,429,222,50).collidepoint(mx,my):
                    selected_action=0

                if pygame.Rect(266,429,278,50).collidepoint(mx,my):
                    selected_action=1

                if pygame.Rect(736,429,195,50).collidepoint(mx,my):
                    attack(selected_action==1,selected)

            elif state=='battle_cap2':

                # Ataque básico
                if pygame.Rect(540, 470, 175, 45).collidepoint(mx, my):
                    atacar_cap2(False)

                # Habilidade especial
                elif pygame.Rect(730, 470, 190, 45).collidepoint(mx, my):
                    atacar_cap2(True)

                else:
                    # Selecionar aliado
                    for i in range(len(equipe_batalha)):
                        cartao = pygame.Rect(30 + i * 165, 464, 155, 60)

                        if cartao.collidepoint(mx, my):
                            if equipe_batalha[i].esta_vivo():
                                aliado_selecionado = i
                            break

                    # Selecionar inimigo
                    for i, x in enumerate((580, 720, 860)):
                        area = pygame.Rect(x - 65, 100, 130, 210)

                        if area.collidepoint(mx, my):
                            if inimigos_cap2[i].esta_vivo():
                                alvo_cap2 = i
                            break
            elif state=='team_select':
                # Voltar
                if pygame.Rect(18, 489, 118, 40).collidepoint(mx, my):
                    state = 'chapters'

                # Iniciar batalha
                elif pygame.Rect(360, 475, 240, 55).collidepoint(mx, my):
                    if len(EQUIPE) == 3:
                        dados = {
                            'Maíra': (18, 130, 100, 23, 44),
                            'Caubi': (19, 90, 100, 14, 25),
                            'Jaciara': (20, 105, 100, 20, 32),
                            'Akin': (30, 120, 100, 21, 36),
                            'Curupira': (22, 110, 100, 22, 38)
                        }

                        equipe_batalha = [
                            Personagem(nome, *dados[nome])
                            for nome in EQUIPE
                        ]
                        if cap2_parte == 1:
                            inimigos_cap2 = [
                                Vilao('Soldado 1', 30, 55, 'Baixa', 8),
                                Vilao('Soldado 2', 30, 55, 'Baixa', 8),
                                Vilao('Soldado 3', 30, 55, 'Baixa', 8)
                            ]

                        elif cap2_parte == 3:
                            inimigos_cap2 = [
                                Vilao('Angoera 1', 100, 60, 'Média', 10),
                                Vilao('Angoera 2', 100, 60, 'Média', 10),
                                Vilao('Angoera 3', 100, 60, 'Média', 10)
                            ]

                        elif cap2_parte == 4:
                            inimigos_cap2 = [
                                Vilao('Boitatá', 300, 450, 'Alta', 20)
                            ]

                        else:
                            inimigos_cap2 = [
                                Vilao('Angoera 1', 100, 60, 'Média', 10),
                                Vilao('Angoera Ancestral', 500, 260, 'Alta', 18),
                                Vilao('Angoera 2', 100, 60, 'Média', 10)
                            ]


                        alvo_cap2 = 0
                        aliado_selecionado = 0
                        notice = 'Escolha um inimigo para atacar!'
                        notice_until = pygame.time.get_ticks() + 2000
                        if cap2_parte in (1, 3, 4):
                            state = 'battle_cap2'
                        else:
                            next_script(CENA5)
                    else:
                        print("Escolha 3 personagens antes de iniciar!")

                # Selecionar ou remover personagens
                else:
                    for i, nome in enumerate(PERSONAGENS):
                        coluna = i % 5
                        linha = i // 5

                        x = COLUNAS[coluna]
                        y = LINHAS_ELENCO[linha]

                        carta = pygame.Rect(x, y, 70, 82)

                        if carta.collidepoint(mx, my):
                            if nome not in DESBLOQUEADOS:
                                break

                            if nome in EQUIPE:
                                EQUIPE.remove(nome)
                            elif len(EQUIPE) < 3:
                                EQUIPE.append(nome)

                            break

            elif state=='end':
                print('Clique na tela final:', mx, my)

                if pygame.Rect(165,463,280,50).collidepoint(mx,my):
                    state='chapters'

                elif pygame.Rect(519,463,280,50).collidepoint(mx,my):
                    state='menu'
            elif state=='chapters':
                print('Clique detectado:', mx, my)

                if pygame.Rect(187,108,280,63).collidepoint(mx,my):
                    script=SCENES
                    idx=0
                    state='story'

                elif pygame.Rect(187,182,280,63).collidepoint(mx,my):
                    if 'Curupira' in DESBLOQUEADOS:
                        DESBLOQUEADOS.remove('Curupira')
                    if 'Akin' not in DESBLOQUEADOS:
                        DESBLOQUEADOS.append('Akin')
                    EQUIPE.clear()
                    script=CENA1_3
                    idx=0
                    state='story'

                elif pygame.Rect(490,108,280,63).collidepoint(mx,my):
                    print('Abrindo capítulo 2')
                    if 'Akin' in DESBLOQUEADOS:
                        DESBLOQUEADOS.remove('Akin')
                    EQUIPE.clear()
                    cap2_parte = 1
                    script=CENA1
                    idx=0
                    state='story'

                elif pygame.Rect(19,490,114,37).collidepoint(mx,my):
                    state='menu'
                
        
    if state=='menu':
        screen.blit(TELA_INICIAL,(0,0))
    elif state=='chapters':
        screen.blit(TELA_CAPITULOS,(0,0))
        
                
    elif state=='story':
        kind,who,line=script[idx]
        backdrop('mata_fogo' if script is CENA3_3 else 'mata' if script in (CENA1_3, CENA2_3, CENA4_3) else 'acampamento' if script is CENA3 else 'noite' if script is CENA4 else 'clareira' if script in (CENA5, CENA5_FIM) else 'floresta' if script in (CENA1, CENA2) else ('peace' if kind=='sleep' else kind),t)
        if kind=='sleep':
            shade=pygame.Surface((W,H),pygame.SRCALPHA);shade.fill((2,6,16,188));screen.blit(shade,(0,0))
            txt('A ALDEIA ADORMECE...',230,195,MID,GOLD)
        else:cast_scene(kind,who)
        panel(385)
        portrait_for(who)
        left=46 if who in ('Narrador','Angoera Ancestral') else 140
        txt(who,left,400,FONT,GOLD)
        for j,ln in enumerate(wrap(line,FONT,785 if left==140 else 865)[:3]):
            txt(ln,left,434+j*27)
        txt('ESPAÇO / CLIQUE  >',755,495,SMALL,GOLD)
        txt(f'{idx+1}/{len(script)}',145 if left==140 else 45,495,SMALL,(173,176,175))
    elif state=='team_select':
        desenhar_selecao_equipe()
    elif state=='battle_cap2':
        screen.blit(BACKS['floresta' if cap2_parte == 1 else 'mata' if cap2_parte == 3 else 'mata_fogo' if cap2_parte == 4 else 'clareira'], (0, 0))

        # Inimigos: lado direito, parte superior
        posicoes_inimigos = [580, 720, 860]
        alturas_inimigos = [180, 180, 195]

        for i, inimigo in enumerate(inimigos_cap2):
            x = 720 if inimigo.nome == 'Boitatá' else posicoes_inimigos[i]

            if inimigo.esta_vivo():
                # Escolhe a arte, a altura, a largura da barra de vida e se vira pro outro lado
                if inimigo.nome == 'Angoera Ancestral':
                    arte, altura, larg_barra, virar = 'ancestral', 230, 130, False
                elif inimigo.nome == 'Boitatá':
                    arte, altura, larg_barra, virar = 'boitata', 250, 200, False    
                elif inimigo.nome.startswith('Angoera'):
                    arte, altura, larg_barra, virar = 'angoera', 185, 90, (i == 2)
                else:
                    arte, altura, larg_barra, virar = 'soldier', alturas_inimigos[i], 90, (i == 1)

                actor(arte, x, 300, altura, focused=(i == alvo_cap2), flip=virar)

                # Seta dourada acima do inimigo escolhido
                if i == alvo_cap2:
                    y_seta = 300 - altura - 15
                    pygame.draw.polygon(
                        screen, GOLD,
                        [(x - 9, y_seta), (x + 9, y_seta), (x, y_seta + 14)]
                    )

                # Nome centralizado embaixo do inimigo
                nome_img = SMALL.render(inimigo.nome, True, WHITE)
                screen.blit(nome_img, (x - nome_img.get_width() // 2, 303))

                # Barra de vida centralizada
                pygame.draw.rect(screen, (50, 50, 50), (x - larg_barra // 2, 327, larg_barra, 7))
                largura = max(0, round(larg_barra * inimigo.vida / inimigo.vida_max))
                pygame.draw.rect(screen, RED, (x - larg_barra // 2, 327, largura, 7))

            else:
                txt('DERROTADO', x - 45, 303, SMALL, RED)

        # Aliados: lado esquerdo, parte inferior
        posicoes = [115, 270, 425]

        for i, nome in enumerate(EQUIPE):
            chave = RETRATOS[nome]
            actor(chave, posicoes[i], 425, 200, focused=(i == aliado_selecionado))

        
            # Painel inferior de combate
        painel = pygame.Rect(18, 455, 924, 78)
        pygame.draw.rect(screen, (10, 18, 25), painel, border_radius=8)
        pygame.draw.rect(screen, (178, 137, 78), painel, 2, border_radius=8)

                # Status real dos três aliados
        for i, personagem in enumerate(equipe_batalha):
            x = 30 + i * 165

            card = pygame.Rect(x, 464, 155, 60)
            pygame.draw.rect(screen, (27, 35, 39), card, border_radius=5)
            cor_borda = GOLD if i == aliado_selecionado else (110, 91, 65)
            espessura = 3 if i == aliado_selecionado else 1
            pygame.draw.rect(screen, cor_borda, card, espessura, border_radius=5)

            txt(personagem.nome.upper(), x + 8, 465, SMALL, GOLD)

            # HP atual e barra proporcional
            txt(f'HP {personagem.vida}/{personagem.vida_max}', x + 8, 484, NOME_FONT, WHITE)

            pygame.draw.rect(screen, (55, 55, 55), (x + 8, 498, 139, 5))
            largura_hp = round(139 * personagem.vida / personagem.vida_max) if personagem.vida_max else 0
            pygame.draw.rect(screen, (65, 160, 85), (x + 8, 498, largura_hp, 5))

            # EP atual e barra proporcional
            txt(f'EP {personagem.energia}/{personagem.energia_max}', x + 8, 502, NOME_FONT, WHITE)

            pygame.draw.rect(screen, (55, 55, 55), (x + 8, 516, 139, 5))
            largura_ep = round(139 * personagem.energia / personagem.energia_max) if personagem.energia_max else 0
            pygame.draw.rect(screen, (65, 125, 190), (x + 8, 516, largura_ep, 5))

        # Botões de ação (apenas visuais nesta etapa)
        personagem_atual = equipe_batalha[aliado_selecionado]

        btn('Q  GOLPE BÁSICO', 540, 470, 175, 45, True)

        btn(
            'E  HABILIDADE',
            730, 470, 190, 45,
            personagem_atual.energia >= Personagem.CUSTO_ESPECIAL
        )

        if now < notice_until:
            txt(notice, 540, 440, SMALL, GOLD)        
    elif state=='battle':
        
       
        backdrop('storm' if phase==2 else 'fire',t)
        tint=pygame.Surface((W,375),pygame.SRCALPHA)
        tint.fill((8,14,25,123)); screen.blit(tint,(0,0))
        
        pygame.draw.rect(screen,(16,27,38),(0,307,W,70))
        pygame.draw.line(screen,(109,126,131),(0,306),(960,306),2)
        pygame.draw.rect(screen,(9,15,25),(0,377,W,163))
        pygame.draw.line(screen,GOLD,(0,377),(W,377),2)
        # Hero and enemy actors: same portrait art language, no blocky placeholder sprites.
        actor('maira2' if phase==2 else 'maira',148,317,263,True)
        txt('MAÍRA',115,50,SMALL,GOLD)
        centers=(432,628,827)
        keys=('soldier','soldier','leader')
        for i,e in enumerate(enemies):
            if not e.esta_vivo():continue
            cx=centers[i]
            actor(keys[i],cx,316,216 if i<2 else 238,selected==i,flip=(i==1))
            if selected==i:
                pygame.draw.polygon(screen,GOLD,[(cx-9,79),(cx+9,79),(cx,93)])
                pygame.draw.line(screen,GOLD,(cx-61,326),(cx+61,326),3)
            plate=pygame.Rect(cx-91,32,182,49)
            pygame.draw.rect(screen,(10,20,33),plate,border_radius=6)
            pygame.draw.rect(screen,(70,83,91),plate,1,border_radius=6)
            f=pygame.font.SysFont('arial',15,bold=True)
            label='Líder da Patrulha' if i==2 else e.nome
            screen.blit(f.render(label,True,GOLD if i==2 else WHITE),(plate.x+9,plate.y+5))
            pygame.draw.rect(screen,(48,54,65),(plate.x+9,plate.y+32,164,9),border_radius=3)
            pygame.draw.rect(screen,RED,(plate.x+9,plate.y+32,round(164*e.vida/e.vida_max),9),border_radius=3)
            hp_txt=SMALL.render(f"{e.vida}/{e.vida_max} HP",True,WHITE)
            screen.blit(hp_txt,(cx-hp_txt.get_width()//2,334))
        # Fixed HUD: status row, action row, and help line.
        txt('MAÍRA',26,392,SMALL,GOLD)
        txt(f'HP {maira.vida}/{maira.vida_max}',139,392,SMALL)
        txt(f'EP {maira.energia}/{maira.energia_max}',292,392,SMALL,BLUE)
        pygame.draw.rect(screen,(48,54,65),(139,414,130,8),border_radius=3)
        pygame.draw.rect(screen,GREEN,(139,414,round(130*maira.vida/maira.vida_max),8),border_radius=3)
        pygame.draw.rect(screen,(48,54,65),(292,414,130,8),border_radius=3)
        pygame.draw.rect(screen,BLUE,(292,414,round(130*maira.energia/maira.energia_max),8),border_radius=3)
        txt('ALVO: '+(enemies[selected].nome if enemies[selected].esta_vivo() else 'Derrotado'),477,392,SMALL)
        b0=btn('Q  Golpe de Lança',26,429,222,50,True)
        b1=btn('E  '+('Raio (25 EP)' if phase==2 else 'Investida (25 EP)'),266,429,278,50,maira.energia>=Personagem.CUSTO_ESPECIAL)
        b2=btn('ATACAR  Enter',736,429,195,50)
        pygame.draw.rect(screen,GOLD,b0 if selected_action==0 else b1,3,border_radius=3)
        if now<notice_until:txt(notice,28,499,SMALL,GOLD)
        else:txt('1 / 2 / 3  selecionar alvo     Q / E  habilidade     Enter  atacar',28,499,SMALL)
        shake=max(0,shake-1)
    elif state=='defeat':
        backdrop('storm',t);rect((6,10,20),(0,0,W,H))
        txt('Maíra caiu em batalha',230,180,MID,RED)
        txt('Enter ou clique para tentar a revanche novamente',195,270,FONT)
    elif state=='end':
               screen.blit(TELA_FIM,(0,0))
    pygame.display.flip()
pygame.quit()
