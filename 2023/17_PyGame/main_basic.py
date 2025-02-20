import pygame  # pylint: disable=import-error

running = True


def handle_events() -> None:
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def update() -> None:
    ...


def render(window: pygame.Surface) -> None:
    window.fill((127, 127, 127))
    pygame.display.flip()


def start() -> None:
    window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Hello World!")

    while running:
        handle_events()
        update()
        render(window)


if __name__ == "__main__":
    start()