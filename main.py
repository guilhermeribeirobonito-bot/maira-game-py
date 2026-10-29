"""Tupã: Herdeira do Trovão — capítulo 1. Python 3 + pygame."""
import random
from pathlib import Path
from roteiro import SCENES, AFTER_LOSS, ENDING, CAP2
from capitulo2 import CENA1, CENA2
import pygame

pygame.init()
W, H = 960, 540
screen = pygame.display.set_mode((W, H))
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
BACKS={n:pygame.transform.smoothscale(load('bg_'+n),(W,H)) for n in ('fire','storm','peace','dawn','floresta','equipe')}
PORTRAITS={n:load('portrait_'+n) for n in ('maira','caubi','araci','captain','leader','soldier', 'jaciara')}
ACTORS={n:load('actor_'+n) for n in ('maira','maira2','caubi','araci','captain','leader','soldier', 'jaciara')}
TELA_INICIAL=pygame.transform.smoothscale(load('tela_inicial'),(W,H))
TELA_CAPITULOS=pygame.transform.smoothscale(load('tela_capitulos'),(W,H))
TELA_FIM=pygame.transform.smoothscale(load('tela_fim'),(W,H))
# Personagens disponíveis no jogo
PERSONAGENS = [
    'Maíra',
    'Caubi',
    'Jaciara',
    'Akin',
    '???',
    '???',
    '???',
    '???',
    '???',
    '???'
]

# Personagens que já podem ser escolhidos
DESBLOQUEADOS = ['Maíra', 'Caubi', 'Jaciara']

# Equipe inicial
EQUIPE = ['Maíra', 'Caubi', 'Jaciara']
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
def desenhar_selecao_equipe():
    screen.blit(BACKS['equipe'], (0, 0))

    # Painel das dez vagas
    painel = pygame.Surface((570, 335), pygame.SRCALPHA)
    painel.fill((15, 22, 20, 205))
    screen.blit(painel, (35, 105))

    # Dez vagas organizadas em duas fileiras
    for i in range(10):
        coluna = i % 5
        linha = i // 5

        x = 55 + coluna * 108
        y = 145 + linha * 140

        vaga = pygame.Rect(x, y, 92, 112)
        pygame.draw.rect(screen, (43, 33, 26), vaga, border_radius=5)
        pygame.draw.rect(screen, (178, 137, 78), vaga, 3, border_radius=5)

    # Área da equipe escolhida
    painel_equipe = pygame.Rect(640, 105, 290, 335)
    pygame.draw.rect(screen, (15, 22, 20), painel_equipe, border_radius=8)
    pygame.draw.rect(screen, (178, 137, 78), painel_equipe, 2, border_radius=8)

    # Três vagas da equipe
    for i in range(3):
        x = 661 + i * 86
        vaga = pygame.Rect(x, 185, 78, 110)
        pygame.draw.rect(screen, (43, 33, 26), vaga, border_radius=5)
        pygame.draw.rect(screen, (178, 137, 78), vaga, 2, border_radius=5)

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

        else:
            actor('maira',270,398,340,who=='Maíra')
            actor('caubi',702,398,330,who=='Caubi',flip=True)

