import pygame
from src.paddle import Paddle
from src.ball import Ball
from src.settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    BLACK,
    WHITE,
    DARK_BG,
    LIGHT_BLUE,
    ORANGE,
    YELLOW,
    DARK_GRAY,
    FONT,
    TITLE_FONT,
    SCORE_FONT,
    GAME_OVER_TITLE_FONT,
    WINNER_FONT,
    WINNING_SCORE,
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    GAME_STATE_START,
    GAME_STATE_PLAYING,
    GAME_STATE_GAME_OVER,
    PADDLE_HIT_SOUND,
    SCORE_SOUND,
    GAME_OVER_SOUND,
    load_sound,
)


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pong Python Vibecoding")
        self.clock = pygame.time.Clock()

        # Paletas con colores personalizados
        self.left_paddle = Paddle(
            20, 
            SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,
            LIGHT_BLUE
        )
        self.right_paddle = Paddle(
            SCREEN_WIDTH - PADDLE_WIDTH - 20, 
            SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2,
            ORANGE
        )
        # Pelota con color amarillo
        self.ball = Ball(YELLOW)

        self.left_score = 0
        self.right_score = 0
        self.state = GAME_STATE_START
        self.running = True
        self.game_over_played = False

        self.sound_paddle = load_sound(PADDLE_HIT_SOUND)
        self.sound_score = load_sound(SCORE_SOUND)
        self.sound_game_over = load_sound(GAME_OVER_SOUND)

    def run(self) -> None:
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif self.state == GAME_STATE_START and event.key == pygame.K_SPACE:
                    self.state = GAME_STATE_PLAYING
                elif self.state == GAME_STATE_GAME_OVER and event.key == pygame.K_r:
                    self.reset_game()

        if self.state != GAME_STATE_PLAYING:
            return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.left_paddle.move_up()
        if keys[pygame.K_s]:
            self.left_paddle.move_down()
        if keys[pygame.K_UP]:
            self.right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            self.right_paddle.move_down()

    def update(self) -> None:
        if self.state != GAME_STATE_PLAYING:
            return

        self.ball.move()
        left_collision = self.ball.collide_with_paddle(self.left_paddle.rect)
        right_collision = self.ball.collide_with_paddle(self.right_paddle.rect)

        if left_collision or right_collision:
            if self.sound_paddle:
                self.sound_paddle.play()

        if self.ball.rect.left <= 0:
            self.right_score += 1
            if self.sound_score:
                self.sound_score.play()
            self.ball.reset()

        if self.ball.rect.right >= SCREEN_WIDTH:
            self.left_score += 1
            if self.sound_score:
                self.sound_score.play()
            self.ball.reset()

        if self.left_score >= WINNING_SCORE or self.right_score >= WINNING_SCORE:
            if not self.game_over_played:
                if self.sound_game_over:
                    self.sound_game_over.play()
                self.game_over_played = True
            self.state = GAME_STATE_GAME_OVER

    def draw(self) -> None:
        self.screen.fill(DARK_BG)

        if self.state == GAME_STATE_START:
            self.draw_start_screen()
        elif self.state == GAME_STATE_PLAYING:
            self.draw_center_line()
            self.left_paddle.draw(self.screen)
            self.right_paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.draw_score()
            self.draw_title()
        elif self.state == GAME_STATE_GAME_OVER:
            self.draw_game_over_screen()

        pygame.display.flip()

    def draw_center_line(self) -> None:
        for i in range(10, SCREEN_HEIGHT, 40):
            pygame.draw.rect(self.screen, DARK_GRAY, (SCREEN_WIDTH // 2 - 5, i, 10, 20))

    def draw_score(self) -> None:
        left_text = SCORE_FONT.render(str(self.left_score), True, LIGHT_BLUE)
        right_text = SCORE_FONT.render(str(self.right_score), True, ORANGE)
        self.screen.blit(left_text, (SCREEN_WIDTH // 4 - left_text.get_width() // 2, 10))
        self.screen.blit(right_text, (SCREEN_WIDTH * 3 // 4 - right_text.get_width() // 2, 10))

    def draw_title(self) -> None:
        title = TITLE_FONT.render("Pong Python", True, WHITE)
        self.screen.blit(
            title,
            (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT - 30),
        )

    def draw_start_screen(self) -> None:
        title = GAME_OVER_TITLE_FONT.render("PONG PYTHON", True, WHITE)
        subtitle = TITLE_FONT.render("Vibecoding Edition", True, LIGHT_BLUE)
        start = FONT.render("Presiona ESPACIO para comenzar", True, WHITE)
        
        controls_header = TITLE_FONT.render("Controles:", True, ORANGE)
        controls_1 = FONT.render("Jugador 1 (Azul):   W / S", True, LIGHT_BLUE)
        controls_2 = FONT.render("Jugador 2 (Naranja):   Flechas arriba / abajo", True, ORANGE)

        self.screen.blit(
            title,
            (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 4 - 40),
        )
        self.screen.blit(
            subtitle,
            (SCREEN_WIDTH // 2 - subtitle.get_width() // 2, SCREEN_HEIGHT // 4 + 30),
        )
        self.screen.blit(
            start,
            (SCREEN_WIDTH // 2 - start.get_width() // 2, SCREEN_HEIGHT // 2 - 20),
        )
        self.screen.blit(
            controls_header,
            (SCREEN_WIDTH // 2 - controls_header.get_width() // 2, SCREEN_HEIGHT // 2 + 50),
        )
        self.screen.blit(
            controls_1,
            (SCREEN_WIDTH // 2 - controls_1.get_width() // 2, SCREEN_HEIGHT // 2 + 90),
        )
        self.screen.blit(
            controls_2,
            (SCREEN_WIDTH // 2 - controls_2.get_width() // 2, SCREEN_HEIGHT // 2 + 130),
        )

    def draw_game_over_screen(self) -> None:
        winner_number = 1 if self.left_score > self.right_score else 2
        winner_color = LIGHT_BLUE if winner_number == 1 else ORANGE
        
        title = GAME_OVER_TITLE_FONT.render("GAME OVER", True, WHITE)
        winner_text = WINNER_FONT.render(f"Jugador {winner_number} gana", True, winner_color)
        
        score_text = FONT.render(
            f"Marcador Final: {self.left_score} - {self.right_score}", 
            True, 
            WHITE
        )
        
        retry = FONT.render("Presiona R para reiniciar", True, WHITE)
        quit_text = FONT.render("Presiona ESC para salir", True, WHITE)

        self.screen.blit(
            title,
            (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 4),
        )
        self.screen.blit(
            winner_text,
            (SCREEN_WIDTH // 2 - winner_text.get_width() // 2, SCREEN_HEIGHT // 4 + 80),
        )
        self.screen.blit(
            score_text,
            (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 4 + 140),
        )
        self.screen.blit(
            retry,
            (SCREEN_WIDTH // 2 - retry.get_width() // 2, SCREEN_HEIGHT // 2 + 60),
        )
        self.screen.blit(
            quit_text,
            (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100),
        )

    def reset_game(self) -> None:
        self.left_score = 0
        self.right_score = 0
        self.left_paddle.rect.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.right_paddle.rect.y = SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2
        self.ball.reset()
        self.state = GAME_STATE_START
        self.game_over_played = False
