"""
STEP 5: The Queue Algorithm - Growing the Snake
================================================

ALGORITHM THINKING - CRITICAL CONCEPT!
- Question: How does the snake grow when it eats food?
- Rules: Normally we remove tail after adding head (stays same length)
         But if food eaten, we DON'T remove tail (grows by 1)
- Steps: Add head → Check if food eaten → If yes, keep tail; if no, remove tail

TARGET: Snake grows in size as it eats (simulated with space key for now)
CRITICAL: This teaches the QUEUE data structure concept!
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
pygame.display.set_caption("Snake Game - Step 5")
clock = pygame.time.Clock()

# ============ SNAKE DATA ============
snake = [
    [20, 15],
    [19, 15],
    [18, 15],
]

direction = [1, 0]
next_direction = [1, 0]
ate_food = False  # Flag to track if snake just ate

# ============ GAME LOOP ============
running = True
while running:
    # ===== INPUT PHASE =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Arrow keys to move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                next_direction = [0, -1]
            elif event.key == pygame.K_DOWN:
                next_direction = [0, 1]
            elif event.key == pygame.K_LEFT:
                next_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT:
                next_direction = [1, 0]
            # SPACE to simulate eating food
            elif event.key == pygame.K_SPACE:
                ate_food = True
    
    # ===== UPDATE PHASE =====
    direction = next_direction
    
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    
    head_x = head_x % max_x
    head_y = head_y % max_y
    
    # Add new head
    snake.insert(0, [head_x, head_y])
    
    # THIS IS THE KEY ALGORITHM:
    # If we ate food, DON'T remove tail (body grows)
    # If we didn't eat food, remove tail (body stays same length)
    if ate_food:
        ate_food = False  # Reset the flag
        # Don't pop! This is how growth happens!
    else:
        snake.pop()  # Remove tail normally
    
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
    
    # Draw instructions and snake length
    font = pygame.font.Font(None, 24)
    text1 = font.render("Use arrows to move, SPACE to grow", True, WHITE)
    text2 = font.render(f"Length: {len(snake)}", True, YELLOW)
    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. WHY does not removing the tail make the snake grow? Draw a picture!
# 2. What's the difference between if ate_food vs else pop()?
# 3. Think about a real queue (line at store):
#    - Normal movement: person at front leaves, person at back stays
#    - Growth: person at front leaves, person at BACK JOINS (doesn't leave)
#    How is this like our snake?
# 4. Press space multiple times. The length keeps growing. Modify code so
#    you can only grow by 1 segment per food (limit growth rate)