def portrait_for(who):
    key={
    'Maíra':'maira',
    'Caubi':'caubi',
    'Araci':'araci',
    'Jaciara':'jaciara',
    'Capitão':'captain',
    'Líder':'leader',
    'Soldado 1':'soldier',
    'Soldado 2':'soldier',
    'Soldado 3':'soldier'
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
state='menu'; idx=0; script=SCENES; phase=1; hero_hp=100; hero_ep=70; enemies=[]; turn=0; notice=''; notice_until=0; shake=0; t=0

def start_battle(second=False):
    """Cria os inimigos; second=True ativa a revanche com raios."""
    global state,phase,hero_hp,hero_ep,enemies,turn,notice,notice_until
    state='battle';phase=2 if second else 1;hero_hp=130 if second else 100;hero_ep=100;turn=0
    enemies=[{'name':'Soldado 1','hp':48,'max':48,'atk':9},{'name':'Soldado 2','hp':48,'max':48,'atk':9},{'name':'Líder da Patrulha','hp':125 if second else 110,'max':125 if second else 110,'atk':15}]
    notice='A tempestade fortalece Maíra!' if second else 'Derrote os invasores!';notice_until=pygame.time.get_ticks()+1900

def advance():
    global idx,script,state
    idx+=1
    if idx>=len(script):
        if script is SCENES:start_battle(False)
        elif script is AFTER_LOSS:start_battle(True)
        elif script is ENDING:state='end'
        elif script is CENA1:
         next_script(CENA2)

        elif script is CENA2:
             state='team_select'
def next_script(which):
    global script,idx,state
    script=which;idx=0;state='story'

def enemy_action():
    global hero_hp,notice,notice_until,shake,state
    living=[e for e in enemies if e['hp']>0]
    if not living:return
    foe=random.choice(living)
    damage=random.randint(foe['atk']-3,foe['atk']+3)
    if phase==2:damage=max(2,damage-4)
    hero_hp=max(0,hero_hp-damage)
    notice=f"{foe['name']} atacou: -{damage} HP";notice_until=pygame.time.get_ticks()+1200;shake=8
    if hero_hp<=0:
        if phase==1:next_script(AFTER_LOSS)
        else:state='defeat'

def attack(special,target):
    """Calcula dano, energia e passagem para a próxima cena."""
    global hero_ep,turn,notice,notice_until,shake
    if target<0 or target>=len(enemies) or enemies[target]['hp']<=0:return
    cost=25 if special else 0
    if hero_ep<cost:
        notice='Energia insuficiente!';notice_until=pygame.time.get_ticks()+1300;return
    hero_ep-=cost
    if special:damage=44 if phase==2 else 22
    else:damage=23 if phase==2 else 16
    enemies[target]['hp']=max(0,enemies[target]['hp']-damage)
    turn+=1;shake=5
    notice=f"{('Lança Relampejante' if phase==2 else 'Investida') if special else 'Golpe de Lança'}: {damage} de dano!"
    notice_until=pygame.time.get_ticks()+1400
    if not any(e['hp']>0 for e in enemies):
        if phase==1:next_script(AFTER_LOSS)
        else:next_script(ENDING)
        return
    # A primeira derrota faz parte do roteiro; depois vem o despertar.
    if phase==1 and turn>=5:
        notice='O líder da patrulha prepara um golpe devastador!'
        next_script(AFTER_LOSS)
        return
    enemy_action()

selected=0; selected_action=0
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
                    if pygame.Rect((432,628,827)[i]-96,30,192,307).collidepoint(mx,my):selected=i
                if pygame.Rect(26,429,222,50).collidepoint(mx,my):selected_action=0
                if pygame.Rect(266,429,278,50).collidepoint(mx,my):selected_action=1
                if pygame.Rect(736,429,195,50).collidepoint(mx,my):attack(selected_action==1,selected)
            elif state=='chapters':
                print('Clique detectado:', mx, my)

                if pygame.Rect(187,108,280,63).collidepoint(mx,my):
                    script=SCENES
                    idx=0
                    state='story'

                elif pygame.Rect(490,108,280,63).collidepoint(mx,my):
                    print('Abrindo capítulo 2')
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
        backdrop('floresta' if script in (CENA1, CENA2) else ('peace' if kind=='sleep' else kind),t)
        if kind=='sleep':
            shade=pygame.Surface((W,H),pygame.SRCALPHA);shade.fill((2,6,16,188));screen.blit(shade,(0,0))
            txt('A ALDEIA ADORMECE...',230,195,MID,GOLD)
        else:cast_scene(kind,who)
        panel(385)
        portrait_for(who)
        left=140 if who in ('Maíra','Caubi','Araci','Jaciara','Capitão','Líder','Soldado 1','Soldado 2','Soldado 3') else 46
        txt(who,left,400,FONT,GOLD)
        for j,ln in enumerate(wrap(line,FONT,785 if left==140 else 865)[:3]):
            txt(ln,left,434+j*27)
        txt('ESPAÇO / CLIQUE  >',755,495,SMALL,GOLD)
        txt(f'{idx+1}/{len(script)}',145 if left==140 else 45,495,SMALL,(173,176,175))
    elif state=='team_select':
        desenhar_selecao_equipe()
    elif state=='battle':
        # Stage screen: coherent bust-scale art for both teams, HUD kept separate.
        backdrop('storm' if phase==2 else 'fire',t)
        tint=pygame.Surface((W,375),pygame.SRCALPHA)
        tint.fill((8,14,25,123)); screen.blit(tint,(0,0))
        # Stable stage plinth and soft footline, with a clear battle hierarchy.
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
            if e['hp']<=0:continue
            cx=centers[i]
            actor(keys[i],cx,316,216 if i<2 else 238,selected==i,flip=(i==1))
            if selected==i:
                pygame.draw.polygon(screen,GOLD,[(cx-9,79),(cx+9,79),(cx,93)])
                pygame.draw.line(screen,GOLD,(cx-61,326),(cx+61,326),3)
            plate=pygame.Rect(cx-91,32,182,49)
            pygame.draw.rect(screen,(10,20,33),plate,border_radius=6)
            pygame.draw.rect(screen,(70,83,91),plate,1,border_radius=6)
            f=pygame.font.SysFont('arial',15,bold=True)
            label='Líder da Patrulha' if i==2 else e['name']
            screen.blit(f.render(label,True,GOLD if i==2 else WHITE),(plate.x+9,plate.y+5))
            pygame.draw.rect(screen,(48,54,65),(plate.x+9,plate.y+32,164,9),border_radius=3)
            pygame.draw.rect(screen,RED,(plate.x+9,plate.y+32,round(164*e['hp']/e['max']),9),border_radius=3)
            hp_txt=SMALL.render(f"{e['hp']}/{e['max']} HP",True,WHITE)
            screen.blit(hp_txt,(cx-hp_txt.get_width()//2,334))
        # Fixed HUD: status row, action row, and help line.
        txt('MAÍRA',26,392,SMALL,GOLD)
        txt(f'HP {hero_hp}/{130 if phase==2 else 100}',139,392,SMALL)
        txt(f'EP {hero_ep}/100',292,392,SMALL,BLUE)
        max_hp=130 if phase==2 else 100
        pygame.draw.rect(screen,(48,54,65),(139,414,130,8),border_radius=3)
        pygame.draw.rect(screen,GREEN,(139,414,round(130*hero_hp/max_hp),8),border_radius=3)
        pygame.draw.rect(screen,(48,54,65),(292,414,130,8),border_radius=3)
        pygame.draw.rect(screen,BLUE,(292,414,round(130*hero_ep/100),8),border_radius=3)
        txt('ALVO: '+(enemies[selected]['name'] if enemies[selected]['hp']>0 else 'Derrotado'),477,392,SMALL)
        b0=btn('Q  Golpe de Lança',26,429,222,50,True)
        b1=btn('E  '+('Raio (25 EP)' if phase==2 else 'Investida (25 EP)'),266,429,278,50,hero_ep>=25)
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
