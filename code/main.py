import pygame
from pygame import Vector2
import core
from fenetre import Fenetre
from brique import Brique
from barre import  Barre
from bille import Bille

brique = Brique()
barre = Barre()
bille = Bille()
def setup():
    f = Fenetre()
    f.defTaille(800,800)
    f.defFps(60)
    f.defCouleur((0,0,0))
    f.set(core)
    core.cleanScreen()
    core.printMemory()
    bille.setPosition(Vector2(100,100))
    bille.setVitesse(Vector2(1, 1))
    bille.setAcceleration(Vector2(0, 2))


def run():
    core.cleanScreen()
    if core.getkeyPressValue() == 1073741903 :
        barre.deplacer(1, core)
    if core.getkeyPressValue() == 1073741904:
        barre.deplacer(-1, core)
    if (bille.getPosition().x>barre.getPosition().x-bille.getRayon()) and (bille.getPosition().x<barre.getPosition().x + barre.getTaille().x+bille.getRayon()):
        print("x - ok")
        if bille.getPosition().y >= barre.getPosition().y - bille.getRayon():
            print("y - ok")
            bille.setVitesse(bille.getVitesse().rotate(180 + 2 * bille.getVitesse().angle_to((0, 1))))
    brique.afficher(core)
    barre.afficher(core)
    bille.deplacer(core)
    bille.afficher(core)
    #droite 1073741903
    #gauche 1073741904

core.main(setup, run)