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
    if r <= (r1 + r2):
        # İki boyutlu elastik çarpışma formülü
        nx = dx / r
        ny = dy / r
        # İki topun hızlarının çarpışma doğrultusundaki bileşenleri
        p = 2 * (obj1.vx * nx + obj1.vy * ny - obj2.vx * nx - obj2.vy * ny) / (obj1.m + obj2.m)
        obj1.vx = obj1.vx - p * obj2.m * nx
        obj1.vy = obj1.vy - p * obj2.m * ny
        obj2.vx = obj2.vx + p * obj1.m * nx
        obj2.vy = obj2.vy + p * obj1.m * ny
        # Topları üst üste binmekten kurtar (opsiyonel)
        overlap = (r1 + r2) - r
        obj1.x -= nx * overlap / 2
        obj1.y -= ny * overlap / 2
        obj2.x += nx * overlap / 2
        obj2.y += ny * overlap / 2
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
