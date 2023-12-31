import pygame
from pygame.locals import *
import random 

#dimensões
TAMANHO_JANELA = (600,600)
TAMANHO_PIXEL = 10

#funções:
#  |
#  V

#//Função colisão e limite da parede
def colisao(pos1, pos2):
    return pos1 == pos2

def limite_parede(pos):
    if 0 <= pos[0] < TAMANHO_JANELA[0] and 0 <= pos[1] < TAMANHO_JANELA[1]:
        return False
    else:
        return True

#//Função aleatoridade da maçã
def random_tela():
    x = random.randint(0, TAMANHO_JANELA[0])
    y = random.randint(0, TAMANHO_JANELA[1])
    return x // TAMANHO_PIXEL * TAMANHO_PIXEL, y // TAMANHO_PIXEL * TAMANHO_PIXEL

#// Função restart
def reiniciar_jogo():
    global cobra_pos
    global maça_pos
    global cobra_direçao
    cobra_pos = [(250, 50), (260, 50), (270, 50)]
    cobra_direçao = K_LEFT 
    maça_pos = random_tela()

#//função do contador
def desenhar_pontos(pontuaçao):
    fonte = pygame.font.SysFont('Helvetica', 30)
    texto = fonte.render(f"pontos: {pontuaçao}", True, (255,255,255))
    janela.blit(texto, [1,1])


#Gerar janela
pygame.init()
janela = pygame.display.set_mode(TAMANHO_JANELA)
pygame.display.set_caption("A VIDA SNAKE")

#variaveis
cobra_pos = [(250, 50), (260, 50), (270, 50)]
cobra_superfice = pygame.Surface((TAMANHO_PIXEL, TAMANHO_PIXEL))
cobra_superfice.fill((255, 255, 255))
cobra_direçao = K_LEFT 
tamanho_cobra = 1

maça_superfice = pygame.Surface((TAMANHO_PIXEL, TAMANHO_PIXEL))
maça_superfice.fill((255, 0, 0))
maça_pos = random_tela()

pontos = 0

#Looping (janela e, direção da cobra)
while True:
    pygame.time.Clock().tick(15)
    janela.fill((0,0,0))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            quit()

        elif evento.type == KEYDOWN:
            if evento.key in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
                cobra_direçao = evento.key 

    janela.blit(maça_superfice, maça_pos)

    
    
#colisões
    if colisao(maça_pos, cobra_pos[0]):
        cobra_pos.append((-10,-10))
        maça_pos = random_tela()
        pontos = pontos+1
    desenhar_pontos(pontos)

        
    for pos in cobra_pos:
        janela.blit(cobra_superfice, pos)


    for i in range(len(cobra_pos)-1,0,-1):
        if colisao(cobra_pos[0], cobra_pos[i]):
           reiniciar_jogo()
           pontos = 0
        cobra_pos[i] = cobra_pos[i-1]
      

    if limite_parede(cobra_pos[0]):
      pontos = 0
      reiniciar_jogo()


#direção da cobra(teclado)
    if cobra_direçao == K_UP:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] - TAMANHO_PIXEL)
    elif cobra_direçao == K_DOWN:
        cobra_pos[0] = (cobra_pos[0][0], cobra_pos[0][1] + TAMANHO_PIXEL)
    elif cobra_direçao == K_LEFT:
        cobra_pos[0] = (cobra_pos[0][0] -TAMANHO_PIXEL, cobra_pos[0][1])
    elif cobra_direçao == K_RIGHT:
        cobra_pos[0] = (cobra_pos[0][0] + TAMANHO_PIXEL, cobra_pos[0][1])

#Atualizações da janela
    pygame.display.update()