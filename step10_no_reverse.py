"""
STEP 10: Lock Backwards Movement - Prevent Accidental Death
===========================================================

ALGORITHM THINKING:
- Question: Players accidentally press the opposite direction and die instantly!
- Idea: Don't allow the snake to reverse 180 degrees into itself
- Rules: Can't move directly opposite to current direction
- Examples:
  - If moving RIGHT [1, 0], can't move LEFT [-1, 0]
  - If moving UP [0, -1], can't move DOWN [0, 1]
  - BUT: Can still move UP, DOWN, LEFT, RIGHT to turn!

TARGET: Prevent instant self-collision deaths
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
pygame.display.set_caption("Snake Game - Step 10: No Reverse")
clock = pygame.time.Clock()

# ============ HELPER FUNCTIONS ============
def spawn_food():
    """Create food at random grid position"""
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    return [random.randint(0, max_x - 1), random.randint(0, max_y - 1)]

def is_opposite_direction(current_dir, new_dir):
    """
    Check if new_dir is exactly opposite to current_dir
    
    If we're moving RIGHT [1, 0], opposite is LEFT [-1, 0]
    If we're moving UP [0, -1], opposite is DOWN [0, 1]
    
    To find opposite: multiply each component by -1
    """
    opposite = [-current_dir[0], -current_dir[1]]
    return new_dir == opposite

# ============ SNAKE DATA ============
snake = [
    [20, 15],
    [19, 15],
    [18, 15],
]

direction = [1, 0]  # Moving RIGHT initially
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
            # Capture what key was pressed
            pressed_up = event.key == pygame.K_UP
            pressed_down = event.key == pygame.K_DOWN
            pressed_left = event.key == pygame.K_LEFT
            pressed_right = event.key == pygame.K_RIGHT
            
            # Convert key press to direction vector
            if pressed_up:
                potential_direction = [0, -1]
            elif pressed_down:
                potential_direction = [0, 1]
            elif pressed_left:
                potential_direction = [-1, 0]
            elif pressed_right:
                potential_direction = [1, 0]
            else:
                potential_direction = None
            
            # NEW: Only accept the direction if it's NOT the opposite
            if potential_direction is not None:
                if not is_opposite_direction(direction, potential_direction):
                    next_direction = potential_direction
                # else: Ignore this input (player tried to reverse)
            
            if event.key == pygame.K_r and game_over:
                snake = [[20, 15], [19, 15], [18, 15]]
                direction = [1, 0]
                next_direction = [1, 0]
                food = spawn_food()
                score = 0
                game_over = False

    # ===== UPDATE PHASE =====
    if not game_over:
        direction = next_direction
        
        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]
        
        max_x = WINDOW_WIDTH // GRID_SIZE
        max_y = WINDOW_HEIGHT // GRID_SIZE
        
        # Check wall collision
        if head_x < 0 or head_x >= max_x or head_y < 0 or head_y >= max_y:
            game_over = True
        
        if not game_over:
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
    direction_text = font.render(f"Direction: {direction}", True, CYAN)

    screen.blit(score_text, (10, 10))
    screen.blit(length_text, (10, 40))
    screen.blit(direction_text, (10, 70))

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
# 1. What does is_opposite_direction() do?
# 2. How does [-current_dir[0], -current_dir[1]] calculate the opposite direction?
# 3. Why is this check in the INPUT phase and not the UPDATE phase?
# 4. Test: If the snake is moving RIGHT, what happens if you press LEFT?
# 5. What CAN you press if the snake is moving RIGHT?
