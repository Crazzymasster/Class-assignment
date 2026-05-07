# Teaching Guide: Snake Game (4-Class Structure)

## 🎯 Overall Philosophy

This assignment teaches **algorithmic thinking** through progressive problem-solving:
- Each class builds on the previous one
- Students write **minimal code** - focus is on understanding the algorithm
- Reflection questions encourage discussion about *why* the code works
- By the end, students understand **game loops**, **data structures**, and **collision detection**

---

## 📅 Class 1: Foundation (60 minutes)

### Time Allocation
- **5 min**: Discuss: "What is an algorithm?" → list of steps to solve a problem
- **15 min**: Run `step1_setup.py` → ask questions about coordinates and colors
- **15 min**: Run `step2_draw_snake.py` → discuss grid vs pixel coordinates
- **15 min**: Run `step3_move_snake.py` → trace through the movement algorithm
- **10 min**: Reflection & preview of next class

### Key Concepts to Emphasize

**Grid Coordinates vs Pixels**
- Show: `[20, 15]` is a position on the grid
- Show: `* GRID_SIZE` converts to pixel coordinates for drawing
- Question: "Why do we do this? Why not just use pixels?"

**The Movement Algorithm (Step 3)**
```
1. Calculate new head: head_x = current_x + direction_x
2. Wrap around: use modulo (%)
3. Insert at front: snake.insert(0, [head_x, head_y])
4. Remove tail: snake.pop()
```
- Trace through one movement cycle together
- Question: "What does insert(0, ...) do?" vs "What does pop() do?"
- This introduces the concept that will be crucial in Step 5

**Homework/Reflection**
- Write down the 4 steps of snake movement in your own words
- Try modifying `step3_move_snake.py` to start moving left instead of right

---

## 📅 Class 2: Input & Queue Logic (60 minutes)

### Time Allocation
- **5 min**: Homework review - did they modify step3?
- **10 min**: Run `step4_player_input.py` → practice controlling the snake
- **10 min**: Discuss: Why do we need `next_direction` buffer? (avoid 180° turns)
- **20 min**: Run `step5_queue_growth.py` → THE CRITICAL CONCEPT
- **10 min**: Trace through growth algorithm step-by-step
- **5 min**: Reflection & celebration of understanding

### Key Concepts to Emphasize

**Player Input (Step 4)**
- Discuss the `next_direction` buffer
- Question: "What happens if you remove next_direction and just use direction?"
- Let them test it - they'll see the snake can turn into itself immediately
- This teaches about **buffering input** (real games do this too!)

**Queue Logic & Growth (Step 5) - MAIN LEARNING**

This is the crucial moment! Make sure they deeply understand this:

```python
if ate_food:
    # Don't remove tail - so body grows by 1!
else:
    snake.pop()  # Normal movement - stays same length
```

**Drawing & Analogy**:
- Draw on whiteboard: `[HEAD] -> [Body] -> [Body] -> [TAIL]`
- Normal movement: "Remove from tail, add to head → same length"
- Growth: "Add to head, DON'T remove tail → grows by 1"

**Real-World Analogy**:
- "Imagine a train on a circular track"
- "Normally: add car to front, remove car from back = same train"
- "Growth: add car to front, DON'T remove from back = longer train"

**Reflection Questions** (Have them write answers):
1. What's the difference between `if ate_food` and `else`?
2. If you press SPACE 5 times, how many segments does the snake grow?
3. Why does the code `snake.pop()` not happen when we eat food?

**Homework/Extension**
- Modify step5 to only grow by 1 segment per food (add a counter)
- Predict: If food is eaten 5 times, how long is the snake?

---

## 📅 Class 3: Game Mechanics (60 minutes)

### Time Allocation
- **10 min**: Homework review + run `step6_food_collision.py`
- **15 min**: Understand food spawning with `random.randint()`
- **15 min**: Trace collision detection: `if snake[0] == food`
- **10 min**: Run `step7_game_over.py` → add collision rules
- **10 min**: Identify all collision checks and discuss logic

### Key Concepts to Emphasize

**Food Spawning (Step 6)**
- Question: "How does the game know where to put food?"
- Show: `random.randint(0, max_x - 1)` picks random grid cell
- Question: "What if food spawns on the snake? Should we prevent it?"
  (This leads to interesting problem-solving!)

**Collision Detection**
```python
# Three types:
1. Head == Food → eat, grow, spawn new food
2. Head in boundary → game over
3. Head == any body segment → game over
```

Walk through the logic:
- Step 6: Only teaches food collision
- Step 7: Adds wall + self collision
- Show how each if/else statement checks different conditions

**Common Mistake** (discuss proactively):
- Question: "In self-collision, why do we check `range(1, len(snake))` not `range(0, len(snake))`?"
- Answer: "The head can't collide with itself (index 0), only with body!"

