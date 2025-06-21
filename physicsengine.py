import math
G = 6.674e-11
class objcir:
    def __init__(self, cor: tuple, mass: float, radius: int, startvelocity: tuple,color: tuple):
        self.c = cor
        self.x = cor[0]
        self.y = cor[1]
        self.m = mass
        self.r = radius
        self.v = startvelocity
        self.vx = startvelocity[0]
        self.vy = startvelocity[1]
        self.color = color

def hesapla(obj1, obj2, dt):
    dx = obj2.x - obj1.x
    dy = obj2.y - obj1.y
    r = math.hypot(dx, dy) + 1e-10
    r1,r2= obj1.r ,obj2.r 
    F = G * obj1.m * obj2.m / r**2
    Fx = F * dx / r
    Fy = F * dy / r
    if r <= 2*(r1 + r2):
        obj1.vx = -obj1.vx
        obj1.vy = -obj1.vy
        return
    ax1 = Fx / obj1.m
    ay1 = Fy / obj1.m
    obj1.vx += ax1 * dt
    obj1.vy += ay1 * dt
    obj1.x += obj1.vx * dt
    obj1.y += obj1.vy * dt



def all_bodies (all,dt):
    for body01 in all:
        all2 = all.copy()  # Orijinalin kopyası
        all2.remove(body01)
        for body02 in all2:
            hesapla( body01,body02,dt)
