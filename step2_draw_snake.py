"""
STEP 2: Draw the Snake Body
============================

ALGORITHM THINKING:
- Question: How do I draw the snake as separate segments?
- Rules: Snake is a list of positions, each position is a grid cell
- Steps: Create a list → loop through it → draw each segment

TARGET: A snake made of 3 segments displayed on screen
"""

import pygame

pygame.init()

# ============ CONFIGURATION ============
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 10

# ============ SETUP ============
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Step 2")
clock = pygame.time.Clock()

# ============ SNAKE DATA ============
# Each position is [x, y] in GRID coordinates (not pixels!)
# x goes from 0 to WINDOW_WIDTH/GRID_SIZE
# y goes from 0 to WINDOW_HEIGHT/GRID_SIZE

snake = [
    [20, 15],  # Head (position on grid)
    [19, 15],  # Body segment 1
    [18, 15],  # Body segment 2
]

# ============ GAME LOOP ============
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ===== DRAW PHASE =====
    screen.fill(BLACK)
    
    # Draw each segment of the snake
    for i, segment in enumerate(snake):
        x = segment[0] * GRID_SIZE
        y = segment[1] * GRID_SIZE
        
        # Head is brighter green, body is darker
        if i == 0:
            color = GREEN
        else:
            color = (0, 200, 0)
        
        pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
        # Draw border to see segments clearly
        pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. Why do we multiply by GRID_SIZE? (What's the difference between grid coords and pixel coords?)
# 2. Add a 4th segment to the snake. Where would it go?
# 3. What does enumerate() do? Why is it useful here?
# 4. How many segments can you add before they go off screen?