**Homework/Extension**
- Test game thoroughly: How many ways can you make the snake die?
- Try to beat a high score

---

## 📅 Class 4: Polish & Reflection (60 minutes)

### Time Allocation
- **5 min**: Play `step7_game_over.py` for fun
- **10 min**: Run `step8_final_version.py` → see polished version
- **15 min**: Identify enhancements (speed scaling, high score, visuals)
- **20 min**: Code exploration - students modify and experiment
- **10 min**: Final reflection & future ideas

### Key Concepts to Emphasize

**Difficulty Scaling (Step 8)**
- Function `calculate_fps(score)`: speed increases with score
- Question: "Why does the game get harder as you succeed?"
- This teaches about **difficulty curves** in game design

**Code Organization**
- Helper functions: `spawn_food()`, `calculate_fps()`
- Constants at the top: `WINDOW_WIDTH`, `GRID_SIZE`, colors
- Why organize this way? (Easier to modify, read, debug)

**Visual Polish**
- Grid background (faint lines)
- Different colors for head vs body
- Food as a circle instead of square
- Semi-transparent game-over overlay

**Student Challenges** (Pick 1-2 based on interest):
1. **Speed Challenge**: Modify `calculate_fps()` - make it harder/easier
2. **Visual Challenge**: Change colors, make food fancy, add animations
3. **Logic Challenge**: Add obstacles the snake can't pass
4. **Data Challenge**: Add a "food combo" system (eating multiple foods fast = bonus)
5. **Level Challenge**: Create levels with increasing difficulty

### Final Reflection Discussion

Ask students to write/discuss:

1. **What algorithm concepts did you learn?**
   - (Expected: grid logic, queues, collision detection, loops)

2. **Describe the snake growth algorithm in one sentence**
   - (This is the test of true understanding!)

3. **If you wanted to add something new to the game, what would it be?**
   - Let them brainstorm and help them think through the algorithm

4. **How is this game similar to other games you know?**
   - (Pac-Man, slither.io, Tron, etc.)

---

## 🔑 Key Teaching Moments

### Moment 1: Grid Coordinates (Class 1)
**Why important**: Helps students think in discrete logic, not continuous

**How to teach**: Show `[20, 15]` and ask "Where is this on the screen?" until they realize they need to multiply by GRID_SIZE

### Moment 2: Queue/Growth Algorithm (Class 2)
**Why important**: This is THE core algorithm - everything is built on this

**How to teach**: Draw it out, use analogies, have them trace through step-by-step

**Signs of understanding**: They can explain why `snake.pop()` doesn't happen when food is eaten

### Moment 3: Collision Detection (Class 3)
**Why important**: Teaches if/else logic and boundary conditions

**How to teach**: Show all three collision types, ask "What should happen in each case?"

### Moment 4: Code Organization (Class 4)
**Why important**: Real programming is about writing readable code

**How to teach**: Compare step7 (messy) with step8 (organized), ask "Which is easier to modify?"

---

## ⚠️ Common Student Mistakes & Solutions

| Mistake | Cause | Solution |
|---------|-------|----------|
| Snake doesn't appear | Forgot to draw in loop | Check indentation of draw code |
| Snake moves off screen | Wrapping logic wrong | Review modulo (%) operator |
| Snake grows without eating | Forgot to check food collision | Trace through: is food being eaten? |
| Game doesn't respond to keys | Event handling wrong | Check KEYDOWN inside event loop |
| Collision detection broken | Wrong comparison logic | Print snake[0] and food to debug |

---

## 🚀 Extensions for Fast Learners

After completing step 8, students can try:

1. **Add obstacles**: Randomly place walls that snake can't pass
2. **Power-ups**: Special food that does different things (invincibility, slow-motion)
3. **Two-player snake**: Second player controls with WASD
4. **Settings menu**: Let players adjust difficulty/colors/speed
5. **High score file**: Save high scores to a file
6. **Smooth animation**: Make snake move more fluidly (harder!)

---

## 📝 Assessment Ideas

### What I'm Looking For (Algorithmic Thinking):
- ✅ Can they explain the queue growth algorithm?
- ✅ Can they identify collision detection points?
- ✅ Can they modify code without breaking it?
- ✅ Do they ask "why" before "how"?

### Not Looking For:
- ❌ Perfect code formatting
- ❌ Advanced Python features
- ❌ Artistic game design
- ❌ Speed of completion

---

## 💡 Final Note for Teachers

The goal is **not a finished game** - it's understanding that:
- **Coding is algorithms** (step-by-step instructions)
- **Algorithms solve problems** (moving, growing, detecting collisions)
- **Constraints matter** (grid size, speed, boundaries)
- **Testing is crucial** (play the game, find edge cases!)

Celebrate small wins:
- "You understood how the queue works!" 
- "You found a bug in the collision detection!"
- "You modified the code and it still works!"

These moments matter more than a high score. 🎮
