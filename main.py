import pygame
import sys
import physicsengine as phypy
from constants import *
from objects import bodys1
import control
pygame.init()
SCALE = 1e10
dt = 1


screen = pygame.display.set_mode((W, W))
pygame.display.set_caption("Similasyon")
ROWS = W // 50
COLS = W // 50
while running:
      # 1 = sadece kenar çiz
    
    cam_cor = (cam_x,cam_y)
    cam_x,cam_y = control.cam_control( (cam_x, cam_y),SCALE)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    count += dt
    # Fizik hesaplama
    phypy.all_bodies(bodys1,dt)
    
    # Görüntüleme
    screen.fill(colors["BLACK"])
    DRS = 10  # görsel oran
    
    control.draw_cir(screen,W,DRS,cam_cor,SCALE/DRS,bodys1)
    #control.draw_grid(screen, cam_cor, SCALE, 50, color=(50, 50, 50))
    pygame.display.flip()
    
    
pygame.quit()
sys.exit()
