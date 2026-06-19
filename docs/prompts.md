# Prompts utilizados - Proyecto Pong (Vibecoding)

Este documento recopila los prompts utilizados durante el desarrollo del
juego Pong en Python con Pygame, usando IA (GitHub Copilot) como asistente
de programación.

---

## Prompt 1 — Creación del Proyecto

**Qué se pidió a la IA**

```text
Quiero desarrollar un juego Pong en Python utilizando Pygame.

Necesito una estructura profesional y organizada para un proyecto académico de Vibecoding.

Requisitos:

- Utilizar programación orientada a objetos.
- Separar el código en varios archivos.
- Crear una clase Game.
- Crear una clase Paddle.
- Crear una clase Ball.
- Mantener un archivo settings.py para las constantes.
- Crear un main.py como punto de entrada.
- Crear un requirements.txt.
- Explicar la responsabilidad de cada archivo.
- Seguir buenas prácticas de Python.
```

**Resultado**

La IA generó la estructura inicial del proyecto con:
- `main.py`
- `game.py`
- `paddle.py`
- `ball.py`
- `settings.py`
- `requirements.txt`

**Motivo del prompt**

Se utilizó para generar una base organizada y fácil de mantener, aplicando
programación orientada a objetos desde el inicio.

---

## Prompt 2 — Corrección de Error

**Qué se pidió a la IA**

```text
Estoy desarrollando un juego Pong en Python usando Pygame.

Al ejecutar el proyecto obtengo el siguiente error:

NameError: name 'PADDLE_HEIGHT' is not defined

Analiza el código y encuentra la causa raíz del problema.

Requisitos:

- Identifica exactamente por qué ocurre el error.
- Revisa las importaciones del archivo game.py.
- Verifica que todas las constantes utilizadas estén correctamente importadas desde settings.py.
- Indica qué líneas deben modificarse.
- Proporciona el código corregido.
- Explica brevemente la solución aplicada.
```

**Resultado**

La IA identificó que `PADDLE_HEIGHT` y `PADDLE_WIDTH` estaban siendo
utilizados en `game.py` pero no se encontraban importados desde
`settings.py`.

**Por qué se ajustó/refinó el prompt**

Se utilizó para corregir un error real encontrado durante las pruebas del
proyecto, en lugar de simplemente pedir código nuevo. Esto permitió
practicar depuración guiada por IA.

---

## Prompt 3 — Mejora Funcional del Juego

**Qué se pidió a la IA**

```text
Estoy desarrollando un juego Pong en Python usando Pygame.

El juego ya funciona con:

- Dos paletas
- Pelota con rebote
- Marcador
- Ventana 800x600
- Código separado en varios archivos

Ahora necesito agregar una mejora visible para mi proyecto académico.

Requisitos:

1. Agregar una pantalla de inicio.
2. Agregar estados del juego:
   - START
   - PLAYING
   - GAME_OVER
3. El juego debe iniciar al presionar ESPACIO.
4. Mostrar pantalla de ganador.
5. Agregar reinicio con la tecla R.
6. Permitir salir con ESC.
7. Mantener la arquitectura actual.
8. Explicar los cambios realizados.
```

**Resultado**

La IA agregó:
- Pantalla de inicio.
- Pantalla de Game Over.
- Estados del juego (START, PLAYING, GAME_OVER).
- Reinicio de partida con la tecla R.
- Salida con ESC.
- Mejor organización de la lógica del juego.

**Por qué se ajustó/refinó el prompt**

Después de tener la base funcional (Prompt 1) y corregir el error (Prompt 2),
se buscó mejorar la experiencia de usuario añadiendo estados claros al juego,
demostrando iteración real sobre el comportamiento del programa.

---

## Prompt 4 — Mejora Visual (Extra)

**Qué se pidió a la IA**

```text
Quiero mejorar la parte visual de mi juego Pong en Python con Pygame sin romper la funcionalidad actual.

Necesito:

- Fondo moderno.
- Colores diferentes para cada jugador.
- Mejor diseño del marcador.
- Mejor pantalla de inicio.
- Mejor pantalla de Game Over.
- Mantener la arquitectura actual.
```

**Resultado**

La IA agregó:
- Fondo azul oscuro.
- Título principal mejorado.
- Diferenciación visual de jugadores.
- Mejor presentación de controles.
- Pantallas más profesionales.

**Por qué se ajustó/refinó el prompt**

Se usó como mejora adicional (no obligatoria) para pulir la apariencia del
proyecto y hacerlo más atractivo, sin afectar la lógica ya validada.

---

## Validación del resultado

**Cómo se probó el código**

El juego se ejecutó con `python main.py` después de cada prompt aplicado,
verificando manualmente:
- Que la ventana se abre correctamente (800x600).
- Que ambas paletas responden a los controles del teclado.
- Que la pelota rebota correctamente en los bordes y paletas.
- Que el marcador aumenta correctamente al anotar un punto.
- Que los estados START → PLAYING → GAME_OVER funcionan según lo esperado.
- Que las teclas ESPACIO, R y ESC responden correctamente en cada estado.

**Error o limitación identificada**

Durante las pruebas se encontró el error `NameError: name 'PADDLE_HEIGHT'
is not defined` (ver Prompt 2), causado porque las constantes definidas en
`settings.py` no estaban siendo importadas en `game.py`. Se corrigió
agregando la importación correspondiente (`from settings import *` o las
constantes específicas necesarias).

---

## Reflexión final

**Qué aprendí usando IA para programar**

Aprendí que la IA es muy útil para acelerar la creación de una base de
código organizada, pero que sigue siendo necesario revisar, ejecutar y
entender cada parte del código generado para detectar errores y verificar
que cumple con lo que realmente se necesita.

**Ventajas y límites del vibecoding**

- *Ventajas:* permite avanzar rápido en la estructura inicial, facilita
  corregir errores explicando el contexto exacto del problema, y ayuda a
  iterar mejoras (funcionales y visuales) sin tener que escribir todo el
  código desde cero.
- *Límites:* la IA puede generar código que "funciona" pero que no siempre
  sigue exactamente las mejores prácticas si no se le pide explícitamente;
  además, requiere que el desarrollador entienda el código para poder
  pedir correcciones precisas (como en el Prompt 2) y para detectar
  errores que la IA no menciona por sí sola.

**Qué partes del código comprendo y cuáles necesito reforzar**

- *Comprendo bien:* la lógica de movimiento de las paletas, el rebote de
  la pelota, el manejo del marcador y la máquina de estados del juego
  (START, PLAYING, GAME_OVER).
- *Necesito reforzar:* el manejo más avanzado de Pygame (como animaciones,
  efectos de sonido y optimización del bucle principal), así como buenas
  prácticas de empaquetado de proyectos Python (uso de `pyproject.toml`,
  estructura `src layout`, pruebas con `pytest`).