import pygame
import sys
import physicsengine as phypy
from constants import *
from objects import bodys1
import control
pygame.init()
#Constants:
# Screen dimensions
H = 800
W = 800

SCALE = 5e9  # Ölçek faktörü, piksel başına metre
# Time step for the simulation
dt = 10  # 1 milyon saniye (yaklaşık 11.57 gün)
cam_x = cam_y = 0
clock = pygame.time.Clock()
count = 0
running =True
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Similasyon")
ROWS = W // 50
COLS = H // 50
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      # 1 = sadece kenar çiz
    
    cam_cor = (cam_x,cam_y)
    cam_x,cam_y = control.cam_control( (cam_x, cam_y),SCALE)
    
    
    
    count += dt
    # Fizik hesaplama
    phypy.all_bodies(bodys1,dt)
    
    # Görüntüleme
    screen.fill(colors["BLACK"])
    DRS = 1
     # görsel oranlar
    control.draw_grid(screen, cam_cor, cell_size=50, color=(50, 50, 50))


    control.draw_cir(screen,W,DRS,cam_cor,SCALE/DRS,bodys1)
    control.draw_velocity_vectors(screen, W, SCALE, cam_cor, bodys1)
    control.draw_menu(screen,colors["WHITE"],dt,count,SCALE,"THE SIMULATION")
    # Ekranı güncelle
    clock.tick(60)  # FPS ayarı
    pygame.display.flip()
    
    
pygame.quit()
sys.exit()
