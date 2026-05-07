"""
STEP 3: Move the Snake
======================

ALGORITHM THINKING:
- Question: How does the snake move?
- Rules: Head moves in a direction, body follows
- Steps: Move head → body catches up (by removing tail)

TARGET: Snake continuously moves to the right, wraps around screen
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

FPS = 10

# ============ SETUP ============
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Step 3")
clock = pygame.time.Clock()

# ============ SNAKE DATA ============
snake = [
    [20, 15],
    [19, 15],
    [18, 15],
]

# Direction: [dx, dy] how much to move each frame
direction = [1, 0]  # Moving right (+1 on x-axis)

# ============ GAME LOOP ============
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # ===== UPDATE PHASE =====
    # 1. Calculate new head position
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    
    # 2. Wrap around screen (if head goes off right, appear on left)
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    
    head_x = head_x % max_x
    head_y = head_y % max_y
    
    # 3. Add new head to front of snake
    snake.insert(0, [head_x, head_y])
    
    # 4. Remove tail (so snake stays same length)
    snake.pop()
    
    # ===== DRAW PHASE =====
    screen.fill(BLACK)
    
    for i, segment in enumerate(snake):
        x = segment[0] * GRID_SIZE
        y = segment[1] * GRID_SIZE
        
        if i == 0:
            color = GREEN
        else:
            color = (0, 150, 0)
        
        pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. What does direction = [1, 0] mean? What would [0, 1] do?
# 2. What's the purpose of insert(0, ...) and pop()?
# 3. Try changing direction to [-1, 0]. What happens?
# 4. What does % (modulo) do? Why do we use it for wrap-around?
# 5. The snake moves at FPS speed. Try changing FPS - what happens?
