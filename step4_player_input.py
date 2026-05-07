"""
STEP 4: Player Control - Change Direction
===========================================

ALGORITHM THINKING:
- Question: How does the player control the snake?
- Rules: Arrow keys change direction, can't reverse into itself
- Steps: Listen for key press → change direction variable

TARGET: Use arrow keys to move snake up/down/left/right
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
YELLOW = (255, 255, 0)

FPS = 10

# ============ SETUP ============
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Step 4")
clock = pygame.time.Clock()

# ============ SNAKE DATA ============
snake = [
    [20, 15],
    [19, 15],
    [18, 15],
]

direction = [1, 0]  # Start moving right
next_direction = [1, 0]  # Buffer for next direction

# ============ GAME LOOP ============
running = True
while running:
    # ===== INPUT PHASE =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Check for arrow key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                next_direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                next_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                next_direction = [1, 0]
    
    # ===== UPDATE PHASE =====
    # Use next_direction (prevents turning 180 degrees into yourself)
    direction = next_direction
    
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    
    head_x = head_x % max_x
    head_y = head_y % max_y
    
    snake.insert(0, [head_x, head_y])
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
    
    # Draw instructions
    font = pygame.font.Font(None, 24)
    text = font.render("Use arrow keys to move", True, WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. Why do we need both direction and next_direction?
# 2. Try removing the next_direction logic. What breaks?
# 3. What happens if you press multiple keys at once?
# 4. Add a key to pause the game. HINT: Add another variable to track if paused
