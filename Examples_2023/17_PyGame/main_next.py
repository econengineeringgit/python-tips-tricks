import random

import pygame  # pylint: disable=import-error

running = True
bird_x = 100
bird_y = 50
jump = 0
pipe_x = None
pipe_y = None
countdown_to_pipe = 100
point = 0
point_cooldown = 0
game_over = False


def handle_events() -> None:
    global running, jump
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if jump == 0:
                    jump = 15


def collision() -> bool:
    global point, point_cooldown
    if isinstance(pipe_x, int):
        # top pipe
        if bird_x >= pipe_x and bird_x <= pipe_x + 50 and bird_y >= 0 and bird_y <= pipe_y:
            return True
        # bottom pipe
        if bird_x >= pipe_x and bird_x <= pipe_x + 50 and bird_y >= pipe_y + 200 and bird_y <= 600:
            return True
        if bird_x >= pipe_x and bird_x <= pipe_x + 50 and bird_y >= pipe_y and bird_y < pipe_y + 200 and point_cooldown == 0:
            point += 1
            point_cooldown = 20
    return False


def update(dt: float) -> None:
    global bird_y, jump, countdown_to_pipe, pipe_x, pipe_y, game_over, point_cooldown

    if jump == 0:
        bird_y += 0.3 * dt
    else:
        bird_y -= 0.5 * dt
        jump -= 1

    if countdown_to_pipe != 0:
        countdown_to_pipe -= 1

    elif pipe_x is None:
        pipe_x = 850
        pipe_y = random.randint(150, 400)

    elif pipe_x == -50:
        pipe_x = 850
        pipe_y = random.randint(150, 400)

    elif pipe_x > -50:
        pipe_x -= 5

    if point_cooldown > 0:
        point_cooldown -= 1

    if collision():
        game_over = True


def render(window: pygame.Surface) -> None:
    if not game_over:
        window.fill((127, 127, 127))

        pygame.draw.circle(window, (200, 0, 0), (bird_x, bird_y), 20)

        if isinstance(pipe_x, int):
            pygame.draw.rect(window, (0, 200, 0), (pipe_x, 0, 50, pipe_y))
            pygame.draw.rect(window, (0, 200, 0), (pipe_x, pipe_y + 200, 50, 600))
    else:
        game_over_font = pygame.font.SysFont("Arial", 72)
        game_over_text = game_over_font.render("Game Over!", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect()
        game_over_text_rect.center = (800 // 2, 600 // 2)
        window.fill((127, 127, 127))
        window.blit(game_over_text, game_over_text_rect)

    point_font = pygame.font.SysFont("Arial", 24)
    point_text = point_font.render(f"Point: {point}", True, (0, 0, 0))
    point_text_rect = point_text.get_rect()
    point_text_rect.center = (50, 25)
    window.blit(point_text, point_text_rect)

    pygame.display.flip()

def start() -> None:
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Bird Game!")
    clock = pygame.time.Clock()
    pygame.font.init()

    while running:
        dt = clock.tick(60)
        handle_events()
        update(dt)
        render(window)


if __name__ == "__main__":
    start()