import pygame


pygame.init()
dis = pygame.display
dis.set_mode((400, 300))
dis.set_caption("Snake game")
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.quit()
quit()
