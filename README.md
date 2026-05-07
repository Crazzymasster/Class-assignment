# Python Pygame Assignment: Snake Game

## 🐍 Project Overview

In this assignment, you will learn **algorithm development** by building the classic Snake game step-by-step. Each step introduces new ideas and challenges that require you to think about:

- **What problem am I solving?**
- **What are the rules (constraints)?**
- **What steps do I need to take?**
- **How do I test if it works?**

## 📋 Learning Goals

- Understand the game loop (update → draw → repeat)
- Break complex problems into smaller pieces
- Practice logical thinking (if/else conditions)
- Learn about **grid-based movement** (not pixel-by-pixel)
- Understand **queue data structure** (body following head)
- Learn collision detection

## 📅 4-Class Structure

| Class | Steps | Focus | Goal |
|-------|-------|-------|------|
| **1** | 1-3 | Setup & Movement | Snake moves on grid, responds to input |
| **2** | 4-5 | Queue Logic | Snake body grows properly when food eaten |
| **3** | 6-7 | Game Mechanics | Food, scoring, and game over |
| **4** | 8+ | Polish & Bugs | Test, fix, add enhancements |

---

## The Game Concept

**Snake**

- Snake moves on a **grid** (like a checkerboard)
- You control the direction (arrow keys)
- Food spawns randomly
- When snake eats food: **score +1** and **body grows**
- Game ends if snake hits wall or itself
- Goal: Eat as much food as possible!

---

## 🚀 How to Use This Assignment

1. Read through each step file completely
2. **Run it** and see what happens
3. **Modify the code** - try changing colors, speed, or grid size
4. **Answer the reflection questions** at the bottom
5. Discuss with your teacher before moving to the next step

---

## 🔧 Requirements

```
Python 3.x
pygame (install with: pip install pygame)
```

To install pygame:
```
pip install pygame
```

---

## 💡 Key Algorithmic Concepts

- **Grid Logic**: Movement in discrete cells, not smooth pixels
- **Queue/Deque**: Snake body follows the head (first-in, first-out)
- **Collision Detection**: Checking if snake hits wall or itself
- **Game State**: Tracking if game is running or over

---

**Start with step1_setup.py!**