try:
    import pygame
except ModuleNotFoundError as error:
    if error.name != "pygame":
        raise
    raise SystemExit(
        "Pygame is not installed. Install it with: python -m pip install pygame"
    ) from error
from player import Player

pygame.init()
screen = pygame.display.set_mode((750, 600))
clock = pygame.time.Clock()  # Great for controlling frame rate!
my_player = Player(375, 525)

running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Continuous Keyboard Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        my_player.move_left()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        my_player.move_right()

    # 3. Drawing / Rendering (Must be INSIDE the loop!)
    screen.fill((0, 0, 0))          # Wipe old frames black
    my_player.draw(screen)          # Draw the player
    pygame.display.flip()           # Refresh the display window

    clock.tick(60)                  # Lock game to 60 FPS

pygame.quit()