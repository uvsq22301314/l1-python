import pygame
from pygame.locals import *
pygame.init()
import time
from random import randint


screen = pygame.display.set_mode((1400, 800))
screen.fill((0,0,0))

coordonnee_centre = screen.get_rect().center

def afficher_chrono(temps):
    seconde, minute = temps % 60, temps // 60
    police = pygame.font.SysFont("Cambria", 80)
    texte = police.render(f"{str(minute).zfill(2)}:{str(seconde).zfill(2)}", True, (250, 250, 250))
    rect = texte.get_rect()
    rect.center = coordonnee_centre
    screen.blit(texte, rect)

rectangle = pygame.Rect(0, 0, 150, 50)
rectangle.topright = (coordonnee_centre[0] - 10, coordonnee_centre[1] + 50)
rectangle2 = pygame.Rect(0, 0, 150, 50)
rectangle2.topleft = (coordonnee_centre[0] + 10, coordonnee_centre[1] + 50)

continuer = True
i = 0
j = 1
while continuer:
    afficher_chrono(i)
    pygame.draw.rect(screen, (250,0,0), rectangle)
    pygame.draw.rect(screen, (0,250,0), rectangle2)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == MOUSEBUTTONDOWN:
            if rectangle.collidepoint(event.pos):
                j = 0
            elif rectangle2.collidepoint(event.pos):
                j = 1
    i += j
    screen.fill((0, 0, 0))
    time.sleep(0.99)

pygame.quit()