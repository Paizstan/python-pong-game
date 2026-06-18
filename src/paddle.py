import pygame
from src.settings import PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED


class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move_up(self) -> None:
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self) -> None:
        if self.rect.bottom < pygame.display.get_surface().get_height():
            self.rect.y += self.speed

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
