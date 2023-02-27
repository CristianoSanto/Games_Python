import pygame
import time
import random
 
pygame.init()
 
# Definição de cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# Definição da largura e altura da tela
dis_width = 600
dis_height = 400
 
# Criação da tela
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Jogo da Cobrinha')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
# Função para exibir a mensagem na tela
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
# Função principal do jogo
def gameLoop():
    game_over = False
    game_close = False
 
    # Início da posição da cobra
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    # Alteração na posição da cobra
    x1_change = 0
    y1_change = 0
 
    # Criação da comida em uma posição aleatória
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(white)
            message("Você perdeu! Pressione Q-Sair ou C-Jogar novamente", red)
            pygame.display.update()
 
            # Criação da opção para jogar novamente ou sair do jogo
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        # Movimentação da cobra
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        # Verificação de colisão com as paredes
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        # Alteração na posição da cobra
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
 
        # Desenho da comida
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
 
          # Desenho da cobra
        pygame.draw.rect(dis, blue, [x1, y1, snake_block, snake_block])
        pygame.display.update()
 
        # Verificação de colisão com a comida
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
 
        # Criação de uma nova comida em uma posição aleatória
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
        clock.tick(snake_speed)
 
    # Finalização do pygame
    pygame.quit()
 
    # Finalização do sistema
    quit()
 
gameLoop()

