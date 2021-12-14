import random
from pygame import Vector2
import pygame


class Brique:
    def __init__(self):
        self.largeur = 50
        self.hauteur = 20
        self.couleur = (51, 204, 255)
        self.position = Vector2(300,300)
        self.vie = 1
        self.taille = Vector2(self.largeur, self.hauteur)

    def hit(self, force):
        self.vie -= force
        self.refreshColor()

    def afficher(self, core):
        pygame.draw.rect(core.screen, self.couleur, (self.position, self.taille))

    def refreshColor(self):
        if self.vie == 1:
            self.couleur = (51, 204, 255)
        elif self.vie == 2:
            self.couleur = (0, 204, 0)
        elif self.vie == 3:
            self.couleur = (255, 204, 0)
        elif self.vie == 4:
            self.couleur = (255, 26, 26)
        elif self.vie == 5:
            self.couleur = (204, 0, 153)

    def getPosition(self):
        return self.position

    def getTaille(self):
        return self.taille

    def setPosition(self, position):
        self.position = position

    def setTaille(self, taille):
        self.taille = taille
