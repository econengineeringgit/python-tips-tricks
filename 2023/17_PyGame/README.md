# PyGame

---

## How does a game work?
Needs a loop that runs forever -> Only when window is closed

The 3 phases of games:
1. Handle events
2. Game logic
3. Render

The "main_next.py" is an example game of flappy bird. A minimalistic version.<br>
<br>
The logic behind flappy bird:
- Not the bird goes from left to right, but the pipes goes from right to left (and if there is, then the background too.)
- Constant "gravity" is applied to the "bird" so the bird goes down (by increasing its y value)
- When SPACE is pressed, for some frame the "bird" goes upwards
- If the bird hits the pipes its Game Over
- If the bird goes between the two pipes, it scores a point