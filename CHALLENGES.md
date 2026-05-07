# 🎮 Challenge Levels: Take Your Snake Game Further!

After completing Step 8, try these challenges! Each one teaches a new concept.

---

## 🟢 GREEN Level (Easy - Good for practicing loops/if-else)

### Challenge 1: Colorful Food
**Problem**: Food is boring. Make it change color based on what it is!

**Algorithm**:
```
If food_type == "normal": color = RED, worth 1 point
If food_type == "special": color = GOLD, worth 5 points  
If food_type == "poison": color = PURPLE, worth -1 point
```

**Hints**:
- Add `food_type` variable next to `food`
- Modify `spawn_food()` to return [x, y, type]
- When drawing food, check the type and use different color
- When eating, check type to decide points

**New Concept Learned**: Data structures with multiple properties

---

### Challenge 2: Display Difficulty Level
**Problem**: Show which "level" the player is on based on score

**Algorithm**:
```
Level 1: Score 0-4
Level 2: Score 5-9
Level 3: Score 10-14
...and so on
```

**Hints**:
- Create function: `def get_level(score): return score // 5 + 1`
- Display level on screen
- Maybe change background color per level?

**New Concept Learned**: Using division to categorize data

---

## 🟡 YELLOW Level (Medium - Understanding data and algorithms)

### Challenge 3: Obstacles! (The Big One)
**Problem**: The game is too easy! Add walls that snake can't pass.

**Algorithm**:
```
Create list of obstacles: obstacles = [[50, 50], [51, 50], ...]
Each frame, after moving head:
  - Check if head hit any obstacle
  - If yes, game over!
```

**Hints**:
- Add `obstacles = []` list at top
- Draw obstacles as GRAY rectangles
- In collision detection, add: 
  ```python
  for obstacle in obstacles:
      if snake[0] == obstacle:
          game_over = True
  ```
- Create 3-4 obstacles manually OR randomly

**Challenge Within Challenge**: 
- Can you create a maze pattern with obstacles?
- Can you prevent food from spawning on obstacles?

**New Concept Learned**: Collision with multiple object types

---

### Challenge 4: Snake History (Motion Trail)
**Problem**: Show where the snake has been!

**Algorithm**:
```
Keep a list of all positions the snake has been
Each frame, add current head position
Draw all old positions in faint color
```

**Hints**:
- Add `history = []`
- Each frame: `history.append(snake[0])`
- Loop through history and draw in dark green
- Optional: limit history to last 20 positions

**New Concept Learned**: Recording state over time

---

## 🔴 RED Level (Hard - Real programming challenges)

### Challenge 5: Two-Player Snake (WASD + Arrows)
**Problem**: Make it competitive! Two snakes, one controls with arrows, one with WASD.

**Algorithm**:
```
snake_1 = [head, body, body]   # Controlled with arrows
snake_2 = [head, body, body]   # Controlled with WASD

Each frame:
  - Move both snakes
  - Check if either hits wall or self
  - Check if either eats food (same food, first one wins!)
  - Check if they hit EACH OTHER
```

**Hints**:
- Add `snake_2`, `direction_2`, `next_direction_2`
- Copy all movement/collision code for snake_2
- When drawing, use different colors
- When eating food, check snake_1[0] first, then snake_2[0]

**Challenge**: Who wins? First to score 10 points? Longest alive?

**New Concept Learned**: Managing multiple game objects, complex collision

---

### Challenge 6: Smart Food (It Moves!)
**Problem**: Food tries to escape! It moves away from snake.

**Algorithm**:
```
Each frame, food moves:
  If snake is to the left, food moves right
  If snake is above, food moves down
  etc.
```

**Hints**:
- Check if `snake[0][0] < food[0]` (snake left of food)
- If yes, `food[0] += 1` (move food right)
- Handle boundary wrapping same as snake
- Maybe add a delay so food doesn't move EVERY frame

**New Concept Learned**: Algorithmic AI behavior

---

### Challenge 7: High Score File (Persistence)
**Problem**: High scores disappear when you close the game!

**Algorithm**:
```
When game closes:
  Write high_score to a file "highscore.txt"

When game starts:
  Read "highscore.txt" and load it
```

**Hints**:
- At the end of the program:
  ```python
  with open("highscore.txt", "w") as f:
      f.write(str(high_score))
  ```
- At the start:
  ```python
  try:
      with open("highscore.txt", "r") as f:
          high_score = int(f.read())
  except:
      high_score = 0
  ```

**New Concept Learned**: File I/O (reading/writing files)

---

### Challenge 8: Speed Modes (Hard Mode!)
**Problem**: Let players choose difficulty at start

**Algorithm**:
```
At startup, show menu:
  Press 1 for Easy (slow)
  Press 2 for Normal (medium)
  Press 3 for Hard (fast)

Set FPS based on choice
```

**Hints**:
- Add `difficulty = None` at start
- Create a "menu" state before game starts
- Read input: if '1' pressed, set BASE_FPS = 5
- Loop: `while difficulty is None: wait for input`

**Challenge**: Add a pause menu in-game too (Press P)

**New Concept Learned**: Game states and menus

---

## 🟣 PURPLE Level (Expert - Combine everything!)

### Challenge 9: Full Game Suite
**Problem**: Combine multiple challenges into one mega-game!

**Create**:
- Difficulty selector menu
- Colorful, valuable foods
- Obstacles and mazes
- Two-player mode
- High score tracking
- Motion trail
- Speed that increases with level

**This is a REAL game now!** 🎮

---

## 🏆 Bonus: Design Your Own Challenge

**You've learned the algorithm!** Now create something new:

1. **Think of a feature you want**: (weapon? shield? teleport? combo system?)
2. **Break it into steps**: (What data do I need? How do I check it?)
3. **Implement it**: (Write the code)
4. **Test it**: (Does it work? Can you break it?)
5. **Share it**: (Show your teacher/classmates!)

---

## 🔗 Concept Progression

```
EASY: 
  - Simple variable changes
  - More colors/drawing
  
MEDIUM:
  - New lists/data structures
  - Multiple collision types
  
HARD:
  - Multiple game objects
  - File I/O
  - Game states
  
EXPERT:
  - Combine all concepts
  - Create your own features
```

---

## 💡 Debugging Checklist

When something breaks:
- [ ] Print out variables to see their values
- [ ] Trace through the algorithm step-by-step
- [ ] Check your if/else conditions
- [ ] Make sure lists are created before using them
- [ ] Check indentation (Python cares about spaces!)
- [ ] Run from Step 7 as a base, add one thing at a time

---

**Remember**: Every bug is a learning opportunity! Good luck! 🚀
