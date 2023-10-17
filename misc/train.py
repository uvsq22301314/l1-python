import pygame
from pygame.locals import *
import time
import sys
import sncfrequetes as req
from datetime import datetime, timedelta
import math

pygame.init()
screen = pygame.display.set_mode((1400, 800))
screen.fill((204,202,204))

def renvoie_heure_minute():
    heure_actuelle = time.localtime()
    heure = heure_actuelle.tm_hour
    minutes = heure_actuelle.tm_min
    return f"{str(heure).zfill(2)}:{str(minutes).zfill(2)}"

class Train():
    def __init__(self, type: str, numero: str, terminus: str, heure_arrivee: str, arrets: list, statut: str = "TBD", voie: str = ""):
        self.type = type            # Type de train (ex: "TGV", "TER", etc.)
        self.numero = numero        # Numéro du train
        self.terminus = terminus    # Terminus du train
        self.heure_arrivee = heure_arrivee  # Heure d'arrivée prévue
        self.arrets = arrets        # Liste des arrêts du train
        self.statut = statut        # Statut du train : à quai, à l'approche, 50 min ... (par défaut "TBD")
        self.voie = voie            # Voie d'arrivée du train (par défaut "")

        self.composants_dessins = {
            "rect": (),
            "type": (),
            "id": (),
            "terminus": (),
            "arrets": [(),()],
            "status": (),
            "quai": ()
        }
        self.animation_arret = 0
        self.animation2 = 0
        self.rect = 0
        self.taille_arret = ()

        self.tour = 0

        self.passer = False # Le train a-t-il effectué son départ de la station

    def init_coord(self, last_rectangle_coordy):
        rect = pygame.Rect(10, last_rectangle_coordy, 1250, 100)
        self.rect = rect
        r = pygame.Rect(1270, last_rectangle_coordy + 10, 90, 60)

        

        txt = pygame.font.SysFont("Arial Nova", 30)
        txt = txt.render("> " + " > ".join(self.arrets), True, (246, 250, 253))
        self.taille_arret = txt.get_size()
        if self.taille_arret[0] < 1200:
            self.animer = False
        else:
            self.animer = True
        txt = (txt, txt.get_rect())
        
        type = self.creer_texte("Arial Nova", 60, self.type, (246, 250, 253))
        type[1].midleft = (40, rect.centery)

        ide = self.creer_texte("Cambria", 30, self.numero, (150, 173, 186))
        ide[1].midleft = (140, rect.centery - 20)

        terminus = self.creer_texte("Arial Nova", 60, self.terminus, (246, 250, 253))
        if terminus[1].width > 1000:
            terminus = self.creer_texte("Arial Nova", 40, self.terminus, (246, 250, 253))
        terminus[1].midleft = (265, rect.centery - 20)

        status = self.creer_texte("Cambria", 30, self.statut, (246, 250, 253))
        status[1].midright = (1245, rect.centery - 20)

        voie = self.creer_texte("Arial Nova", 60, self.voie, (25, 25, 63))
        voie[1].center = (r.centerx, r.centery)

        self.jesaispas = rect.centery + 20
        
        self.composants_dessins = {
            "rect": pygame.Rect(20, last_rectangle_coordy, 1250, 100),
            "type": type,
            "id": ide,
            "terminus": terminus,
            "status": status,
            "arrets": txt,
            "quai": voie
        }
        
        self.animation2 = -txt[1].width + 564 - 1125
        

    def reinitialiser_animations(self):
        self.animation_arret = 0
        self.animation2 = 0
    
    def effacer_train(self):
        pygame.draw.rect(screen, (204,202,204), pygame.Rect(0, self.composants_dessins["rect"].y, 1400, 100))

    
    
    def animer_stations(self):
        self.animation_arret = self.animation_arret - 1
        self.animation2 = self.animation2 - 1

        if self.animation_arret <= (- 2*self.composants_dessins["arrets"][1].width):
            self.animation_arret = 1125
        elif self.animation2 <= (- 2*self.composants_dessins["arrets"][1].width):
            self.animation2 = 1125
        

        # Créez une nouvelle surface pour le texte
        text_surf = pygame.Surface((1125, 30))
        text_surf.fill((25, 25, 63))  # Remplissez la surface avec une couleur de fond (noir)

        # Rendu du texte sur la nouvelle surface
        text_surf.blit(self.composants_dessins["arrets"][0], (self.animation_arret, 0))
        text_surf.blit(self.composants_dessins["arrets"][0], (self.animation2, 0))

        # Créez une surface de masquage
        mask_surf = pygame.Surface((1125, 30))
        mask_surf.fill((25, 25, 63))  # Remplissez la surface de masquage avec une couleur de fond (noir)

        # Calculez la partie visible du texte en fonction de self.animation_arret
        visible_width = 1125

        # Remplissez la partie masquée de la surface de masquage avec une couleur d'arrière-plan
        mask_surf.fill((25, 25, 63), (visible_width, 0, 1125 - visible_width, 30))

        # Affichez la surface de masquage sur l'écran
        screen.blit(mask_surf, (140, self.jesaispas))

        # Affichez la nouvelle surface de texte au-dessus de la surface de masquage
        screen.blit(text_surf, (140, self.jesaispas))

    def afficher_station_sans_animation(self):
        screen.blit(self.composants_dessins["arrets"][0], (140, self.jesaispas))
   
        

    def afficher_train(self):
        self.calculer_temps_restant()
        rect_prec = self.composants_dessins["rect"].y
        # Grand RECTANGLE DE BASE
        pygame.draw.rect(screen, (25, 25, 63), self.composants_dessins["rect"], 0, border_bottom_left_radius=10,border_bottom_right_radius=10,border_top_left_radius=10)

        # Quai 
        pygame.draw.rect(screen, (25, 25, 63), pygame.Rect(1270, rect_prec, 100, 80), border_bottom_right_radius=10, border_top_right_radius=10)
        pygame.draw.rect(screen, (246, 250, 253), pygame.Rect(1270, rect_prec + 10, 90, 60), border_bottom_right_radius=10, border_top_right_radius=10)

        changement = ["quai", "type", "id", "terminus", "status"]
        for change in changement:
            texte, texte_rec = self.composants_dessins[change]
            screen.blit(texte, texte_rec)


    def creer_texte(self, nom_police, taille, label, couleur):
        police = pygame.font.SysFont(nom_police, taille)
        text = police.render(label, True, couleur)
        return (text, text.get_rect())

    def calculer_temps_restant(self):
        difference = self.heure_arrivee - datetime.now()
        if difference.total_seconds() >= 60:
            minutes = difference.total_seconds() / 60
            self.statut = f"{math.floor(minutes)} min"
        
        elif difference.total_seconds() >= 0:
            self.statut = "À l'approche"

        elif difference.total_seconds() >= -60:
            self.statut = "À quai"

        else:
            self.passer = True

        status = self.creer_texte("Cambria", 30, self.statut, (246, 250, 253))
        status[1].midright = (1245, self.rect.centery - 20)
        self.composants_dessins["status"] = status


