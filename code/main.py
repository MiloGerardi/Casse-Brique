import pygame
from pygame import Vector2
import core
from fenetre import Fenetre
from brique import Brique
from barre import  Barre
from bille import Bille

b = Brique()
ba = Barre()
bi = Bille()
def setup():
    f = Fenetre()
    f.defTaille(800,800)
    f.defFps(60)
    f.defCouleur((0,0,0))
    f.set(core)
    core.cleanScreen()
    core.printMemory()
    bi.setPosition(Vector2(100,100))
    bi.setVitesse(Vector2(1, 1))
    bi.setAcceleration(Vector2(0, 2))


def run():
    core.cleanScreen()
    b.afficher(core)
    ba.afficher(core)
    bi.afficher(core)
    bi.deplacer(core)

core.main(setup, run)