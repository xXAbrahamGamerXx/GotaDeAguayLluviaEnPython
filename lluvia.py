import pygame
import random
import os

# Inicializar pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lluvia en pygame")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sprite_sheet = pygame.image.load(os.path.join(BASE_DIR, "gotaagua.jpg")).convert()

FRAME_COUNT = 8
FRAME_WIDTH = sprite_sheet.get_width() // FRAME_COUNT
FRAME_HEIGHT = sprite_sheet.get_height()

frames = [
    sprite_sheet.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT))
    for i in range(FRAME_COUNT)
]

# Hacer transparente el fondo negro del sprite
for f in frames:
    f.set_colorkey((0, 0, 0))

# Punto de impacto dentro del frame (donde la gota toca el suelo)
# Analizando la imagen: la base de la salpicadura está en y≈96 de 115px
IMPACT_Y = 96  # píxel dentro del frame que se alinea con el suelo

GROUND_Y = HEIGHT - 60
GROUND_COLOR = (30, 60, 30)

class Raindrop:
    FALL_FRAMES  = list(range(0, 2))   # frames 0-1: gota cayendo
    SPLASH_FRAMES = list(range(2, 8))  # frames 2-7: salpicadura

    def __init__(self):
        self.reset(spawn_top=False)

    def reset(self, spawn_top=True):
        self.x = random.randint(20, WIDTH - 20)
        self.y = random.randint(-200, -10) if spawn_top else random.randint(-200, HEIGHT - 100)
        self.vel_y = random.uniform(4, 8)
        self.falling = True
        self.frame_index = 0
        self.frame_timer = 0
        self.done = False

    def move(self):
        if self.falling:
            self.y += self.vel_y
            # Tocar suelo: cuando IMPACT_Y del frame llega a GROUND_Y
            if self.y >= GROUND_Y:
                self.y = GROUND_Y
                self.falling = False
                self.frame_index = 2   # primera frame de salpicadura
                self.frame_timer = 0

    def update_animation(self):
        self.frame_timer += 1
        delay = 5 if self.falling else 6

        if self.frame_timer >= delay:
            self.frame_timer = 0
            if self.falling:
                # Ciclar entre frames de caída
                self.frame_index = (self.frame_index + 1) % len(self.FALL_FRAMES)
            else:
                # Avanzar salpicadura hasta el final
                self.frame_index += 1
                if self.frame_index >= FRAME_COUNT:
                    self.done = True

    def draw(self, surface):
        if self.done:
            return
        idx = min(self.frame_index, FRAME_COUNT - 1)
        # Posicionar el frame para que IMPACT_Y coincida con self.y (el suelo)
        draw_x = self.x - FRAME_WIDTH // 2
        draw_y = self.y - IMPACT_Y
        surface.blit(frames[idx], (draw_x, draw_y))


NUM_DROPS = 18
raindrops = [Raindrop() for _ in range(NUM_DROPS)]

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 30))
    pygame.draw.rect(screen, GROUND_COLOR, (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y))

    for i, drop in enumerate(raindrops):
        drop.move()
        drop.update_animation()
        drop.draw(screen)
        if drop.done:
            raindrops[i] = Raindrop()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