txttt = pygame.font.SysFont("Arial", 30).render("Nous préparons votre affichage", True, (246, 250, 253))
re = txttt.get_rect()
taille = pygame.display.get_window_size()
re.center = [ taille[0]//2, taille[1]//2 - 20]
screen.blit(txttt, re)

pygame.display.update()

def creer_classes_cinq_train():
    liste_train = []
    liste_voie = ["C", "F", "H", "E", "F"]
    j_en = 0
    for i in range(5):
        x = 110 + 110*i - 110*j_en
        inf = req.req(i)
        if inf != "E":
            tr = Train(inf["ligne"], inf["id"], inf["terminus"], inf["arrivee"], inf["arrêts"], voie=liste_voie[i])
            liste_train.append(tr)
            tr.init_coord(x)
        else:
            j_en += 1
    return liste_train

liste_train = creer_classes_cinq_train()


"""
tTER2 = Train("TER", "849950", "Paris-Montparnasse Hall 1 & 2", "15:39", ['Chartres', 'La Villette Saint-Prest', 'Jouy', 'Saint-Piat', 'Maintenon', 'Épernon', 'Gazeran', 'Rambouillet', 'Versailles Chantiers', 'Paris-Montparnasse Hall 1 & 2'], voie="E")
tTER2.init_coord(220)
tTER2.afficher_train()
tTER2.statut = "10 min"

tTER = Train("TER", "849950", "Chartres", "14:25", ["Paris-Montparnasse Hall 1 & 2", "Versailles Chantiers", "Rambouillet", "Gazeran", "Épernon", "Maintenon", "Saint-Piat", "Jouy", "La Villette Saint-Prest", "Chartres"], voie="F")
tTER.init_coord(110)
tTER.afficher_train()
tTER.statut = "à quai"
"""

# Grand rectangle au dessus
pygame.draw.rect(screen, (246, 250, 253), pygame.Rect(0, 0, 1400, 70))

# Texte "Prochains trains"
police = pygame.font.SysFont("Arial Nova", 60)
texte = police.render("Prochains Trains", True, (101, 120, 131))
texte_rec = texte.get_rect()
texte_rec.center = (400, 35)
screen.blit(texte, texte_rec)



def afficher_heure():

    # Rectangle heure en gris
    r1 = pygame.Rect(20, 10, 100, 50)
    pygame.draw.rect(screen, (87, 105, 115), r1, 0, 10)

    # Heure 
    police = pygame.font.SysFont("Cambria", 30)
    texte = police.render(renvoie_heure_minute(), True, (223, 240, 245))
    texte_rec = texte.get_rect()
    texte_rec.center = r1.center
    screen.blit(texte, texte_rec)

# Voie
rectttt = pygame.Rect(1270, 15, 100, 40)
pygame.draw.rect(screen, (25, 25, 63), rectttt, 0, 10)

police = pygame.font.SysFont("Arial Nova", 45)
texte = police.render("Voie", True, (223, 240, 245))
texte_rec = texte.get_rect()
texte_rec.center = rectttt.center
screen.blit(texte, texte_rec)

clock = pygame.time.Clock()
continuer = True
while continuer:
    afficher_heure()
    for train in liste_train:
        train.effacer_train()
        train.afficher_train()
        if train.animer:
            train.animer_stations()
        else:
            train.afficher_station_sans_animation()
        if train.passer:
            liste_train = creer_classes_cinq_train()
    
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = False
    
    clock.tick(60)

pygame.quit()






""" def animer_stations(self):
        largeur = 1200
        self.animation_arret = (self.animation_arret - 1) % largeur

        screen.blit(self.composants_dessins["arrets"][0][0], (self.animation_arret, self.composants_dessins["arrets"][1][1]))

        
        if self.animation_arret + self.taille_arret[0] > largeur:
            fin_largeur = self.animation_arret + self.taille_arret[0] - largeur
            fin_rect = pygame.Rect(self.taille_arret[0] - fin_largeur, 0, fin_largeur, self.taille_arret[1])
            fin_msg = self.composants_dessins["arrets"][0][0].subsurface(fin_rect)

            screen.blit(fin_msg, (140, self.composants_dessins["arrets"][1][1]))
"""