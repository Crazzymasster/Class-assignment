"""
STEP 6: Food & Collision Detection
===================================

ALGORITHM THINKING:
- Question: How do I spawn food randomly and detect when snake eats it?
- Rules: Food appears at random grid position, snake grows when head touches it
- Steps: Spawn food at start → each frame check if head == food position
         If yes: grow snake and spawn new food

TARGET: Food appears randomly, snake grows when eating it
"""

import pygame
import random

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
pygame.display.set_caption("Snake Game - Step 6")
clock = pygame.time.Clock()

# ============ HELPER FUNCTION ============
def spawn_food():
    """Create food at random grid position"""
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    return [random.randint(0, max_x - 1), random.randint(0, max_y - 1)]

# ============ SNAKE DATA ============
snake = [
    [20, 15],
    [19, 15],
    [18, 15],
]

direction = [1, 0]
next_direction = [1, 0]
food = spawn_food()
score = 0

# ============ GAME LOOP ============
running = True
while running:
    # ===== INPUT PHASE =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
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
    direction = next_direction
    
    head_x = snake[0][0] + direction[0]
    head_y = snake[0][1] + direction[1]
    
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    
    head_x = head_x % max_x
    head_y = head_y % max_y
    
    snake.insert(0, [head_x, head_y])
    
    # ===== COLLISION DETECTION =====
    # Check if head collides with food
    if snake[0] == food:
        score += 1
        # Don't remove tail (grow)
        food = spawn_food()  # Spawn new food
    else:
        snake.pop()  # Remove tail normally
    
    # ===== DRAW PHASE =====
    screen.fill(BLACK)
    
    # Draw snake
    for i, segment in enumerate(snake):
        x = segment[0] * GRID_SIZE
        y = segment[1] * GRID_SIZE
        
        if i == 0:
            color = GREEN
        else:
            color = (0, 150, 0)
        
        pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 1)
    
    # Draw food
    fx = food[0] * GRID_SIZE
    fy = food[1] * GRID_SIZE
    pygame.draw.rect(screen, RED, (fx, fy, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, YELLOW, (fx, fy, GRID_SIZE, GRID_SIZE), 2)
    
    # Draw UI
    font = pygame.font.Font(None, 24)
    text_score = font.render(f"Score: {score}", True, YELLOW)
    text_length = font.render(f"Length: {len(snake)}", True, YELLOW)
    screen.blit(text_score, (10, 10))
    screen.blit(text_length, (10, 40))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. How does spawn_food() work? What does random.randint do?
# 2. Why do we check snake[0] == food? What are we comparing?
# 3. What happens if food spawns ON the snake body? (Does it matter?)
# 4. How would you prevent food from spawning on the snake?
# 5. Try making food purple and bigger. Find where to change this.
