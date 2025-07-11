# 🚀 Asteroids (Pygame Edition)

A modern remake of the classic **Asteroids** arcade game, built using **Python** and **Pygame**.

---

## 🧩 Summary

Fly a spaceship through space, dodge asteroids, and blast them into pieces! This game is a simple and fun programming project to learn 2D game development, OOP principles, and collision mechanics using Python.

---

## ✨ Features

- 🚀 **Player-controlled spaceship**  
  Rotate, move, and shoot using keyboard controls

- 🪨 **Dynamic asteroid field**  
  Asteroids spawn from screen edges and move in randomized directions

- 💥 **Bullet shooting**  
  Fire projectiles in the direction you're facing (with cooldown)

- 🔁 **Asteroid splitting**  
  Large asteroids split into smaller ones when hit

- ❌ **Collision detection**  
  - Ship collision with an asteroid ends the game  
  - Bullet collision with asteroids destroys or splits them

- 🌀 **Group-based object management**  
  Clean and scalable game loop using sprite groups

---

## 🎮 Controls

| Key         | Action                     |
|-------------|-----------------------------|
| `A`         | Rotate left                 |
| `D`         | Rotate right                |
| `W`         | Move forward                |
| `S`         | Move backward               |
| `SPACE`     | Shoot bullet (rate-limited) |
| `ESC` or ❌ | Close game window           |

---

## 📜 Game Rules

- You start at the center of the screen in a triangular spaceship.
- Asteroids spawn randomly from the screen edges.
- Shoot asteroids to destroy them:
  - Large → 2 Medium  
  - Medium → 2 Small  
  - Small → Gone
- If your ship collides with any asteroid: **Game Over**.
- Survive as long as you can!

---

## ▶️ How to Run

1. **Install dependencies** (if not already):
   ```bash
   pip install pygame
   ```

2. **Run the game**:
   ```bash
   uv run main.py
   ```

---

## 🧱 Project Structure

```
.
├── main.py              # Game loop
├── constants.py         # Game settings and constants
├── player.py            # Player spaceship logic
├── circleshape.py       # Base class for all circular objects
├── asteroid.py          # Asteroid behavior & splitting logic
├── asteroidfield.py     # Asteroid spawn logic
├── README.md            # Project description
```

---