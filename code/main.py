import core
from fenetre import Fenetre
from brique import Brique


def setup():
    f = Fenetre()
    f.defTaille(800,800)
    f.defFps(60)
    f.defCouleur((255,255,255))
    f.set(core)


def run():
    core.cleanScreen()
    core.printMemory()
    b = Brique()
    b.afficher(core)

core.main(setup, run)