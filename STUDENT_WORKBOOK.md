# 📝 Student Workbook & Progress Tracker

**Name**: ________________________     **Date**: ________________

---

## 📅 Class 1: Foundation & Movement

### Before Class
- [ ] I have pygame installed (`pip install pygame`)
- [ ] I've read the README.md

### During Class

**Step 1 - Setup & Drawing**
- [ ] I ran step1_setup.py successfully
- [ ] I understand that GRID_SIZE = 20 means each square is 20×20 pixels
- [ ] I modified the code to change one thing (color? position? grid size?)

**What I learned:**
_________________________________________________________________

**Step 2 - Draw Snake**
- [ ] I ran step2_draw_snake.py successfully
- [ ] I understand that [20, 15] is a grid position, not pixels
- [ ] I can explain why we multiply by GRID_SIZE when drawing

**What I learned:**
_________________________________________________________________

**Step 3 - Move Snake**
- [ ] I ran step3_move_snake.py successfully
- [ ] I can trace the movement: insert(0, ...) adds head, pop() removes tail
- [ ] I modified the code to make the snake move in a different direction

**What I learned:**
_________________________________________________________________

### Reflection Questions (Write 2-3 sentences)

1. **What does the % symbol do?** 
   ________________________________________________________________

2. **Why do we need both insert() and pop()?**
   ________________________________________________________________

3. **How is the snake like a train on a circular track?**
   ________________________________________________________________

### Homework
- [ ] Draw a picture of snake movement with labels
- [ ] Write pseudocode (English steps) for snake movement

---

## 📅 Class 2: Input & The Queue Algorithm

### During Class

**Step 4 - Player Input**
- [ ] I ran step4_player_input.py successfully
- [ ] I can control the snake with arrow keys
- [ ] I understand why `next_direction` prevents 180-degree turns

**What I learned:**
_________________________________________________________________

**Step 5 - Queue Growth** ⭐ MOST IMPORTANT STEP ⭐
- [ ] I ran step5_queue_growth.py successfully
- [ ] I can explain the difference between normal movement and growth
- [ ] I understand: NOT calling pop() makes the snake grow by 1

**What I learned:**
_________________________________________________________________

### Critical Reflection (This is the heart of the assignment!)

**Draw and label what happens:**

```
Normal Movement:
[   ][   ][   ]   →  [   ][   ][   ]
head body tail       head body tail

After Eating Food:
[   ][   ][   ]   →  [   ][   ][   ][   ]
head body tail       head body tail NEW!
```

**Explanation in your words:**
When the snake eats food, we _____________________________________

When the snake doesn't eat, we ____________________________________

---

## 📅 Class 3: Game Mechanics

### During Class

**Step 6 - Food & Collision**
- [ ] I ran step6_food_collision.py successfully
- [ ] Food appears randomly on the grid
- [ ] Snake grows when eating food
- [ ] I saw the score increase

**What I learned:**
_________________________________________________________________

**Step 7 - Game Over**
- [ ] I ran step7_game_over.py successfully
- [ ] I made the snake crash into a wall
- [ ] I made the snake crash into itself
- [ ] I understand all three collision types

**What I learned:**
_________________________________________________________________

### Collision Detection Checklist

**List all the things that can happen when snake moves:**
- [ ] Hits food → _________________________________
- [ ] Hits wall → _________________________________
- [ ] Hits self → _________________________________

**Test each one!** Can you make it happen?

### Challenge Question
**If the snake is 5 segments long, how many things can it collide with?**

(HINT: Count head + all body segments)

Answer: _______

---

## 📅 Class 4: Polish & Your Own Ideas

### During Class

**Step 8 - Final Version**
- [ ] I ran step8_final_version.py successfully
- [ ] I played and got a high score: ________
- [ ] I understand the speed increases as score goes up
- [ ] I identified at least 3 visual improvements from Step 7

**What I learned:**
_________________________________________________________________

### Code Exploration

**Which part of the code interests you most?**

[ ] Input handling (arrow keys)
[ ] Movement algorithm (insert/pop)
[ ] Collision detection (hitting things)
[ ] Random spawning (food)
[ ] Speed scaling (getting harder)
[ ] Graphics (drawing/colors)

**Why?** _________________________________________________________

### My Modification

**I modified the code to:** 
_________________________________________________________________

**How I did it:**
_________________________________________________________________

**Did it work?** [ ] Yes [ ] No [ ] Partially

**What broke (if anything)?**
_________________________________________________________________

---

## 🎯 Final Reflection

### The Queue Algorithm - Prove You Understand It!

**Can you explain this in ONE sentence without looking at the code?**

When the snake eats food, ___________________________________________
_________________________________________________________________

**Grade your understanding:**
[ ] I can teach this to someone else
[ ] I can explain it in my own words
[ ] I understand most of it
[ ] I'm still confused

---

## 🚀 What's Next?

**Which challenge interests you?**

[ ] Colorful Food (Green Level)
[ ] Obstacles (Yellow Level)
[ ] Two-Player Game (Red Level)
[ ] Something I thought of: _____________________________

**Why?** _________________________________________________________

---

## 🏆 Reflection on the Process

1. **What was the hardest part of this project?**
   _________________________________________________________________

2. **When did you understand the queue algorithm?**
   [ ] Step 3 [ ] Step 4 [ ] Step 5 [ ] Step 6 [ ] Still working on it

3. **How is this different from what you thought coding would be?**
   _________________________________________________________________

4. **What surprised you?**
   _________________________________________________________________

5. **Would you want to make more games? Why or why not?**
   _________________________________________________________________

---

## 📊 Your Achievements

**Check the ones you've done:**
- [ ] Wrote code that ran successfully
- [ ] Modified code without breaking it
- [ ] Understood the queue algorithm
- [ ] Debugged a problem
- [ ] Played the game and got a high score
- [ ] Added a feature of my own
- [ ] Helped a classmate understand something
- [ ] Thought deeply about the algorithm

**How many did you check?** _____ out of 8

---

**Date Completed**: ________________

**Teacher Signature**: ______________________________

---

**Great work! You learned real programming concepts. 🎮**

*Keep coding!*
