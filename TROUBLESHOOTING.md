# 🔧 Troubleshooting Guide

## Common Problems & Solutions

---

## ❌ Problem: ImportError: No module named 'pygame'

**Error Message:**
```
ImportError: No module named 'pygame'
ModuleNotFoundError: No module named 'pygame'
```

**Solution:**
1. Open terminal/command prompt
2. Type: `pip install pygame`
3. Wait for installation
4. Try running the program again

**If it still doesn't work:**
- Try: `pip3 install pygame`
- Or: `python -m pip install pygame`

---

## ❌ Problem: Window doesn't appear or immediately closes

**What's happening:** The program ran but the window closed too quickly

**Check:**
1. Is there an error message? (Read it carefully!)
2. Did you close the window? (Press the X button)
3. Is the program stuck waiting for input?

**Solution:**
- Make sure you have `pygame.quit()` at the very end
- Make sure the `while running:` loop is indented properly

---

## ❌ Problem: Snake doesn't move

**Check these things:**

1. **Did you run Step 3 or later?** (Steps 1-2 don't have movement)
   - Step 1: No movement
   - Step 2: No movement  
   - Step 3+: Should move

2. **Is the FPS value reasonable?**
   ```python
   FPS = 10  # Okay (moves 10 times per second)
   FPS = 1   # TOO SLOW (moves once per second)
   FPS = 0   # ERROR (can't move)
   ```

3. **Check your direction variable:**
   ```python
   direction = [1, 0]   # Okay (moves right)
   direction = [0, 0]   # BROKEN (no movement!)
   ```

**Fix:**
- Slow FPS? Increase it: `FPS = 15` or `FPS = 20`
- Wrong direction? Change to `[1, 0]` for right

---

## ❌ Problem: Arrow keys don't work

**Check these things:**

1. **Are you running Step 4 or later?** (Steps 1-3 don't respond to keys)

2. **Are your arrow keys getting recognized?**
   Add this to debug:
   ```python
   if event.type == pygame.KEYDOWN:
       print(f"Key pressed: {event.key}")  # See what key was pressed
   ```

3. **Check the key names:**
   ```python
   pygame.K_UP      # ✓ Correct
   pygame.K_DOWN    # ✓ Correct
   pygame.K_LEFT    # ✓ Correct
   pygame.K_RIGHT   # ✓ Correct
   
   pygame.K_W       # Wrong for arrow keys
   pygame.K_SPACE   # Different key
   ```

**Fix:**
- Use `pygame.K_UP`, `pygame.K_DOWN`, `pygame.K_LEFT`, `pygame.K_RIGHT`

---

## ❌ Problem: Snake doesn't grow when eating food

**Check these things:**

1. **Are you running Step 5 or later?**
   - Steps 1-4: No food
   - Step 5+: Should grow

2. **Is the collision detection working?**
   Add this to debug:
   ```python
   print(f"Snake head: {snake[0]}")
   print(f"Food: {food}")
   print(f"Are they equal? {snake[0] == food}")
   ```

3. **Check the growth logic:**
   ```python
   if ate_food:
       # Don't remove tail
   else:
       snake.pop()  # This should happen if NOT eating
   ```

4. **Is `ate_food` being set to True somewhere?**
   In Step 5:
   ```python
   elif event.key == pygame.K_SPACE:
       ate_food = True  # This line exists?
   ```

**Fix:**
- Make sure Step 5 code has `if ate_food:` not `if not ate_food:`
- Double-check that `ate_food = True` is being set
- Print the values to see what's happening

---

## ❌ Problem: Python says "IndentationError"

**Error Message:**
```
IndentationError: expected an indented block
```

**What it means:** You have a line that should be indented (inside a block) but it's not

**Example of WRONG:**
```python
if ate_food:
food = spawn_food()  # ← This should be indented!
```

**Example of CORRECT:**
```python
if ate_food:
    food = spawn_food()  # ← This is indented (4 spaces)
```

**Fix:**
- Find the line with the error
- Add spaces before it (usually 4 spaces)
- Make sure all code inside an `if`/`for`/`while` is indented

---

## ❌ Problem: Game over happens immediately

**What's happening:** Snake dies without reason

**Check:**

1. **Is wrap-around still active?**
   In Step 3-5, snake wraps around screen
   ```python
   head_x = head_x % max_x  # Wrapping
   ```
   
   In Step 7, this is removed and walls kill you instead
   ```python
   if head_x < 0 or head_x >= max_x:  # Check boundaries
       game_over = True
   ```

2. **Is the boundary check wrong?**
   ```python
   max_x = WINDOW_WIDTH // GRID_SIZE    # Correct
   max_x = WINDOW_WIDTH / GRID_SIZE     # Wrong (division, not //)
   ```

**Fix:**
- Use `//` (floor division), not `/` (regular division)
- Check that `max_x` and `max_y` are calculated correctly

---

## ❌ Problem: Food spawns on the snake or in the same spot

**This is actually OK!** But if you want to fix it:

**Add this check in `spawn_food()`:**
```python
def spawn_food():
    while True:
        x = random.randint(0, max_x - 1)
        y = random.randint(0, max_y - 1)
        
        # Check if this position is occupied by snake
        if [x, y] not in snake:
            return [x, y]  # Safe position found!
```

---

## ❌ Problem: Snake can turn 180 degrees and die immediately

**What's happening:** You can press left while moving right, causing instant death

**Solution:**
This is why Step 4 introduces `next_direction`:
```python
# Check that new direction is not opposite
if event.key == pygame.K_UP and direction != [0, 1]:
    next_direction = [0, -1]
elif event.key == pygame.K_DOWN and direction != [0, -1]:
    next_direction = [0, 1]
# etc...
```

The checks (`and direction != ...`) prevent 180-degree turns.

---

## ❌ Problem: Code runs but nothing is visible

**Check these things:**

1. **Window size is 0?**
   ```python
   WINDOW_WIDTH = 800   # ✓ Good
   WINDOW_WIDTH = 0     # ✗ Bad
   ```

2. **Drawing code is wrong?**
   ```python
   pygame.draw.rect(screen, color, (x, y, width, height))
   ```

3. **pygame.display.flip() missing?**
   This line is required to show changes:
   ```python
   pygame.display.flip()  # Don't forget!
   ```

**Fix:**
- Check all dimensions are > 0
- Make sure pygame.display.flip() is in the loop
- Verify colors are tuples like (255, 0, 0)

---

## ❌ Problem: Game runs but looks weird

**Possible issues:**

1. **Grid size too small or large**
   ```python
   GRID_SIZE = 1   # Too small (can't see)
   GRID_SIZE = 20  # Good
   GRID_SIZE = 100 # Too large (only few squares)
   ```

2. **Colors aren't RGB tuples**
   ```python
   GREEN = (0, 255, 0)    # ✓ Correct
   GREEN = "green"        # ✗ Wrong
   GREEN = (0, 255)       # ✗ Wrong (need 3 values)
   ```

3. **Drawing order wrong**
   Sprites draw ON TOP of what was drawn before
   ```python
   screen.fill(BLACK)           # Background
   # Draw snake (on top of background)
   # Draw food (on top of snake if overlapping)
   pygame.display.flip()        # Show everything
   ```

**Fix:**
- Use recommended values from the code
- Use RGB tuples: (Red, Green, Blue)
- Fill background first, then draw sprites

---

## 🔍 Debugging Techniques

### Technique 1: Print Everything
```python
print(f"Snake: {snake}")
print(f"Food: {food}")
print(f"Head: {snake[0]}")
print(f"Collision? {snake[0] == food}")
```

Run and watch the console to see values change.

### Technique 2: Trace Step-by-Step
Add a delay to slow things down:
```python
import time
time.sleep(0.5)  # Wait 0.5 seconds between frames
```

Or reduce FPS:
```python
FPS = 2  # Very slow, easy to watch
```

### Technique 3: Simplify to Test
Remove complicated parts:
```python
# Comment out collision detection temporarily
# if snake[0] == food:
#     game_over = True
```

Test if basic movement works, then add features back.

### Technique 4: Copy Working Code
If your code is broken, use Step 7 as a base and add ONE THING at a time. This way you can identify exactly what breaks the code.

---

## 📞 When to Ask for Help

**Ask your teacher if:**
- You get an error you don't understand
- The code runs but doesn't do what you expect
- You tried 3 different fixes and nothing worked
- You want to add a feature but don't know how

**Try to fix yourself first:**
- Read the error message carefully
- Check indentation and spelling
- Look for similar code that works
- Use print() to debug

---

## 💡 Pro Tips

1. **Save versions of your code** (step7_my_version.py, step7_v2.py, etc.)
   - If you break it, you have a backup!

2. **Make one small change at a time**
   - Change one thing, test it, then change another
   - This way you know which change broke things

3. **Use comments to mark your changes**
   ```python
   # MY CHANGE: Made snake bigger
   GRID_SIZE = 30
   ```

4. **Test edge cases**
   - What happens if snake is in a corner?
   - What if food spawns at edge?
   - What if you press 5 keys at once?

---

**Good luck debugging! Remember: errors are learning opportunities! 🚀**
