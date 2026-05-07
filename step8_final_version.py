"""
STEP 8: Final Polish & Enhancements
====================================

ALGORITHM THINKING - FINAL VERSION:
- Question: How do we make the game more interesting?
- Ideas: Speed increases with score, better visuals, sound (optional)
- Rules: Every X points, speed increases slightly

TARGET: Fully playable Snake game with scaling difficulty
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
MAX_FPS = 25

# ============ SETUP ============
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game - Final Version")
clock = pygame.time.Clock()

# ============ HELPER FUNCTIONS ============
def spawn_food():
    """Create food at random grid position"""
    max_x = WINDOW_WIDTH // GRID_SIZE
    max_y = WINDOW_HEIGHT // GRID_SIZE
    return [random.randint(0, max_x - 1), random.randint(0, max_y - 1)]

def calculate_fps(score):
    """Speed increases with score"""
    # Every 5 points, increase speed by 1 FPS (up to MAX_FPS)
    fps = BASE_FPS + (score // 5)
    return min(fps, MAX_FPS)

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
high_score = 0

# ============ GAME LOOP ============
running = True
while running:
    # ===== INPUT PHASE =====
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != [0, 1]:
                next_direction = [0, -1]
            elif event.key == pygame.K_DOWN and direction != [0, -1]:
                next_direction = [0, 1]
            elif event.key == pygame.K_LEFT and direction != [1, 0]:
                next_direction = [-1, 0]
            elif event.key == pygame.K_RIGHT and direction != [-1, 0]:
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
                if score > high_score:
                    high_score = score
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
    
    # Draw grid (optional, for visual reference)
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, WINDOW_HEIGHT), 1)
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, (30, 30, 30), (0, y), (WINDOW_WIDTH, y), 1)
    
    # Draw snake
    for i, segment in enumerate(snake):
        x = segment[0] * GRID_SIZE
        y = segment[1] * GRID_SIZE
        
        if i == 0:
            color = CYAN  # Head is cyan
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
    high_score_text = font.render(f"High Score: {high_score}", True, CYAN)
    speed_text = font.render(f"Speed: {calculate_fps(score)} FPS", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(length_text, (10, 40))
    screen.blit(high_score_text, (10, 70))
    screen.blit(speed_text, (10, 100))
    
    # Draw game over screen
    if game_over:
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        large_font = pygame.font.Font(None, 80)
        small_font = pygame.font.Font(None, 36)
        
        game_over_text = large_font.render("GAME OVER", True, RED)
        final_score_text = small_font.render(f"Final Score: {score}", True, YELLOW)
        restart_text = small_font.render("Press R to Restart or Q to Quit", True, WHITE)
        
        screen.blit(game_over_text, (WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2 - 120))
        screen.blit(final_score_text, (WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2))
        screen.blit(restart_text, (WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT//2 + 80))
        
        # Check for quit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
    
    pygame.display.flip()
    
    # Dynamic FPS based on score
    current_fps = calculate_fps(score)
    clock.tick(current_fps)

pygame.quit()

# ============ REFLECTION QUESTIONS ============
# 1. What does calculate_fps() do? How does it make the game harder?
# 2. What's the purpose of high_score? How is it useful?
# 3. We prevent 180-degree turns (can't reverse into self immediately).
#    Why is this important?
# 4. Try these enhancements:
#    - Add a \"level\" system that increases every 10 points
#    - Make food worth different points (regular=1, special=5)
#    - Add obstacles that snake can't pass through
# 5. What's the highest score you can get?
