"""
STEP 1: Pygame Setup & Drawing
================================

ALGORITHM THINKING:
- Question: How do I display a window?
- Rules: Set a fixed screen size, pick colors
- Steps: Initialize pygame → create window → draw background → update display

TARGET: A window that displays, with a small square (our starting snake)
"""

import pygame

# Initialize pygame
pygame.init()

# ============ CONFIGURATION ============
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20  # Each cell is 20x20 pixels

# Colors (as RGB tuples: Red, Green, Blue)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 10  # Updates per second

# ============ SETUP ============
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# ============ GAME LOOP ============
running = True
while running:
    # Handle events (like closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ===== DRAW PHASE =====
    screen.fill(BLACK)  # Clear screen with black
    
    # Draw a square at position (100, 100) - this will be our snake head
    pygame.draw.rect(screen, GREEN, (100, 100, GRID_SIZE, GRID_SIZE))
    
    # Update display
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. What does GRID_SIZE do? What happens if you change it?
# 2. What are the RGB values for (255, 0, 0)? Try different numbers!
# 3. How would you draw 3 squares in a row?
# 4. What does clock.tick(FPS) do? What happens if you change FPS?
