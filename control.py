import pygame

def cam_control(cam_cor, SCALE):
    base_speed = 1 # bu sabiti isteğine göre ayarla
    cam_speed = max(base_speed * SCALE, 1e-2)
    keys = pygame.key.get_pressed()
    cam_speed2 = cam_speed * 0.25   # Ctrl ile yavaş hareket
    cam_x,cam_y =cam_cor[0] ,cam_cor[1]
    if keys[pygame.K_w] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
        cam_y -= cam_speed2 
    elif keys[pygame.K_w]:
        cam_y -= cam_speed 

    if keys[pygame.K_s] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
        cam_y += cam_speed2 
    elif keys[pygame.K_s]:
        cam_y += cam_speed 

    if keys[pygame.K_a] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
        cam_x -= cam_speed2 
    elif keys[pygame.K_a]:
        cam_x -= cam_speed 

    if keys[pygame.K_d] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
        cam_x += cam_speed2 
    elif keys[pygame.K_d]:
        cam_x += cam_speed 

    return cam_x, cam_y
    
def to_screen(w,Scale,cam,obj):
    camx, camy= cam[0],cam[1] 
    x = w // 2 + (obj.x - camx) / Scale
    y = w // 2 + (obj.y - camy) / Scale
    return x,y
def draw_cir(screen,W,D,cam_cor,SCALE,ALL):
    for body in ALL:
        radius = max(1, int(body.r / SCALE * D))
        x1,y1 =to_screen(W,SCALE,cam_cor,body)
        pygame.draw.circle(screen, body.color, (int(x1), int(y1)),radius)

def draw_grid(screen, cam_cor, scale, cell_size, color=(50, 50, 50)):
    cam_x, cam_y = cam_cor[0], cam_cor[1]
    width, height = screen.get_size()
    start_x = -((cam_x % cell_size) * scale)
    start_y = -((cam_y % cell_size) * scale)
    
    for x in range(int(start_x), width, int(cell_size * scale)):
        pygame.draw.line(screen, color, (x, 0), (x, height))
    for y in range(int(start_y), height, int(cell_size * scale)):
        pygame.draw.line(screen, color, (0, y), (width, y))