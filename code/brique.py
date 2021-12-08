import random
from pygame import Vector2
import pygame

class Brique:
    def  __init__(self):
        self.largeur = 50
        self.hauteur = 20
        self.couleur = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        self.position = Vector2(300,300)
        self.vie = 1
        self.taille = Vector2(self.largeur, self.hauteur)

    def hit(self, force):
        self.vie -= force

    def afficher(self, core):
        pygame.draw.rect(core.screen, self.couleur, (self.position, self.taille))