import physicsengine as phypy
import math
from constants import *

v = 5e3
d = 5e11
m = sm*5e8
r = 5e10
cor1 = (0,-d)
L = 2*d*math.sin(math.pi/6)
cor2 = (-L,d)
cor3 = (L,d)



# Yıldızlar birbirlerinin etrafında zıt yönlü döner


bodyB = phypy.objcir(
    cor = cor2,
    mass = m*2,
    radius = r,
    startvelocity = (0,0),
    color = colors["RED"]
)
bodyC = phypy.objcir(
    cor = cor3,
    mass = m,
    radius = r,
    startvelocity = (v/2,0),
    color = colors["BLUE"]
)
bodyD = phypy.objcir(
    cor = cor1,
    mass = m,
    radius = r,
    startvelocity = (0,v/2),
    color = colors["YELLOW"]
)



bodys1 = [bodyB,bodyC,bodyD]
