from pygame.math import Vector2
import pygame


class Bille:
    def __init__(self):
        self.rayon = 5
        self.position = Vector2(0,0)
        self.masse = 0
        self.couleur = (255,255,255)
        self.vitesse = Vector2(0,0)
        self.vitesseMax = 0
        self.vitesseMin = 0
        self.positionDepart = Vector2(0,0)
        self.acceleration = Vector2(0,0)
        self.accMax = 0
        self.accMin = 0
        self.force = Vector2(0,0)
        self.nom = ""
        self.score = 0

    def setVitesse(self, v):
        self.vitesse = v

    def setAcceleration(self, a):
        self.acceleration = a
        self.vitesse += self.acceleration

    def setPosition(self, pos):
        self.position = pos

    def deplacer(self, core):

        if self.position.x >= core.WINDOW_SIZE[0] or self.position.x <= 0:
            self.vitesse = self.vitesse.rotate(180 + 2 * self.vitesse.angle_to((1, 0)))

        if self.position.y >= core.WINDOW_SIZE[1] or self.position.y <= 0:
            self.vitesse = self.vitesse.rotate(180 + 2 * self.vitesse.angle_to((0, 1)))

        self.position += self.vitesse
        self.acceleration = Vector2(0,0)

    def afficher(self, core):
        pygame.draw.circle(core.screen, self.couleur, self.position, self.rayon)