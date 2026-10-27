import pygame
import math

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("Atoms/attract.wav")
pygame.mixer.music.set_volume(0.5)

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
running = True
clock = pygame.time.Clock()

G = 1000

x1 = 200
y1 = 450
vx1 = 0
vy1 = 0
MASS = 25

x2 = 600
y2 = 350
vx2 = 0
vy2 = 0
MASS2 = 25

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    
    circle1 = pygame.draw.circle(screen, (255, 0, 0), (x1, y1), 10)
    circle2 = pygame.draw.circle(screen, (0, 0, 255), (x2, y2), 10)
    
    cr_rect = pygame.Rect(x1, y1, 20, 20)
    cr_rect2 = pygame.Rect(x2, y2, 20, 20)
    
    dx = x2 - x1 
    dy = y2 - y1
    
    angle = math.atan2(dy, dx)
    
    r = math.hypot(dx, dy)
    
    r = max(20, r)
    
    F = G * MASS * MASS2 / r**2
    
    fx = F * math.cos(angle)
    fy = F * math.sin(angle)
    
    vx1 += fx / MASS
    vy1 += fy / MASS
    
    vx1 = max(-20, min(20, vx1))
    vy1 = max(-20, min(20, vy1))
    
    vx2 -= fx / MASS2
    vy2 -= fy / MASS2

    vx2 = max(-20, min(20, vx2))
    vy2 = max(-20, min(20, vy2))
    
    x1 += vx1
    y1 += vy1
    
    x2 += vx2
    y2 += vy2
    
    if x1 >= W or x1 <= 0:
        vx1 *= -1
    if x2 >= W or x2 <= 0:
        vx2 *= -1
    if y1 >= H or y1 <= 0:
        vy1 *= -1
    if y2 >= H or y2 <= 0:
        vy2 *= -1
        
    print(f"x1: {x1}, x2: {x2}, y1: {y1}, y2: {y2}")
    
    if cr_rect.colliderect(cr_rect2):
        pygame.mixer.music.play()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
