import pygame
from pygame.locals import *
import time

pygame.init()
screen = pygame.display.set_mode((1400, 800))
screen.fill((204,202,204))


pygame.draw.rect(screen, (246, 250, 253), pygame.Rect(0, 0, 1400 , 70))
police = pygame.font.SysFont("Arial", 30)
texte = police.render("Prochains Trains", True, (101, 120, 131))
texte_rec = texte.get_rect()
texte_rec.center = (100, 30)
screen.blit(texte, texte_rec)


pygame.draw.rect(screen, (22,28,62), pygame.Rect(20, 150, 800, 100))


continuer = True
while continuer:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
    
    time.sleep(0.5)

pygame.quit()