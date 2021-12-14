import pygame
from pygame import Vector2
import core
from fenetre import Fenetre
from brique import Brique
from barre import Barre
from bille import Bille

brique = Brique()
barre = Barre()
bille = Bille()


def setup():
    f = Fenetre()
    f.defTaille(800, 600)
    f.defFps(60)
    f.defCouleur((10, 10, 10))
    f.set(core)
    core.cleanScreen()
    core.printMemory()
    bille.setPosition(Vector2(250, 100))
    bille.setVitesse(Vector2(1, 1))
    bille.setAcceleration(Vector2(0, 2))
    barre.setPosition(Vector2((core.WINDOW_SIZE[0] - barre.getTaille().x) / 2, core.WINDOW_SIZE[1] - 100))


def run():
    core.cleanScreen()
    if core.getkeyPressValue() == 275:
        barre.deplacer(1, core)
    if core.getkeyPressValue() == 276:
        barre.deplacer(-1, core)
    rebondBarre(barre, bille)

    bille.deplacer(core)
    rebondBrique(brique, bille)

    afficher()


def rebondBarre(barre, bille):
    if (bille.getPosition().x >= barre.getPosition().x - bille.getRayon()) and (
            bille.getPosition().x <= barre.getPosition().x + barre.getTaille().x + bille.getRayon()):
        if bille.getPosition().y >= barre.getPosition().y - bille.getRayon():
            rot = 2 * bille.getVitesse().angle_to((0, 1))
            decal = (barre.getPosition().x + (barre.getTaille().x / 2)) - bille.getPosition().x
            rot -= 2 * decal
            bille.setVitesse(bille.getVitesse().rotate(180 + rot))


def rebondBrique(brique, bille):
    prevX = bille.getPosition().x - bille.getVitesse().x
    prevY = bille.getPosition().y - bille.getVitesse().y
    rot = -180
    if (bille.getPosition().x >= brique.getPosition().x) and (
            bille.getPosition().x <= brique.getPosition().x + brique.getTaille().x):
        if (bille.getPosition().y >= brique.getPosition().x) and (
                bille.getPosition().y <= brique.getPosition().y + brique.getTaille().y):
            print("colision")
            if (prevX <= brique.getPosition().x) or (prevX >= brique.getPosition().x + brique.getTaille().x):
                rot = 2 * bille.getVitesse().angle_to((0, 1))
                print('rebond x')
            elif (prevY <= brique.getPosition().y) or (prevY >= brique.getPosition().y + brique.getTaille().y):
                rot = 2 * bille.getVitesse().angle_to((1, 0))
                print('rebond y')

    bille.setVitesse(bille.getVitesse().rotate(180 + rot))


def afficher():
    bille.afficher(core)
    brique.afficher(core)
    barre.afficher(core)


core.main(setup, run)
