from Ball import Ball
import constants as k
from Player import Player
from Game import Game
import pygame
import random
import cmath
import time

#inizializza pygame
pygame.init()

#inizializza finestra
window = pygame.display.set_mode((k.WIDTH, k.HEIGHT))
pygame.display.set_caption("Pong")
color = "black"

#definisce i font
win_font = pygame.font.SysFont(None, 80)
goal_font = pygame.font.SysFont(None, 100)
score_font = pygame.font.SysFont(None, 30)

#definisce i testi
win1_text = win_font.render("Player 1 Wins!", True, (255,255,255))
win2_text = win_font.render("Player 2 Wins!", True, (255,255,255))
goal_text = goal_font.render("GOAL!", True, (255,255,255))

#inizializza giocatori, pallina e partita
player1 = Player(2*k.STEP,k.HEIGHT/2,20,k.HEIGHT*0.2, k.STEP)
player2 = Player(k.WIDTH-3*k.STEP,k.HEIGHT/2,20,k.HEIGHT*0.2, k.STEP)
first_ball = Ball(k.HEIGHT/2,k.WIDTH/2,10,random.random()*2*cmath.pi,15.0) 

game = Game(player1, player2, first_ball)

#mostra il testo GOAL! dopo un goal
def show_goal_text():
    window.blit(goal_text, (k.HEIGHT/2-110, k.WIDTH/2-40))
    pygame.display.flip()
    time.sleep(1)

#verificano se i giocatori hanno segnato
def player1_has_scored():
    return game.ball.x <=k.STEP

def player2_has_scored():
    return game.ball.x - game.ball.radius >=k.WIDTH-k.STEP

#verifica se il giocatore ha vinto
def player_has_won(player):
    return player.score == k.WINNING_SCORE

#crea una nuova pallina
def new_ball():
    return Ball(k.HEIGHT/2,k.WIDTH/2,10,random.random()*2*cmath.pi,15.0)

#richiede se si vuole iniziare una nuova partita
def new_game_prompt():
    print("Vuoi fare un'altra partita? (y/n)")
    new_game = input()
    if new_game == "y":
        game.new_game()
        game.ball = new_ball()
    else:
        game.is_running = False

#loop del gioco
while game.is_running:

    #eventi con la tastiera
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]:
        player2.move_up()
    if keys[pygame.K_DOWN]:
        player2.move_down()
    if keys[pygame.K_s]:
        player1.move_down()
    if keys[pygame.K_w]:
        player1.move_up()

    #evento:chiudi la scheda
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.is_running = False

    #gameloop
    game.game_loop()
    
    #verifico se il player1 ha segnato e vinto
    if player1_has_scored():
        game.player1.score += 1
        if player_has_won(player1):
            window.blit(win1_text, (k.WIDTH/2-200, k.HEIGHT/2-30))
            pygame.display.flip()
            new_game_prompt()
        else:
            show_goal_text()
            game.ball = new_ball()

    # verifico se il player2 ha segnato e vinto
    if player2_has_scored():
        game.player2.score += 1
        if player_has_won(player2):
            window.blit(win2_text, (k.WIDTH/2-200, k.HEIGHT/2-30))
            pygame.display.flip()
            new_game_prompt()
        else:
            show_goal_text()
            game.ball = new_ball()


    # Disegno lo schermo con gli elementi aggiornati
    window.fill(color)

    p1canvas = pygame.Rect(player1.x,player1.y,player1.width,player1.heigth)
    p2canvas = pygame.Rect(player2.x,player2.y,player2.width,player2.heigth)

    pygame.draw.circle(window,(255,255,255),(game.ball.x,game.ball.y),game.ball.radius)

    pygame.draw.rect(window,(0,0,255),p1canvas)
    pygame.draw.rect(window,(0,255,0),p2canvas)

    score1_text = score_font.render(str(player1.score), True, (255,255,255))
    score2_text = score_font.render(str(player2.score), True, (255,255,255))
    window.blit(score1_text, (2*k.STEP, 20))
    window.blit(score2_text, (k.WIDTH-2*k.STEP, 20))

    pygame.display.flip()

    #passa al frame successivo
    pygame.time.Clock().tick(k.FRAME_RATE)

