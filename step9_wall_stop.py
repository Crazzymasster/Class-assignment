"""
STEP 9: Wall Collision - Stop Instead of Game Over
===================================================

ALGORITHM THINKING:
- Question: Instead of dying when hitting a wall, what if the snake just stops?
- Idea: When movement would go out of bounds, prevent that movement but keep playing
- Rules: Snake can't move into walls, but continues living; player chooses new direction

TARGET: Snake stops at boundaries instead of ending the game
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
CYAN = (0, 255, 255)

BASE_FPS = 10

# ============ SETUP ============
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Step 9: Wall Stop")
clock = pygame.time.Clock()

# ============ HELPER FUNCTIONS ============
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
            elif event.key == pygame.K_r and game_over:
                snake = [[20, 15], [19, 15], [18, 15]]
                direction = [1, 0]
                next_direction = [1, 0]
                food = spawn_food()
                score = 0
                game_over = False

    # ===== UPDATE PHASE =====
    if not game_over:
        # Calculate new position
        test_head_x = snake[0][0] + next_direction[0]
        test_head_y = snake[0][1] + next_direction[1]
        
        max_x = WINDOW_WIDTH // GRID_SIZE
        max_y = WINDOW_HEIGHT // GRID_SIZE
        
        # NEW: Check if movement would hit a wall
        # If so, DON'T change direction (keep moving in current direction)
        # Otherwise, accept the new direction
        if 0 <= test_head_x < max_x and 0 <= test_head_y < max_y:
            direction = next_direction
        # else: Direction change rejected, snake continues in current direction
        
        # Move snake
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        
        # Check if new position is out of bounds
        # If it is, DON'T move (keep head in same spot)
        if head_x < 0 or head_x >= max_x or head_y < 0 or head_y >= max_y:
            # Snake stays still (don't add new segment)
            pass
        else:
            # Normal movement
            snake.insert(0, [head_x, head_y])
            
            # Check food collision
            if snake[0] == food:
                score += 1
                food = spawn_food()
            else:
                snake.pop()
            
            # Check self collision
            for i in range(1, len(snake)):
                if snake[0] == snake[i]:
                    game_over = True
                    break

    # ===== DRAW PHASE =====
    screen.fill(BLACK)

    # Draw grid
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, WINDOW_HEIGHT), 1)
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (30, 30, 30), (0, y), (WINDOW_WIDTH, y), 1)

    # Draw snake
    for i, segment in enumerate(snake):
        x = segment[0] * GRID_SIZE
        y = segment[1] * GRID_SIZE
        
        if i == 0:
            color = CYAN
        else:
            color = GREEN
        
        pygame.draw.rect(screen, color, (x, y, GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, WHITE, (x, y, GRID_SIZE, GRID_SIZE), 2)

    # Draw food
    fx = food[0] * GRID_SIZE
    fy = food[1] * GRID_SIZE
    pygame.draw.circle(screen, RED, (fx + GRID_SIZE//2, fy + GRID_SIZE//2), GRID_SIZE//2 - 2)
    pygame.draw.circle(screen, YELLOW, (fx + GRID_SIZE//2, fy + GRID_SIZE//2), GRID_SIZE//2 - 4)

    # Draw UI
    font = pygame.font.Font(None, 24)
    score_text = font.render(f"Score: {score}", True, YELLOW)
    length_text = font.render(f"Length: {len(snake)}", True, YELLOW)

    screen.blit(score_text, (10, 10))
    screen.blit(length_text, (10, 40))

    # Draw game over screen
    if game_over:
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        large_font = pygame.font.Font(None, 80)
        small_font = pygame.font.Font(None, 36)
        
        game_over_text = large_font.render("GAME OVER", True, RED)
        final_score_text = small_font.render(f"Final Score: {score}", True, YELLOW)
        restart_text = small_font.render("Press R to Restart", True, WHITE)
        
        screen.blit(game_over_text, (WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2 - 120))
        screen.blit(final_score_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2))
        screen.blit(restart_text, (WINDOW_WIDTH//2 - 200, WINDOW_HEIGHT//2 + 80))

    pygame.display.flip()
    clock.tick(BASE_FPS)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. What are the TWO wall collision checks? Why do we need both?
# 2. When the snake "stays still", what part of the code makes that happen?
# 3. How is this different from the previous version? What's better about it?
