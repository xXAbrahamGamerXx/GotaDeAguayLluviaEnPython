import pygame
import os

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animación de gota de agua")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sprite_sheet = pygame.image.load(os.path.join(BASE_DIR, "gotaagua.jpg")).convert()

FRAME_COUNT = 8
FRAME_WIDTH = sprite_sheet.get_width() // FRAME_COUNT
FRAME_HEIGHT = sprite_sheet.get_height()

frames = [
    sprite_sheet.subsurface((i * FRAME_WIDTH, 0, FRAME_WIDTH, FRAME_HEIGHT))
    for i in range(FRAME_COUNT)
]

# Hacer transparente el fondo negro
for f in frames:
    f.set_colorkey((0, 0, 0))

# Punto de impacto dentro del frame
IMPACT_Y = 96

clock = pygame.time.Clock()
frame_index = 0
animation_finished = False
frame_timer = 0
FRAME_DELAY = 8

# Posición central donde "cae" la gota (centro de pantalla, al nivel del suelo simulado)
DROP_X = WIDTH // 2
DROP_Y = HEIGHT // 2

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 10, 30))

    # Dibujar alineando IMPACT_Y del frame con DROP_Y
    draw_x = DROP_X - FRAME_WIDTH // 2
    draw_y = DROP_Y - IMPACT_Y
    screen.blit(frames[frame_index], (draw_x, draw_y))

    if not animation_finished:
        frame_timer += 1
        if frame_timer >= FRAME_DELAY:
            frame_timer = 0
            frame_index += 1
            if frame_index >= FRAME_COUNT:
                frame_index = FRAME_COUNT - 1
                animation_finished = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
