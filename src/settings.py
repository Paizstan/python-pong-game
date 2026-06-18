import pygame


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

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 30, bold=False)
TITLE_FONT = pygame.font.SysFont("Arial", 24, bold=True)
SCORE_FONT = pygame.font.SysFont("Arial", 60, bold=True)
GAME_OVER_TITLE_FONT = pygame.font.SysFont("Arial", 72, bold=True)
WINNER_FONT = pygame.font.SysFont("Arial", 40, bold=True)
