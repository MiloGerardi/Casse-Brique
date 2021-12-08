import pygame
from pygame import Vector2

class Barre:
    def __init__(self):
        self.taille = Vector2(50, 5)
        self.couleur = (255,255,255)
        self.position = Vector2(500,500)
        self.vitesse = 5

    def afficher(self, core):
        pygame.draw.rect(core.screen, self.couleur, (self.position, self.taille), 0, 10)

    def deplacer(self, direction):
        if direction>0 :
            self.position.x += self.vitesse
        if direction<0 :
            self.position.x -= self.vitesse

    def setVitesse(self, v):
        self.vitesse = v

    def setPosition(self, pos):
        self.position = pos

    def getVitesse(self):
        return self.vitesse

    def getPosition(self):
        return self.position

    def getTaille(self):
        return self.taille