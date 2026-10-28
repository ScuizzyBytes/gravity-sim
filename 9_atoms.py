import math

import pygame

pygame.init()
W, H = 800, 800
screen = pygame.display.set_mode((W, H))

atom_red = pygame.image.load("atom_red.png").convert_alpha()
atom_blue = pygame.image.load("atom_blue.png").convert_alpha()

SIZE = 20

scaled_red_atom = pygame.transform.scale(atom_red, (SIZE, SIZE))
scaled_blue_atom = pygame.transform.scale(atom_blue, (SIZE, SIZE))


COLS = 3
CELL = W // COLS

G = 1000
MASS = 20
MASS2 = 20


clock = pygame.time.Clock()

class Simulation:
    def __init__(self, col, row):
        self.ox = col * CELL
        self.oy = row * CELL
        self.x1 = CELL * 0.25
        self.y1 = CELL * 0.56
        self.vx1 = 0
        self.vy1 = 0
        self.x2 = CELL * 0.75   
        self.y2 = CELL * 0.44
        self.vx2 = 0
        self.vy2 = 0

    def update(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        angle = math.atan2(dy, dx)
        r = max(20, math.hypot(dx, dy))
        F = G * MASS * MASS2 / r**2
        fx = F * math.cos(angle)
        fy = F * math.sin(angle) 
        
        self.vx1 += fx / MASS
        self.vy1 += fy / MASS
        self.vx1 = max(-20, min(20, self.vx1))
        self.vy1 = max(-20, min(20, self.vy1))
        self.vx2 -= fx / MASS2
        self.vy2 -= fy / MASS2
        self.vx2 = max(-20, min(20, self.vx2))
        self.vy2 = max(-20, min(20, self.vy2))
        
        self.x1 += self.vx1
        self.y1 += self.vy1
        self.x2 += self.vx2
        self.y2 += self.vy2
        
        if self.x1 >= CELL or self.x1 <= 0:
            self.vx1 *= -1
        if self.y1 >= CELL or self.y1 <= 0:
            self.vy1 *= -1
        if self.x2 >= CELL or self.x2 <= 0:
            self.vx2 *= -1
        if self.y2 >= CELL or self.y2 <= 0:
            self.vy2 *= -1

    def draw(self):
        pygame.draw.rect(screen,(255, 255, 255), (self.ox, self.oy, CELL, CELL), 2)
        screen.blit(scaled_red_atom, (self.ox + self.x1 - SIZE // 2, self.oy + self.y1 - SIZE // 2))
        screen.blit(scaled_blue_atom, (self.ox + self.x2 - SIZE // 2, self.oy + self.y2 - SIZE // 2))

sims = [Simulation(i % COLS, i // COLS) for i in range(COLS * COLS)]

running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for sim in sims:
        sim.update()
        sim.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
