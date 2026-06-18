import pygame
from src.settings import BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y, SCREEN_WIDTH, SCREEN_HEIGHT


class Ball:
    def __init__(self) -> None:
        self.rect = pygame.Rect(
            SCREEN_WIDTH // 2 - BALL_SIZE // 2,
            SCREEN_HEIGHT // 2 - BALL_SIZE // 2,
            BALL_SIZE,
            BALL_SIZE,
        )
        self.reset()

    def reset(self) -> None:
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed_x = BALL_SPEED_X if pygame.time.get_ticks() % 2 == 0 else -BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y if pygame.time.get_ticks() % 2 == 0 else -BALL_SPEED_Y

    def move(self) -> None:
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1

    def draw(self, surface: pygame.Surface) -> None:
        pygame.draw.ellipse(surface, (255, 255, 255), self.rect)

    def collide_with_paddle(self, paddle_rect: pygame.Rect) -> None:
        if self.rect.colliderect(paddle_rect):
            should_bounce = (
                self.speed_x < 0 and self.rect.centerx > paddle_rect.centerx
            ) or (
                self.speed_x > 0 and self.rect.centerx < paddle_rect.centerx
            )
            if should_bounce:
                self.speed_x *= -1
