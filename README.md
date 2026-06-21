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

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrese de tener instalado:

* Python 3.12.x
* pip
* Git (opcional)

> **Importante:** El proyecto fue probado utilizando Python 3.12 y Pygame 2.6.1. Versiones más recientes de Python pueden presentar problemas de compatibilidad con algunas dependencias.

---

## Estructura del Proyecto

```text
python-pong-game/
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
├── docs/
│   └── prompts.md
│
└── assets/
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Paizstan/python-pong-game.git
cd python-pong-game
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Verificar la versión de Python

```bash
python --version
```

Resultado esperado:

```text
Python 3.12.x
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

### Errores Encontrados

#### Error 1

```text
NameError: PADDLE_HEIGHT is not defined
```

**Causa:**

La constante utilizada en `game.py` no estaba siendo importada correctamente desde `settings.py`.

**Solución:**

Se corrigió la importación correspondiente y el juego volvió a funcionar correctamente.

#### Error 2

```text
ModuleNotFoundError: No module named 'pygame'
```

**Causa:**

La librería Pygame no estaba instalada en el entorno de ejecución utilizado para correr el proyecto.

**Solución:**

Se instalaron las dependencias definidas en `requirements.txt` y se verificó la compatibilidad de la versión de Python utilizada.

---

## Uso de Inteligencia Artificial

Durante el desarrollo se utilizó ChatGPT como asistente de programación para:

* Generar la estructura inicial del proyecto.
* Organizar el código en múltiples archivos.
* Corregir errores encontrados durante la ejecución.
* Mejorar la experiencia del usuario.
* Implementar nuevas funcionalidades.
* Explicar conceptos y validar decisiones de implementación.

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
* Importancia de validar dependencias y entornos de ejecución.

Como mejora futura, me gustaría implementar:

* Modo de un jugador contra IA.
* Efectos de sonido.
* Incremento progresivo de dificultad.
* Mejoras visuales y animaciones.

---

## Autor

**Stanley Paiz**

Proyecto desarrollado para la actividad:

**"Vibecoding Guiado: Desarrollo de una Aplicación o Mini-Juego con IA como Copiloto"**
