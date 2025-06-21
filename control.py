import pygame

def cam_control(cam_cor, SCALE):
    base_speed = 10 # bu sabiti isteğine göre ayarla
    cam_speed = max(base_speed * SCALE , 1e-2)
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

def draw_grid(screen, cam_cor, cell_size=50, color=(50, 50, 50)):
    cam_x, cam_y = cam_cor[0], cam_cor[1]
    width, height = screen.get_size()
    start_x = -((cam_x % cell_size) )
    start_y = -((cam_y % cell_size) )
    
    for x in range(int(start_x), width, int(cell_size )):
        pygame.draw.line(screen, color, (x, 0), (x, height))
    for y in range(int(start_y), height, int(cell_size )):
        pygame.draw.line(screen, color, (0, y), (width, y))

def draw_vector(screen, start, vec, color=(255,0,0), width=2):
    end = (start[0] + vec[0], start[1] + vec[1])
    pygame.draw.line(screen, color, start, end, width)
    
def draw_velocity_vectors(screen, W, SCALE, cam_cor, bodys):
    for body in bodys:
        # Hız vektörünü çiz
        # Dünya koordinatında başlangıç ve bitiş noktası
        start_world = (body.x, body.y)
        # Vektörün uzunluğunu daha kısa yapmak için bir katsayı ile çarp
        VDRS = 1e3  # Bu değeri ihtiyacına göre değiştir
        end_world = (body.x + body.vx * VDRS, body.y + body.vy * VDRS)
        # Ekran koordinatına çevir
        start_screen = to_screen(W, SCALE, cam_cor, body)
        # Geçici bir obje gibi davranmak için:
        class Temp: pass
        temp = Temp()
        temp.x, temp.y = end_world
        end_screen = to_screen(W, SCALE, cam_cor, temp)
        # Vektörü çiz
        vec = (end_screen[0] - start_screen[0], end_screen[1] - start_screen[1])
        draw_vector(screen, start_screen, vec, color=body.color, width=2)
##MENU##
#TEXT
def draw_text(surface, text, x, y , color=(0,0,0)):
        font = pygame.font.SysFont(None, 24)
        img = font.render(text, True, color)
        surface.blit(img, (x, y))
#TIME FORMAT
def format_time(seconds):
        month = int(seconds // 86400 / 28)
        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        return f"MONTH :{month},  DAY :{days},  HOUR: {hours:02}"
# DRAW MENU
def draw_menu(screen,color,dt,count,SCALE,NAME):
    pygame.draw.rect(screen, color,(5,15,400,100),0,10)
    
    draw_text(screen, f"Scale: {SCALE:.0e}", 10, 30)
    draw_text(screen, f"Data Time: {dt} per second", 10, 50)
    draw_text(screen, f"DATE: {format_time(count)}", 10, 70)
    draw_text(screen,NAME,10,90)