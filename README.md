# Pong Python Vibecoding

Juego clásico de Pong creado en Python con `pygame`.

## Estructura

- `main.py`: punto de entrada.
- `requirements.txt`: dependencias.
- `.gitignore`: archivos generados ignorados.
- `src/`: código del juego.
  - `game.py`: lógica principal y bucle del juego.
  - `paddle.py`: clase para las palas.
  - `ball.py`: clase para la pelota.
  - `settings.py`: constantes de configuración.
- `docs/prompts.md`: guía y prompts relacionados.

## Requisitos

- Python 3.8+
- `pygame`

## Instalación

```bash
python -m pip install -r requirements.txt
```

## Ejecución

```bash
python main.py
```

## Controles

- Jugador 1: `W` / `S`
- Jugador 2: `ARRIBA` / `ABAJO`

## Objetivo

Anotar 10 puntos antes que el rival.
