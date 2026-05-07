"""
STEP 7: Game Over Conditions
=============================

ALGORITHM THINKING:
- Question: When does the game end?
- Rules: Game ends if snake hits wall OR hits itself
- Steps: After moving, check if head hits wall or body
         If yes: stop game, show game over screen

TARGET: Game ends when snake crashes, display final score
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
pygame.display.set_caption("Snake Game - Step 7")
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
game_over = False

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
            # R to restart
            elif event.key == pygame.K_r and game_over:
                snake = [[20, 15], [19, 15], [18, 15]]
                direction = [1, 0]
                next_direction = [1, 0]
                food = spawn_food()
                score = 0
                game_over = False
    
    # ===== UPDATE PHASE (only if not game over) =====
    if not game_over:
        direction = next_direction
        
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        
        max_x = WINDOW_WIDTH // GRID_SIZE
        max_y = WINDOW_HEIGHT // GRID_SIZE
        
        # ===== COLLISION WITH WALL =====
        # Instead of wrapping, check if out of bounds
        if head_x < 0 or head_x >= max_x or head_y < 0 or head_y >= max_y:
            game_over = True
        
        # If we can move, add new head
        if not game_over:
            snake.insert(0, [head_x, head_y])
            
            # ===== COLLISION WITH FOOD =====
            if snake[0] == food:
                score += 1
                food = spawn_food()
            else:
                snake.pop()
            
            # ===== COLLISION WITH SELF =====
            # Check if head collides with any body segment (skip index 0, that's the head)
            for i in range(1, len(snake)):
                if snake[0] == snake[i]:
                    game_over = True
                    break
    
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
    
    # Draw game over screen
    if game_over:
        large_font = pygame.font.Font(None, 60)
        small_font = pygame.font.Font(None, 36)
        
        game_over_text = large_font.render("GAME OVER", True, RED)
        final_score_text = small_font.render(f"Final Score: {score}", True, YELLOW)
        restart_text = small_font.render("Press R to Restart", True, WHITE)
        
        screen.blit(game_over_text, (WINDOW_WIDTH//2 - 200, WINDOW_HEIGHT//2 - 100))
        screen.blit(final_score_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2))
        screen.blit(restart_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2 + 60))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. What changed from Step 6? List all the new collision checks.
# 2. Why do we check range(1, len(snake))? Why not start at 0?
# 3. What's the difference between hitting a wall and hitting yourself?
# 4. How would you add \"lives\" so the player gets 3 chances?
# 5. Test the game! Can you beat your high score?
