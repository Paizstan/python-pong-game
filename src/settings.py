import pygame
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SOUNDS_DIR = BASE_DIR / "assets" / "sounds"

PADDLE_HIT_SOUND = SOUNDS_DIR / "paddle_hit.wav"
SCORE_SOUND = SOUNDS_DIR / "score.wav"
GAME_OVER_SOUND = SOUNDS_DIR / "game_over.wav"

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_SPEED = 6
BALL_SIZE = 20
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WINNING_SCORE = 10

GAME_STATE_START = "START"
GAME_STATE_PLAYING = "PLAYING"
GAME_STATE_GAME_OVER = "GAME_OVER"

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BG = (15, 20, 35)  # Fondo oscuro moderno
LIGHT_BLUE = (100, 200, 255)  # Paleta izquierda
ORANGE = (255, 165, 50)  # Paleta derecha
YELLOW = (255, 255, 0)  # Pelota
DARK_GRAY = (40, 50, 70)  # Línea central

def load_sound(path: Path) -> pygame.mixer.Sound | None:
    if not pygame.mixer.get_init():
        try:
            pygame.mixer.init()
        except pygame.error:
            return None

    if not path.exists():
        return None

    try:
        return pygame.mixer.Sound(str(path))
    except pygame.error:
        return None


pygame.font.init()
FONT = pygame.font.SysFont("Arial", 30, bold=False)
TITLE_FONT = pygame.font.SysFont("Arial", 24, bold=True)
SCORE_FONT = pygame.font.SysFont("Arial", 60, bold=True)
GAME_OVER_TITLE_FONT = pygame.font.SysFont("Arial", 72, bold=True)
WINNER_FONT = pygame.font.SysFont("Arial", 40, bold=True)
