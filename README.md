# Pong Python Vibecoding

## Descripción

Pong Python Vibecoding es una implementación del clásico juego Pong desarrollada en Python utilizando la librería Pygame.

Este proyecto fue creado aplicando técnicas de Vibecoding, utilizando Inteligencia Artificial como asistente de programación para generar código, corregir errores, mejorar funcionalidades y validar resultados.

---

## Objetivo del Proyecto

Desarrollar un mini-juego funcional utilizando Python y Pygame, demostrando:

* Uso de IA como copiloto de programación.
* Aplicación de Prompt Engineering.
* Iteración y refinamiento de instrucciones.
* Validación y corrección de errores.
* Comprensión del código generado.
* Uso de Git y GitHub para control de versiones.

---

## Tecnologías Utilizadas

* Python 3.12
* Pygame 2.6.1
* Git
* GitHub
* Visual Studio Code

---

## Estructura del Proyecto

```text
pong-python-vibecoding/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── game.py
│   ├── paddle.py
│   ├── ball.py
│   ├── settings.py
│   └── __init__.py
│
└── docs/
    └── prompts.md
```

---

## Instalación

Instalar las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Ejecutar el juego:

```bash
python main.py
```

---

## Controles

### Jugador 1

* W → Mover arriba
* S → Mover abajo

### Jugador 2

* Flecha Arriba → Mover arriba
* Flecha Abajo → Mover abajo

### Controles Generales

* ESPACIO → Iniciar partida
* R → Reiniciar partida
* ESC → Salir del juego

---

## Funcionalidades Implementadas

* Pantalla de inicio.
* Juego Pong para dos jugadores.
* Marcador en tiempo real.
* Detección de colisiones.
* Rebote de pelota.
* Sistema de puntuación.
* Pantalla de Game Over.
* Reinicio de partida.
* Arquitectura modular basada en clases.
* Configuración centralizada mediante constantes.

---

## Validación del Resultado

Se realizaron pruebas ejecutando el juego mediante:

```bash
python main.py
```

### Pruebas realizadas

* Apertura correcta de la ventana.
* Movimiento de ambas paletas.
* Movimiento de la pelota.
* Rebotes contra paredes y paletas.
* Actualización del marcador.
* Inicio mediante la tecla ESPACIO.
* Reinicio mediante la tecla R.
* Cierre mediante la tecla ESC.
* Pantalla de victoria al alcanzar el puntaje objetivo.

### Error Encontrado

Durante la fase de pruebas apareció el siguiente error:

```text
NameError: PADDLE_HEIGHT is not defined
```

### Solución Aplicada

Se identificó que la constante utilizada en `game.py` no estaba siendo importada correctamente desde `settings.py`.

Se corrigió la importación y el juego volvió a funcionar correctamente.

---

## Uso de Inteligencia Artificial

Durante el desarrollo se utilizó ChatGPT como asistente de programación para:

* Generar la estructura inicial del proyecto.
* Organizar el código en múltiples archivos.
* Corregir errores encontrados durante la ejecución.
* Mejorar la experiencia del usuario.
* Implementar nuevas funcionalidades.

La evidencia completa de los prompts utilizados se encuentra en:

```text
docs/prompts.md
```

---

## Reflexión Final

Este proyecto permitió comprender cómo la Inteligencia Artificial puede utilizarse como una herramienta de apoyo durante el desarrollo de software.

Una de las principales ventajas del Vibecoding fue la rapidez para generar código funcional y obtener ayuda durante la depuración de errores. También permitió experimentar con mejoras progresivas mediante la iteración de prompts.

Sin embargo, se identificó que no es recomendable utilizar el código generado sin comprenderlo previamente, ya que pueden existir errores o detalles que requieren revisión manual.

Durante el proyecto logré comprender:

* Estructura básica de un videojuego en Pygame.
* Manejo de eventos del teclado.
* Uso de clases y programación orientada a objetos.
* Detección de colisiones.
* Organización modular de proyectos Python.

Como mejora futura, me gustaría implementar:

* Modo de un jugador contra IA.
* Efectos de sonido.
* Incremento progresivo de dificultad.
* Mejoras visuales y animaciones.

---

## Autor

Stanley Paiz

Proyecto desarrollado para la actividad:

**"Vibecoding Guiado: Desarrollo de una Aplicación o Mini-Juego con IA como Copiloto"**
