import pygame
from time import sleep
import random


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


dis_width = 800
dis_height = 600


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game")

game_over = False

x1 = dis_width/2
y1 = dis_height/2

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [100, 200])


def play_game():

    game_over = False
    game_close = False

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(white)
            message("You lost! Press Q-quit or C-play again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        play_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        x1 += x1_change
        y1 += y1_change

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        dis.fill(white)
        pygame.draw.rect(dis, blue, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            print("Yummy")
        clock.tick(30)

    pygame.quit()
    quit()


if __name__ == '__main__':
    play_game()
